from .requests_soup import *
from .mysql_functions import *
from bs4 import BeautifulSoup
import mysql.connector


def is_hbo_service_available(cnx, cursor, par):
    query = ('SELECT COUNT(*) AS "rows"'
             'FROM movie_streaming_service_selection LEFT JOIN'
             'movie ON movie.id = movie_streaming_service_selection.movie_id'
             'WHERE movie.name = %s AND movie.year = %s')
    cursor.execute(query,(par))
    cursor.fetchall()
    if cursor.rows >= 1:
        return True
    else:
        return False 
        

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
                    #print('need to add omdb_search')
                    continue # later add omdb_search
                else:
                    print("need to add url")
            else:
                add_title_year_to_db(cnx, cursor, par)
                
        if content.select('errorCode'):
            flag = False        
    return
