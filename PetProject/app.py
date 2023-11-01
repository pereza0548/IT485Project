from flask import Flask, render_template, request, jsonify
import requests
import json
from api_keys import CALL_URL, access_token

app = Flask(__name__)


@app.route('/')
def getAnimalResponse():    
    # state = request.form['state']
    # type = request.form['type']
    # gender = request.form['gender']
    # age = request.form['age']
    # size = request.form['size']

    headers = {
        "Authorization": "Bearer " + access_token
    }

    params = {
            "location" : "MA",
            "distance" : 30,
            "type" : "",
            "gender" : "",
            "age": "Young",
            "size": "small" 
            }


    animalResponse = requests.get(CALL_URL, headers=headers, params= params)

    data = animalResponse.json().get('animals')

    return render_template('index.html', value = data)
