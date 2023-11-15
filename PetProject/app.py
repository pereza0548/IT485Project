from flask import Flask, render_template, request
import requests
from api_keys import CALL_URL, access_token


app = Flask(__name__)


def getAnimalResponse(params, message):   
    headers = {
        "Authorization": "Bearer " + access_token
    }
    animalResponse = requests.get(CALL_URL, headers=headers, params= params)
    
    data =animalResponse.json().get('animals')

    if not data:
       return message
    return data

@app.route('/', methods=['GET', 'POST'])
def getParams():
    if request.method == 'POST':
        zipcode = request.form.get('zipcode')
        type = request.form.get('type')
        gender = request.form.get('gender')
        age = request.form.get('age')
        size = request.form.get('size')
        sort = request.form.get('sort')

        if len(zipcode) != 5:
             return render_template('zipError.html')
        
        # store user input
        params = {
                "location" : zipcode,
                "type" : type,
                "gender" : gender,
                "age": age,
                "size": size,
                "sort": sort
            }
        # Message to use when no pets in zipcode or 100 mile radius
        message = "No pets found around here. Please try a different set of filters. There's a pet waiting to come home with you."
           
        # calls function using params and message if there are pets
        # values will be returned if not message will be returned
        r = getAnimalResponse(params, message)

        if r == message:
                return render_template('preview.html', value=r, params = params)
        
        details = storeDetails(r)
        
        return render_template('index.html', value = details, all = r)
    
    return render_template('Home.html')




def storeDetails(details):
    animal_details = []
    for animal in details:
        filter_details={
            'name': animal.get('name', 'N/A'),
            'breeds': animal.get('breed', 'N/A'),
            'color' : animal.get('color', 'N/A'),
            'size': animal.get('size', 'N/A'),
            'gender': animal.get('gender', 'N/A'),
            'age': animal.get('age', 'N/A'),
            'environment' : animal.get('environment', 'N/A'),
            'attributes' : animal.get('attributes', 'N/A'),
            'photos' : animal.get('photos', 'N/A'),
            'breeds' : animal.get('breeds', 'N/A'),
            'description' : animal.get('description', 'N/A'),
            'url' : animal.get('url', 'N/A'),
            'contact' : animal.get('contact', 'N/A'),
            'coat' : animal.get('coat', 'N/A')
            }
        animal_details.append(filter_details)
    return animal_details

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
       "location" : 'Lebanon, KS',
       "distance" : '',
    
   }
   message = "The pets are shy, they will return later."

   rImg = getAnimalResponse(paramsStatic, message)
   animal_details = storeDetails(rImg)
   

   return render_template("Gallery.html", value=animal_details)


if __name__ == '__main__':
    app.run(debug=True)

    