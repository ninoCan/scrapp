from .requests_soup import *
from .mysql_functions import *
from bs4 import BeautifulSoup

def omdb_search(title,year):
    #reads the key for the api and store it in the variable key
    with open("api.key",'r') as f:
        key = f.read().replace('\n','')
    
    #builds the url to be passed to the scraper
    url = 'http://www.omdbapi.com/?apikey=' + key + '&t=' + title.replace(" ","+").replace("'",'+') + '&r=xml'
    request = simple_get(url) #sends a request to the url and returns a tuple (<format>,<raw_content>)
    
    content = BeautifulSoup(request[1],"lxml-"+request[0]) #parse the content
    
    return content