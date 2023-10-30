from flask import Flask, render_template, redirect, url_for, request
import requests
from tokenflask import get_token




app = Flask(__name__)                             
Access_Token = get_token()
#################################################



@app.route('/input', methods=['POST', 'GET'])                                   

def pushingUserInput():
    if request.method == 'POST':
        usr = request.form['pt']
        return redirect(url_for('GetMyPet') )
   
    

##################################################

@app.route('/animals', methods=['POST','GET'])

def GetMyPet():
    

    headers = {
                'Authorization': 'Bearer '+ Access_Token
               }

    params  = {
                'type': 'dog'
                }

    response = requests.get('https://api.petfinder.com/v2/animals', params=params, headers=headers)

    displayinfo = response.json()          
    return displayinfo

  ################################################
    
if __name__ =='__main__':
    app.run(debug=True, port=8000)