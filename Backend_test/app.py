from flask import Flask, render_template, request, jsonify
import requests
import json
from api_keys import CALL_URL, access_token
import re

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
    
    data =animalResponse.json().get('animals')

    if not data:
       return message
    return data

# [2]
# DEFINE A FUNCTION TO VALIDATE AND CHECK THE POSTAL CODE
# ENTERED BY THE USER, RETURNING A MESSAGE IF ERROR!!

def valid_zip(zipcode):
        return re.match(r'^\d{5}$', zipcode) is not None

# [3]
# DEFINE A FUNCTION TO AGGREGATE THE FILTERED RESPONSE 
# THAT WAS BASED ON THE USER INPUT, IN A FORMAT OF A LIST 
# CONTAINING EACH ANIMAL INFO AS A DICTIONARY IN A LIST
def storeDetails(details):
    animal_details = []
    for animal in details:

        Address = {
                        'Street': animal.get('contact', 'N/A').get('address', 'N/A').get('address1', 'N/A'),
                        'City': animal.get('contact', 'N/A').get('address', 'N/A').get('city', 'N/A'),
                        'State': animal.get('contact', 'N/A').get('address', 'N/A').get('state', 'N/A'),
                        'Zip Code': animal.get('contact', 'N/A').get('address', 'N/A').get('postcode', 'N/A'),
                        'Country': animal.get('contact', 'N/A').get('address', 'N/A').get('country', 'N/A')
                      }
        
        filter_details={
            
            #'Address' : Address,            # THIS SHOULD DISPLAY THE ADDRESS WITH NO MISSED INFO
            'name': animal.get('name', 'N/A'),
            'breeds': animal.get('breed', 'N/A'),    #.get('primary'),
            'color' : animal.get('color', 'N/A'),
            'size': animal.get('size', 'N/A'),
            'gender': animal.get('gender', 'N/A'),
            'age': animal.get('age', 'N/A'),
            'environment' : animal.get('environment', 'N/A'),
            'attributes' : animal.get('attributes', 'N/A'),
            'photos' : animal.get('photos', 'N/A'),
            'description' : animal.get('description', 'N/A'),
            'url' : animal.get('url', 'N/A'),
            'contact' : animal.get('contact', 'N/A'),
            'coat' : animal.get('coat', 'N/A')

            #'Email': animal.get('contact', 'N/A').get('email', 'N/A'),#THIS SHOUD RETRIEVE THE EMAIL ONLY
            #'Phone': animal.get('contact', 'N/A').get('phone', 'N/A'),#THIS SHOULD RETRIEVE THE PHONE NUMBER ONLY

            
            }
        animal_details.append(filter_details)
    # Display the error page if there are no results
    if not animal_details:
        return render_template('noresults.html')
    else:
        return animal_details


# [4] 
# DEFINE THE ROUTE TO COLLECT USER INPUT THEN PROCESS IT
@app.route('/', methods=['GET', 'POST'])


# [5]
#  GET THE PARAMETERS FROM USER INPUT
def getParams():                   
    if request.method == 'POST':
        zipcode = request.form.get('zipcode')
        type = request.form.get('type')
        gender = request.form.get('gender')
        age = request.form.get('age')
        size = request.form.get('size')
        sort = request.form.get('sort')

        # [6]
        # VALIDATE THE ZIPCODE ENTERERED BY THE USER.
        if not valid_zip(zipcode):
            return render_template ('zipError.html')
        
        # [7]
        # RESTORE THE OPTAINED PARAMETERS IN VARIABLES
        # TO BE PASSED IN THE API CALL, IN THE PARAMS ARGUMENT.
        params = {
                "location" : zipcode,
                "type" : type,
                "gender" : gender,
                "age": age,
                "size": size,
                "sort": sort
            }
        
        # [8]
        # DEFINE THE MESSAGE ARGUMENT TO FLAG THE 
        # UNAVAILABILITY IN THE PROVIDED ZIPCODE.
        message = "No pets found around here. Please try a different set of filters. There's a pet waiting to come home with you."


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
                return render_template('preview.html', value=r, params = params)
        
        # [10]
        # RESTORE THE FILTERED RESPONSE AS A LIST OF DICTIONARIES
        # TO REPRESENT EACH AVAILABLE ANIMAL.
        details = storeDetails(r)
        
        return render_template('index.html', value = details, all = r)
    
    return render_template('Home.html')


@app.route("/Directions", methods= ['GET', 'POST'])
def directions():
        if request.method == 'POST':
            return getParams()
        return render_template("Directions.html")



@app.route("/Gallery", methods=['GET', 'POST'])
def gallery():
   if request.method == 'POST':
       return getParams()

   paramsStatic = {
       "location" : 'Denver, CO',
       "distance" : '100',
    
   }
   message = "The pets are shy, they will return later."

   rImg = getAnimalResponse(paramsStatic, message)
   animal_details = storeDetails(rImg)
   

   return render_template("Gallery.html", value=animal_details)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

    