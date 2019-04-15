from flask import Flask,Response,request
import json
import omdb_access
import os

app = Flask(__name__)

@app.route("/")
def hello():
    """Returns simple  Hello World message"""
    return "Hello World!"

def getSpecificRating(ratings):
    """Returns rating dictionary with value (if available)"""
    rating = {}
    for resp in ratings:
        #print('resp',resp)
        for key in resp.keys():
            val = resp[key]
            #print("Key", key, 'points to', val)
            if (key == 'Source' and val == 'Rotten Tomatoes'):
                nextVal = resp['Value']
                rating['val']=nextVal
    return rating

@app.route("/movie")
def getMovie(): 
    # http://www.omdbapi.com/?i=tt3896198&apikey=ca5e163c
    """ 
    Summary line. 
  
    Extended description of getMovie. 
  
    Parameters: 
      request object value in query arguments

    Returns: 
    dict: omdbapi Response value with {'rating':ratingValue} 
    """    

    '''
    movieId (int): movieId if known 
    movieTitle (String): movieTitle if known 
    apikey (String): apikey if available from environment value 
    '''

    movieId = request.args.get("movieId")
    print("movieId ", movieId)
    
    movieTitle = request.args.get("movieTitle")
    print("movieTitle ", movieTitle)    

    apikey = os.environ["APIKEY"]
    # To Do:
    # if the APIKEY is not set then return
    # {'error':'No APIKEY available'}
    
    responseObj = omdb_access.getMovieFromOmdb(movieId,movieTitle,apikey)
    print("responseObj ",responseObj)
    ratings = responseObj['Ratings']
    print("ratings ", ratings)
    specificRate = getSpecificRating(ratings)
    print("specificRate ", specificRate)  

    if 'val' in specificRate:
        resp = {'rating':specificRate['val']}
    else: 
        resp = {'rating':'-1%'}

    
    return Response(json.dumps(resp), mimetype='application/json')

if __name__ == '__main__':
    #port = os.environ["PORT"]
    port = os.environ.get('PORT', 8000)
    print('port = ',port)           
    app.run(debug=False,host='0.0.0.0', port=port)