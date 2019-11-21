import mysql.connector
from bs4 import BeautifulSoup

def omdb_search(title,year):
    with open("api.key",'r') as f:
        key = f.readline()
    url = 'http://www.omdbapi.com/?apikey=[' + key + ']&t=' + title.replace(" ","+") + '&r=xml'
    request = simple_get(url)
    content = BeautifulSoup(request,"lxml-xml")
    print(content)

    return