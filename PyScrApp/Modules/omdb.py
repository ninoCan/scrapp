from .requests_soup import *
from .mysql_functions import *
from bs4 import BeautifulSoup
import time 
from hashlib import sha1

def omdb_search(title,year):
    """ Search the Online Movie database from a title and year and return the content of the search if found, or boolean value False otherwise
    """
    #reads the key for the api and store it in the variable key
    with open("api.key",'r') as f:
        key = f.read().replace('\n','')
    
    #builds the url to be passed to the scraper
    url = 'http://www.omdbapi.com/?apikey=' + key + '&t=' + title.replace(" ","+").replace("'",'+') +'&y='+ str(year) + '&r=xml'
    request = simple_get(url) #sends a request to the url and returns a tuple (<format>,<raw_content>)
    try:
        content = BeautifulSoup(request[1],"lxml-"+request[0]) #parse the content

        ################ move this here 
        if content.root['response'] != 'False':
            print("Found", title, "on OMDb!")
            return content
        else:
            if len(shrink_title(title).split()) > 1:
                omdb_search(shrink_title(title), year)
            else:
                print("NEED TO ADD ERROR TO THE TABLE for ", title, year)
                global failed
                failed = True
                return False
        ################ end of modification

    except Exception as exc:
        print(exc ,'occurred!')
        time.sleep(5)
        print('Retrying to get data from omdb')
        omdb_search(title,year)
        
    # if content.root['response'] != 'False':
    #     return content
    # else:
    #     if len(shrink_title(title).split()) > 1:
    #         omdb_search(shrink_title(title), year)
    #     else:
    #         print("NEED TO ADD ERROR TO THE TABLE for ", title, year)
    #         global failed
    #         failed = True
    #         return False


def omdb_search_by_id(title,imdb_id):
    """ Search the Online Movie database from a imbd ID  and return the content of the search if found, or boolean value False otherwise
    """
    #reads the key for the api and store it in the variable key
    with open("api.key",'r') as f:
        key = f.read().replace('\n','')
    
    #builds the url to be passed to the scraper
    url = 'http://www.omdbapi.com/?apikey=' + key + '&i=' + imdb_id + '&r=xml'
    request = simple_get(url) #sends a request to the url and returns a tuple (<format>,<raw_content>)
    try:
        content = BeautifulSoup(request[1],"lxml-"+request[0]) #parse the content

        ################ move this here 
        if content.root['response'] != 'False':
            print("Found", title, "on OMDb!")
            return content
        else:
            print("NEED TO ADD ERROR TO THE TABLE for ", title)
            global failed
            failed = True
            return False
        ################ end of modification

    except Exception as exc:
        print(exc ,'occurred!')
        time.sleep(5)
        print('Retrying to get data from omdb')
        omdb_search_by_id(title,imdb_id)


def shrink_title(title):
    """ Shrink a string "title" by dropping the final word
    """
    with open("api.key",'r') as f:
        key = f.read().replace('\n','')

    last_word = title.split().pop()
    new_title = title.rstrip(last_word).rstrip().rstrip("'")

    return new_title


def omdb_poster(movie):
    """ Save the poster image to folder ./Posters
    """
    with open('api.key','r') as f:
        key = f.read().replace('\n','')

    url = 'http://img.omdbapi.com/?apikey=' + key + '&i=' + movie['imdb_id'] + '&h=300'
    with get(url, stream= True) as resp:
        if resp.status_code == 200:
            name = movie['title'] + movie['year']
            hasher = sha1(name.encode('utf-8'))

            path_to_poster='./Posters/'+hasher.hexdigest()+'.jpg'

            with open(path_to_poster,'wb') as f:
                f.write(resp.content)
  
            return hasher.hexdigest()
        else: 
            return "nocover"

def omdb_search_without_year(title):
    """ Search the Online Movie database from just the title and return the content of the search if found, or boolean value False otherwise
    """
    #reads the key for the api and store it in the variable key
    with open("api.key",'r') as f:
        key = f.read().replace('\n','')
    
    #builds the url to be passed to the scraper
    url = 'http://www.omdbapi.com/?apikey=' + key + '&t=' + title.replace(" ","+").replace("'",'+') + '&r=xml'
    request = simple_get(url) #sends a request to the url and returns a tuple (<format>,<raw_content>)
    try:
        content = BeautifulSoup(request[1],"lxml-"+request[0]) #parse the content

        ################ move this here 
        if content.root['response'] != 'False':
            print("Found", title, "on OMDb!")
            return content
        else:
            if len(shrink_title(title).split()) > 1:
                omdb_search_without_year(shrink_title(title))
            else:
                print("NEED TO ADD ERROR TO THE TABLE for ", title, year)
                nonlocal failed
                failed = True
                return False
        ################ end of modification

    except Exception as exc:
        print(exc ,'occurred!')
        time.sleep(5)
        print('Retrying to get data from omdb')
        omdb_search(title,year)