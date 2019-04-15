from flask import Flask
import requests

def getMovieFromOmdb(movieId,movieTitle,apikey):  
    """ 
    Summary line. 
  
    Extended description of getMovieFromOmdb. 
  
    Parameters: 
    movieId (int): movieId if known 
    movieTitle (String): movieTitle if known 
    apikey (String): apikey if known   

    Returns: 
    dict: omdbapi Response value for the given movieId or movieTitle 
  
    """    
    headers = {'Accept':'application/json','Content-type': 'application/json'}
    url = 'http://www.omdbapi.com/'

    params = {
        'apikey': apikey
    }
    if (movieId != None):
        params['i'] = movieId
    if (movieTitle != None):
        params['t'] = movieTitle  
          
    #fullUrl = f"url?i={movieId}&apikey={apikey}"
    response = requests.get(url, params=params, headers=headers)
    print("response", response)
    print("response", response.json())
    return response.json()
    #{"some":"something"}
