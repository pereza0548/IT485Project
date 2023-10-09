##################################################################################################
#For some Reason on my vscode environment, it won't pop the simplist flask application in a browser,
# So I wasn't able to see if this code worked or not.
When I click on the golive server or run the code, it gives me error due to port issue.
##################################################################################################


from flask import Flask, Request, render_template, redirect, session
import requests
import json

         


app = Flask(__name__)                               

@app.route('/', methods =['GET'])                 

def Data():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'         # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
    'api_key' : API_KEY,                # Specifying the key to Identify myself to the API,
    'method'  : 'chart.gettopartists',  # The method to be used for the process, and the format
    'format'  : 'json'                  # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)

    return print(r.json()['artists']['@attr'])


if __name__ == '__main__':
    app.run() 



########################################################
#########    Notes For Clarification ###################
########################################################
# 1 #
# Here we import the flask library we need
# Next we create a variable named app and have
#  that equal to a function Flask which has in
#  its parentheses a special python variable __name__
# that tells the application flask that all what you 
# need to run this website is just here (./)the current directory
# no need to go any where for 

# 2 #

# @ is python decorator that add more functionality to a function
#  that we are going to reference down below.
# what comes after the @ is what we are going to decorate the funcion with
#which is the variable has the Flask function and the route or the location
# that is part of the Flask function.
# the ("/") is telling the function, once hit the root we will do somthng.
# Which will do next

# 3 #

# Here the function says When someone goes to the base URL 
# just simply return drink more coffee.

# 4 #

#This is basicly telling Flask to run
