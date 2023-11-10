from flask import Flask, render_template, redirect, url_for, request
import requests





app = Flask(__name__)      



@app.route('/tokenresponse', methods=['POST', 'GET']) 
def get_token():
        data = {
        'grant_type': 'client_credentials',
        'client_id': 'key',
        'client_secret': 'secret',
        }

        response = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)
    
        My_token = response.json()['access_token']
    
        return My_token     

  ########################################
    
if __name__ =='__main__':
    app.run(debug=True, port=8000)

    