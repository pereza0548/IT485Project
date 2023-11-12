from flask import Flask, render_template, request, jsonify
import requests
import json
from api_keys import CALL_URL, access_token
import re

app = Flask(__name__)

# used a regular expression to check zipcode format
def valid_zip(zipcode):
        return re.match(r'^\d{5}$', zipcode) is not None


@app.route('/', methods=['GET', 'POST'])

def getAnimalResponse(): 
    if request.method == 'POST': 

        location = request.form.get('zipcode') #had to change so it works with the updated html
        type = request.form.get('type')
        gender = request.form.get('gender')
        age = request.form.get('age')
        size = request.form.get('size')

        # if the zipcode entered is wrong format it returns the error page
        if not valid_zip(location):
            return render_template ('zipError.html')


        headers = {
            "Authorization": "Bearer " + access_token
        }

        params = {
            "location" : location, 
            "distance" : 30,
            "type" : type,
            "gender" : gender,
            "age": age,
            "size": size 
        }
        
        animalResponse = requests.get(CALL_URL, headers=headers, params= params)
        
        data = animalResponse.json().get('animals')

        filtered_data = []
        for animal in data:
        #added the filters Ahmed made
            Address = {
                        'Street': animal.get('contact', 'N/A').get('address', 'N/A').get('address1', 'N/A'),
                        'City': animal.get('contact', 'N/A').get('address', 'N/A').get('city', 'N/A'),
                        'State': animal.get('contact', 'N/A').get('address', 'N/A').get('state', 'N/A'),
                        'Zip Code': animal.get('contact', 'N/A').get('address', 'N/A').get('postcode', 'N/A'),
                        'Country': animal.get('contact', 'N/A').get('address', 'N/A').get('country', 'N/A')
                      }
        
            filtered_animal={
                'Address' : Address,
                'Distance' : animal.get('distance', 'N/A'),
                # photo gave me a type error so i just commented it out for now
                #'Photo': animal.get('primary_photo_cropped').get('small', 'N/A'),
                'Name': animal.get('name', 'N/A'), 
                'Type': animal.get('type', 'N/A'),
                'Size': animal.get('size', 'N/A'),
                'Gender': animal.get('gender', 'N/A'),
                'Age' : animal.get('age', 'N/A'),
                'breeds' : animal.get('breeds', 'N/A').get('primary'),
                #'Good with' : animal.get('environment', 'N/A'),
                'Email': animal.get('contact', 'N/A').get('email', 'N/A'),
                'Phone': animal.get('contact', 'N/A').get('phone', 'N/A'),
                'Description': animal.get('description', 'N/A')
                }
            
            filtered_data.append(filtered_animal)
        
        # makes an error page if there are no results
        if not filtered_data:
             return render_template('noresults.html') 
        
        return render_template('index.html', value=filtered_data)
    
    return render_template('index.html', value=[])

if __name__ == '__main__':
    app.run(debug=True, port=8000)
