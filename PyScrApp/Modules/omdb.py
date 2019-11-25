from .requests_soup import *
from .mysql_functions import *
from bs4 import BeautifulSoup
import time, sys 

def omdb_search(title,year):
    #reads the key for the api and store it in the variable key
    with open("api.key",'r') as f:
        key = f.read().replace('\n','')
    
    #builds the url to be passed to the scraper
    url = 'http://www.omdbapi.com/?apikey=' + key + '&t=' + title.replace(" ","+").replace("'",'+') + '&r=xml'
    request = simple_get(url) #sends a request to the url and returns a tuple (<format>,<raw_content>)
    try:
        content = BeautifulSoup(request[1],"lxml-"+request[0]) #parse the content
    except:
        print(sys.exc_info[0],'occurred!')
        time.sleep(5)
        print('Retrying to get data from omdb')
        omdb_search(title,year)

    if content.root['response'] != 'False':
        return content
    else:
        if len(shrink_title(title).split()) > 1:
            omdb_search(shrink_title(title), year)
        else:
            # print("NEED TO ADD ERROR TO THE TABLE for ", title)
            global failed
            failed = True
            return False

def shrink_title(title):
    with open("api.key",'r') as f:
        key = f.read().replace('\n','')

    last_word = title.split().pop()
    new_title = title.rstrip(last_word).rstrip().rstrip("'")

    return new_title