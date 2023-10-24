from flask import Flask, render_template, request
import requests
import json
from api_keys import API_KEY, USER_AGENT, URL

app = Flask(__name__)
@app.route('/')
def form():
        return render_template('index.html')

@app.route('/', methods =['POST', 'GET'])
def my_form_post(): 
    artist = request.form['artist']
    # album = request.form['album']
    # country = request.form['country']
    # tag = request.form['tag']

     
    payload = {                             
    'method'  : 'artist.getInfo',             
    'artist'  : artist,                   
    'api_key' : API_KEY,
    'format'  : 'json'
    }

    # getMethods(request.form)
    Data = Data_Artistsearch(payload)
    return render_template('index.html', value = Data)


def Data_Artistsearch(payload):             
    r = requests.get(URL, params= payload)
    Data = r.json()
    artist = Data.get('artist')
    Summary = removeTag(getSummaryFromArtist(artist))
    # Stats = getStats(artist)
    return Summary

def getSummaryFromArtist(artist):
     return artist.get("bio").get("summary")

def removeTag(string):
     return string.split("<",1)[0]

# def getStats(artist):
#      listeners = artist.get('stats').get('listeners')
#      return listeners

if __name__ == '__main__':
    app.run(debug=True) 

# artist, album, country, tag = list

# def index():
#     req = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
#     data = json.loads(req.content)
#     return render_template('index.html', data=data['data'])


