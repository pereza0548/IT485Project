from flask import Flask, render_template, request, jsonify
import requests
import json
from api_keys import CALL_URL, access_token

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def getAnimalResponse(): 
    if request.method == 'POST': 
        state = request.form.get('state')
        type = request.form.get('type')
        gender = request.form.get('gender')
        age = request.form.get('age')
        size = request.form.get('size')

        headers = {
            "Authorization": "Bearer " + access_token
        }

        params = {
            "location" : state, # made this state so it shows pets in the selected state, otherwise it kept showing the same animals based on the set location
            "distance" : 30,
            "state": state,
            "type" : type,
            "gender" : gender,
            "age": age,
            "size": size 
        }
        
        animalResponse = requests.get(CALL_URL, headers=headers, params= params)
        
        data = animalResponse.json().get('animals')

        filtered_data = []
        for animal in data:
            # can add more filters here or change what we want to display
            filtered_animal={
                'name': animal.get('name', 'N/A'), 
                'age' : animal.get('age', 'N/A'),
                'Good with' : animal.get('Good with', 'N/A'),
                'breeds' : animal.get('breeds', 'N/A')
            }
            
            filtered_data.append(filtered_animal)

        
        return render_template('index.html', value = filtered_data)
    
    return render_template('index.html', value=None)



if __name__ == '__main__':
    app.run(debug=True, port=8000)
