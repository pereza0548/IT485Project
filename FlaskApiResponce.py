from flask import Flask
import requests

app = Flask(__name__)       # Get a flask object named app



###############################################################################
###############################################################################
###############################################################################
#__________________API METHODS FOR ALBUM QUERIES _____________________________#
#__________________That does not require authorization________________________#


#__________________1_ album.search      ->Search for an album by name. Returns album matches sorted by relevance
#__________________2_ album.getInfo     ->Get the metadata and tracklist for an album on Last.fm using the album name or a musicbrainz id.
#__________________3_ album.getTags     ->Get the tags applied by an individual user to an album on Last.fm
#__________________4_ album.getTopTags  -> Get the top tags for an album on Last.fm, ordered by popularity

###############################################################################
###############################################################################

# Let's work on each one to experiment the output using flask:
###############################################################################

# 1_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/album/search', methods=['GET'])

def Data_albumsearch():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'album.search',             # The method to be used for the process, and the format
    'album' : 'Thriller',                    
    'api_key' : API_KEY
    #'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 2_ Define a route to Get the metadata and tracklist for an album on Last.fm using the album name or a musicbrainz id.
@app.route('/album/getInfo', methods=['POST', 'GET'])

def Data_albumgetinfo():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'album.getInfo',             # The method to be used for the process, and the format
    'artist'  : 'Michael Jackson',
    'album' : 'Thriller',                    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 3_ Define a route to Search for the tags applied by an individual user to an album on Last.fm
@app.route('/album/getTags', methods=['POST','GET'])

def Data_albumgettags():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'album.getTags',             # The method to be used for the process, and the format
    'artist'  : 'Michael Jackson',
    'album' : 'Thriller',                    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 4_ Define a route to Search for the top tags for an album on Last.fm, ordered by popularity.
@app.route('/album/getTopTags', methods=['POST','GET'])

def Data_albumgettoptags():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'album.getTopTags',             # The method to be used for the process, and the format
    'artist'  : 'Michael Jackson',
    'album' : 'Thriller',                    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 


###############################################################################
###############################################################################
###############################################################################
###############################################################################

#__________________API METHODS FOR ARTIST QUERIES _____________________________#
#__________________That does not require authorization________________________#


#__________________1_ artist.search  -> Search for an artist by name. Returns artist matches sorted by relevance.
#__________________2_ artist.getInfo      ->Get the metadata for an artist. Includes biography, truncated at 300 characters.
#__________________3_ artist.getSimilar     ->Get all the artists similar to this artist
#__________________4_ artist.getTags  -> Get the tags applied by an individual user to an artist on Last.fm.
#__________________5_ artist.getTopTags  -> Get the top tags for an artist on Last.fm, ordered by popularity.
#__________________6_ artist.getTopAlbums  -> Get the top albums for an artist on Last.fm, ordered by popularity.
#__________________7_ artist.getTopTracks  -> Get the top tracks by an artist on Last.fm, ordered by popularity
#__________________8_ artist.getCorrection     ->Use the last.fm corrections data to check whether the supplied artist has a correction to a canonical artist

###############################################################################
###############################################################################
###############################################################################

# Let's work on each one to experiment the output using flask:
###############################################################################

# 1_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/artist/search', methods=['POST','GET'])

def Data_artistsearch():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'artist.search',
    'artist'  : 'Cher',             # The method to be used for the process, and the format                      
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 2_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/artist/getInfo', methods=['POST','GET'])

def Data_artistgetinfo():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'artist.getInfo',             # The method to be used for the process, and the format
    'artist'  : 'Cher',                    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 3_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/artist/getSimilar', methods=['POST','GET'])

def Data_artistgetsimilar():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'artist.getSimilar',             # The method to be used for the process, and the format
    'artist'  : 'Cher',                    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 4_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/artist/getTags', methods=['POST','GET'])

def Data_artistgetTags():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'artist.getTags',             # The method to be used for the process, and the format
    'artist'  : 'Cher',                    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 5_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/artist/getTopTags', methods=['POST','GET'])

def Data_artistgettoptags():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'artist.getTopTags',             # The method to be used for the process, and the format
    'artist' : 'Michael Jackson',                    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 6_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/artist/getTopAlbums', methods=['POST','GET'])

def Data_gettopalbums():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'artist.getTopAlbums',             # The method to be used for the process, and the format
    'artist' : 'Michael Jackson',                     
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 7_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/artist/getTopTracks', methods=['POST','GET'])

def Data_artistgettoptracks():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'artist.getTopTracks',             # The method to be used for the process, and the format
    'artist'  : 'Cher',                    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 8_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/artist/getCorrection', methods=['POST','GET'])

def Data_artistgetcorrection():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'artist.getCorrection',             # The method to be used for the process, and the format
    'artist'  : 'Cher',                    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 




###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#__________________API METHODS FOR TRACK QUERIES _____________________________#
#__________________That does not require authorization________________________#


#__________________1_ track.search  -> Search for a track by track name. Returns track matches sorted by relevance.
#__________________2_ track.getInfo      ->Get the metadata for a track on Last.fm using the artist/track name or a musicbrainz id.
#__________________3_ track.getSimilar     ->Get the similar tracks for this track on Last.fm, based on listening data.
#__________________4_ track.getTags  -> Get the tags applied by an individual user to a track on Last.fm.
#__________________5_ track.getTopTags  -> Get the top tags for this track on Last.fm, ordered by tag count. Supply either track & artist name or mbid
#__________________6_ track.getCorrection     ->Use the last.fm corrections data to check whether the supplied track has a correction to a canonical track
###############################################################################
###############################################################################
###############################################################################

# Let's work on each one to experiment the output using flask:

###############################################################################


# 1_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/track/search', methods=['POST','GET'])

def Data_tracksearch():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'track.search',             # The method to be used for the process, and the format
    'track'   : 'Believe',
    'artist'  : 'Cher',              # OPTIONAL     
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 2_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/track/getInfo', methods=['POST','GET'])

def Data_trackgetinfo():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'track.getInfo',             # The method to be used for the process, and the format
    'track'   : 'Believe',
    'artist'  : 'Cher',              # Required  
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 3_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/track/getSimilar', methods=['POST','GET'])

def Data_trackgetsimilar():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'track.getSimilar',             # The method to be used for the process, and the format
    'track'   : 'Believe',
    'artist'  : 'Cher',              # Required    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 4_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/track/getTags', methods=['POST','GET'])

def Data_trackgettags():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'track.getTags',             # The method to be used for the process, and the format
    'track'   : "I'll be by your side",
    'artist'  : 'Sally Shapiro',              # Required     
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 5_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/track/getTopTags', methods=['POST','GET'])

def Data_trackgetToptags():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'track.getTopTags',             # The method to be used for the process, and the format
    'track'   : 'Believe',
    'artist'  : 'Cher',              # required   
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 6_ Define a route to Search for an album by name. Returns album matches sorted by relevance
@app.route('/track/getCorrection', methods=['POST','GET'])

def Data_trackgetcorrection():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'track.getCorrection',             # The method to be used for the process, and the format
    'track'   : 'Mr. Brownstone',
    'artist'  : "Guns N' Roses",              # required     
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 


###############################################################################
###############################################################################
###############################################################################
#__________________API METHODS FOR TAG QUERIES _____________________________#
#__________________That does not require authorization________________________#


#__________________1_ tag.getInfo  -> Get the metadata for a tag
#__________________2_ tag.getSimilar      ->Search for tags similar to this one. Returns tags ranked by similarity, based on listening data.
#__________________3_ tag.getTopAlbums     ->Get the top albums tagged by this tag, ordered by tag count.
#__________________4_ tag.getTopArtists  -> Get the top artists tagged by this tag, ordered by tag count.
#__________________5_ tag.getTopTags  -> Fetches the top global tags on Last.fm, sorted by popularity (number of times used)
#__________________6_ tag.getTopTracks     ->Get the top tracks tagged by this tag, ordered by tag count.
#__________________7_ tag.getWeeklyChartList     ->Get a list of available charts for this tag, expressed as date ranges which can be sent to the chart services.
###############################################################################
###############################################################################


# Let's work on each one to experiment the output using flask:

###############################################################################

# 1_ Get the metadata for a tag

@app.route('/tag/getInfo', methods=['POST','GET'])

def Data_taggetinfo():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'tag.getInfo',             # The method to be used for the process, and the format
    'tag'   : 'disco',
       
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 2_ Search for tags similar to this one. Returns tags ranked by similarity, based on listening data.

@app.route('/tag/getSimilar', methods=['POST','GET'])

def Data_taggetsimilar():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'tag.getSimilar',             # The method to be used for the process, and the format
    'tag'   : 'Disco',    
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 3_ Get the top albums tagged by this tag, ordered by tag count.

@app.route('/tag/getTopAlbums', methods=['POST','GET'])

def Data_taggettopalbums():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'tag.getTopAlbums',             # The method to be used for the process, and the format
    'tag'   : 'Disco',             # required     
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 4_ Get the top artists tagged by this tag, ordered by tag count.

@app.route('/tag/getTopArtists', methods=['POST','GET'])

def Data_taggettopartists():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'tag.getTopArtists',             # The method to be used for the process, and the format
    'tag'   : 'Disco',             # required     
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 5_ Fetches the top global tags on Last.fm, sorted by popularity (number of times used)

@app.route('/tag/getTopTags', methods=['POST','GET'])

def Data_taggettoptags():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'tag.getTopTags',             # The method to be used for the process, and the format
    'api_key' : API_KEY,             # Only the Api key is required     
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 6_ Get the top tracks tagged by this tag, ordered by tag count.

@app.route('/tag/getTopTracks', methods=['POST','GET'])

def Data_taggettoptracks():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'tag.getTopTracks',             # The method to be used for the process, and the format
    'tag'  : "Disco",              # required     
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 7_ Get a list of available charts for this tag, expressed as date ranges which can be sent to the chart services.

@app.route('/tag/getWeeklyChartList', methods=['POST','GET'])

def Data_taggetweeklychartlist():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'tag.getWeeklyChartList',             # The method to be used for the process, and the format
    'tag'  : "rock",              # required     
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################
###############################################################################
###############################################################################
#__________________API METHODS FOR CHART QUERIES _____________________________#
#__________________That does not require authorization________________________#


#__________________1_ chart.getTopArtists  -> Get the top artists chart
#__________________2_ chart.getTopTags      ->Get the top artists chart
#__________________3_ chart.getTopTracks     ->Get the top tracks chart
###############################################################################
###############################################################################
# Let's work on each one to experiment the output using flask:
###############################################################################

# 1_ Get the top artists chart

@app.route('/chart/chartgetTopArtists', methods=['POST','GET'])

def Data_chartgettopartists():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'chart.getTopArtists',             # The method to be used for the process, and the format
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 2_ Get the top artists chart

@app.route('/chart/chartgetTopTags', methods=['POST','GET'])

def Data_chartgettoptags():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'chart.getTopTags',             # The method to be used for the process, and the format
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 



###############################################################################

# 3_ Get the top tracks chart

@app.route('/chart/chartgetTopTracks', methods=['POST','GET'])

def Data_chartgettoptracks():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'chart.getTopTracks',             # The method to be used for the process, and the format
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 


###############################################################################
###############################################################################
###############################################################################
#__________________API METHODS FOR GEO QUERIES _______________________________#
#__________________That does not require authorization________________________#


#__________________1_ geo.getTopArtists  -> Get the most popular artists on Last.fm by country
#__________________2_ geo.getTopTracks      ->Get the most popular tracks on Last.fm last week by country
###############################################################################
###############################################################################
# Let's work on each one to experiment the output using flask:
###############################################################################

# 1_ Get the most popular artists on Last.fm by country

@app.route('/geo/getTopArtists', methods=['POST','GET'])

def Data_geogettopartists():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'geo.getTopArtists', 
    'country' : 'Spain',           # The method to be used for the process, and the format
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################

# 2_ Get the most popular tracks on Last.fm last week by country

@app.route('/geo/getTopTracks', methods=['POST','GET'])

def Data_geogettoptracks():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'geo.getTopTracks',             # The method to be used for the process, and the format
    'api_key' : API_KEY,
    'country' : 'Spain', 
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 


###############################################################################
###############################################################################
###############################################################################
###############################################################################
#__________________API METHODS FOR LIBRARY QUERIES ___________________________#
#__________________That does not require authorization________________________#


#__________________1_ library.getArtists  -> A paginated list of all the artists in a user's library, with play counts and tag counts.
###############################################################################
###############################################################################
# Let's work on each one to experiment the output using flask:
###############################################################################


# 1_ Get A paginated list of all the artists in a user's library, with play counts and tag counts.

@app.route('/librarygetArtists', methods=['POST','GET'])

def Data_librarygetartists():                                        
    API_KEY = '7cb9f9c0c97c61c2c14e43cb6c0db5d4'
    USER_AGENT = 'AAMoussaA'

    headers = {
    'user-agent' : 'USER_AGENT'             # Here I created a dictionary for the headers parameter
    }

    payload = {                             # Here I created a dictionary for the params parameter 
                                            # Specifying the key to Identify myself to the API,
    'method'  : 'library.getArtists', 
    'user' : 'AAMoussaAA',           # The method to be used for the process, and the format
    'api_key' : API_KEY,
    'format'  : 'json'                       # the data returned should be in.
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params= payload)
    Data = r.json()
    return Data 

###############################################################################
###############################################################################
if __name__ =='__main__':
    app.run(debug=True, port=8000)