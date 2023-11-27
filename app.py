from flask import Flask, render_template, request
from api_keys import CALL_URL, access_token, typeURL
from uszipcode import SearchEngine #pip install uszipcode
import requests, html

app = Flask(__name__)

# [1]
# DEFINE A FUNCTION  TO BE CALLED LATER
# TO MAKE THE API REQUEST AND STORE THE
# RESPONSE IN A VARIABLE NAMED "data"

def getAnimalResponse(params, message):   
    headers = {
        "Authorization": "Bearer " + access_token
    }
    animalResponse = requests.get(CALL_URL, headers=headers, params= params)
    
    data = animalResponse.json().get('animals')

    if not data:
       return message
    return data

# [2]
# DEFINE A FUNCTION TO VALIDATE AND CHECK THE POSTAL CODE
# ENTERED BY THE USER, RETURNING A MESSAGE IF ERROR!!

def valid_zip(zipcode, state):
    search = SearchEngine()
    zipcode_info = search.by_zipcode(zipcode)
    if zipcode_info and zipcode_info.state == state:
       return False
    else:
       return True

# [3]
# DEFINE A FUNCTION TO AGGREGATE THE FILTERED RESPONSE 
# THAT WAS BASED ON THE USER INPUT, IN A FORMAT OF A LIST 
# CONTAINING EACH ANIMAL INFO AS A DICTIONARY IN A LIST
def storeDetails(details):
    animal_details = []
    for animal in details:
        filter_details={
            'name': html.unescape(animal.get('name', 'N/A')),
            'breeds': animal.get('breeds', 'N/A'),
            'color' : animal.get('color', 'N/A'),
            'size': animal.get('size', 'N/A'),
            'gender': animal.get('gender', 'N/A'),
            'age': animal.get('age', 'N/A'),
            'environment' : animal.get('environment', 'N/A'),
            'attributes' : animal.get('attributes', 'N/A'),
            'photos' : animal.get('photos', 'N/A'),
            'description' : html.unescape(animal.get('description', 'N/A')),
            'url' : animal.get('url', 'N/A'),
            'contact' : animal.get('contact', 'N/A'),
            'coat' : animal.get('coat', 'N/A')
            }
        animal_details.append(filter_details)
    return animal_details


# [4] 
# DEFINE THE ROUTE TO COLLECT USER INPUT THEN PROCESS IT
@app.route('/', methods=['GET', 'POST'])

# [5]
#  GET THE PARAMETERS FROM USER INPUT
def getParams():                
    types = getTypes()   
    if request.method == 'POST':
        zipcode = request.form.get('zipcode')
        state = request.form.get('state')
        type = request.form.get('type')
        gender = request.form.get('gender')
        age = request.form.get('age')
        size = request.form.get('size')
        sort = request.form.get('sort')

        # [6]
        # VALIDATE THE ZIPCODE ENTERERED BY THE USER.
        if valid_zip(zipcode, state):
            return render_template('zipError.html', types = types)
        
        # [7]
        # RESTORE THE OPTAINED PARAMETERS IN VARIABLES
        # TO BE PASSED IN THE API CALL, IN THE PARAMS ARGUMENT.
        params = {
                "location" : zipcode, 
                "location" : state,
                "type" : type,
                "gender" : gender,
                "age": age,
                "size": size,
                "sort": sort
                }
        
        # [8]
        # DEFINE THE MESSAGE ARGUMENT TO FLAG THE 
        # UNAVAILABILITY IN THE PROVIDED ZIPCODE.
        message="No results found here, please try again to find your newest family member."

        # NOW MAKE THE API REQUEST BY CALLING THE 
        # getAnimalResponse() DEFINED EARLIER,
        # PASSING THE PARAMS AND MESSAGE TO BE
        # PROCCESSED WITH THE HEADER ARGUMENT.
        # vALUE WILL BE RETURNED IF A PET WAS FOUND,
        # OTHERWISE DISPLAY A MESSAGE.

        # [9]
        # STORE THE FILTERED RESPONSE IN A VARIABLE 'r'.
        r = getAnimalResponse(params, message)

        if r == message:
                return render_template('noresults.html', value=r, types = types)
        
        # [10]
        # RESTORE THE FILTERED RESPONSE AS A LIST OF DICTIONARIES
        # TO REPRESENT EACH AVAILABLE ANIMAL.
        details = storeDetails(r)
        
        return render_template('index.html', value = details, types = types)
    
    return render_template('Home.html', types = types)

# [11]
# GET TYPES OF ANIMAL GROUPS TO SEARCH BY FROM API 
def getTypes():
    headers = {
        "Authorization": "Bearer " + access_token
    }
    animalResponse = requests.get(typeURL, headers=headers)
    
    data =animalResponse.json().get('types')
   
    types = []
    for type in data:
        types.append(type.get('name'))
    return types

if __name__ == '__main__':
    app.run(debug=True, port=8000)

    
