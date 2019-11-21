#loading package dependencies
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import mysql.connector

#function definitions

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_html_response(resp):
                return ('html', resp.content)
            elif is_good_xml_response(resp):
                return ('xml', resp.content)
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_html_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def is_good_xml_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('xml') > -1)

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

##
def add_title_year_to_db(cnx, cursor, par):
    """ 
    Add the title and year of a movie to mysql database
    """
    add_movie=("INSERT INTO movie"
               "(name, year, description)"
               "VALUES (%s, %s, ' ')")

    cursor.execute(add_movie,(par))
    print(par[0] + " ("+par[1]+") inserted")
    #save insertion to database
    cnx.commit()
    return 

def add_to_db(cnx, cursor, par):
    """ 
    Add the title of a movie to mysql database
    """
    add_movie=("INSERT INTO movie"
               "(name, description)"
               "VALUES (%s, ' ')")

    cursor.execute(add_movie,(par))
    print(par[0] + " inserted")
    #save insertion to database
    cnx.commit()
    return 

def is_title_year_in_db(cnx, cursor, par):
    query = "SELECT movie.name FROM movie WHERE movie.name = %s AND movie.year = %s"
    cursor.execute(query,(par))
    cursor.fetchall()
    if cursor.rowcount > 0 :
        return True
    else:
        return False

def is_hbo_service_available(cnx, cursor, par):
    query = ('SELECT COUNT(*) AS "rows"'
             'FROM movie_streaming_service_selection LEFT JOIN'
             'movie ON movie.id = movie_streaming_service_selection.movie_id'
             'WHERE movie.name = %s AND movie.year = %s')
    cursor.execute(query,(par))
    cursor.fetchall()
    if cursor.rows >= 1:
        return False 
    else:
        return True 
        

def hbo_scraper(cnx,cursor):
    """
    Scraper from hbo_nordic
    """
    #base page 
    hbo_base = 'https://api-hbon.hbo.clearleap.com/cloffice/client/web/browse/ea73aabd-24a3-473e-8f3a-39aeb7f0f93e?max=20&language=fi_hbon&offset='
    
    i=0 #counter to loop through the page
    flag = True #flag to control the page scraper loop

    while flag:
        url = hbo_base + str(i)
        raw = simple_get(url) #get the raw page
        content = BeautifulSoup(raw[1], "lxml-xml") #parse the content with BS
        i += 20        #moves the counter to next page

        for elem in content.select('item'): #cycles the <item> elements in the page
            #extract title and year from an item of the page
            par = (elem.select('title').pop().text, elem.find('media:credit', role = "year").text)

            if  is_title_year_in_db(cnx, cursor, par): #check if (title,year) is present in the mysql table 'movie'
                if is_hbo_service_available:
                    continue # later add omdb_search
                else:

            else:
                add_title_year_to_db(cnx, cursor, par)
                
        if content.select('errorCode'):
            flag = False        
    return

def omdb_search(title,year):
    with open("api.key",'r') as f:
        key = f.readline()
    url = 'http://www.omdbapi.com/?apikey=[' + key + ']&t=' + title.replace(" ","+") + '&r=xml'
    request = simple_get(url)
    content = BeautifulSoup(request,"lxml-xml")
    print(content)

    return


def viaplay_scraper():
    vp_base='https://content.viaplay.fi/pcdash-fi/leffat/kaikki?blockId=20822ace006b61ea5811662ab365729e&partial=1&pageNumber=1&sort=recently_added'

    return

    
def main():
    """
    This is going to connect to mysql database and scrape data from the various services
    """
    print("connecting to the mysql local container")
    cnx = mysql.connector.connect(user='admin', password='password', host='172.17.0.2', database='vondd')
    print("initializing the cursor to the database")
    cursor =  cnx.cursor(buffered=True)

    print('Scraping data from the internet...')
    hbo_scraper(cnx,cursor)
    print('Scraping complete!')



    print("closing database cursor")
    cursor.close()
    print("closing connection to database")
    cnx.close()
    return

if __name__ == "__main__":
    main()