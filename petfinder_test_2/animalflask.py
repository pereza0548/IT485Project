from flask import Flask, render_template, redirect, url_for, request
import requests
from tokenflask import get_token

app = Flask(__name__)                             
Access_Token = get_token()
CALL_URL = 'https://api.petfinder.com/v2/animals'
#################################################
@app.route('/input', methods=['POST', 'GET'])                                   
def pushingUserInput():
    if request.method == 'POST':
        
        aLocation = request.form.get('Location')
        aType = request.form.get('Type') 
        aGender = request.form.get('Gender')
        #aAge = request.form.get('Age')
        #aSize = request.form.get('Size')


        headers = {
                    'Authorization': 'Bearer '+ Access_Token
                    }

        params  = {
                    'type'    : aType,
                    'location': aLocation,
                    'gender'  : aGender,
                    #'age'     : aAge,
                    #'size'    : aSize
                    }
        response = requests.get(CALL_URL, params=params, headers=headers)

        #displayinfo = response.json()['animals'][0]['age'] This worked
        #displayinfo = response.json()['animals']#['contact'] #from first 20 animals
        #displayinfo = response.json()
        data = response.json().get('animals')
        filtered_data = []
        for animal in data:
            
            Address = {
                        'Street': animal.get('contact', 'N/A').get('address', 'N/A').get('address1', 'N/A'),
                        'City': animal.get('contact', 'N/A').get('address', 'N/A').get('city', 'N/A'),
                        'State': animal.get('contact', 'N/A').get('address', 'N/A').get('state', 'N/A'),
                        'Zip Code': animal.get('contact', 'N/A').get('address', 'N/A').get('postcode', 'N/A'),
                        'Country': animal.get('contact', 'N/A').get('address', 'N/A').get('country', 'N/A')
                      }
         #   goodwith  = animal.get('environment', 'N/A')
         #   for val in goodwith.values():
         #       if val != 'true':
         #           del goodwith[val]
            filtered_animal={
                'Address' : Address,
                'Distance' : animal.get('distance', 'N/A'),
                'Photo': animal.get('primary_photo_cropped').get('small', 'N/A'),
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

        return filtered_data            # This Dispays all related results
        #return filtered_data[0]        # This Displays first related result for example
        #return filtered_data[0:4]      # This Displays first Four related results as an example
        
  
  ################################################
if __name__ =='__main__':
    app.run(debug=True, port=8000)