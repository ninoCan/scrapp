from .requests_soup import *
from .mysql_functions import *
from .omdb import *
from bs4 import BeautifulSoup


def is_hbo_service_available(cnx, cursor, par):
    query = ('SELECT movie_streaming_service_selection.id AS "rows"'
             'FROM movie_streaming_service_selection' 
             'LEFT JOIN movie'
             'ON movie.id = movie_streaming_service_selection.movie_id'
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
   
    hbo_base = 'https://api-hbon.hbo.clearleap.com/cloffice/client/web/browse/ea73aabd-24a3-473e-8f3a-39aeb7f0f93e?max=20&language=fi_hbon&offset='                    #base page 
    # add_hbo_to_steamingService(cnx, cursor, hbo_base)
    
    i=0                                                 #counter to loop through the page
    flag = True                                         #flag to control the page scraper loop

    while flag:
        url = hbo_base + str(i) 
        raw = simple_get(url)                           #get the raw page
        content = BeautifulSoup(raw[1], "lxml-"+raw[0]) #parse the content with BS        
        i += 20                                         #moves the counter to next page

        for elem in content.select('item'):             #cycles the <item> elements in the page
                   
            par = (                                     #extract title and year from an item of the page
                elem.select('title').pop().text,            
                elem.find('media:credit', role = "year").text, 
                elem.find('guid').text
            )
            omdb_data = omdb_search(par[0],par[1])      #search for the movie on the Online Movie DataBase
            movie = {                                   #scrape data from omdb to suit our purposes
                'title' = omdb_data.movie['title'],
                'year' = omdb_data.movie['year'],
                'description' = omdb_data.movie['plot'],
                'poster_url' = omdb_data.movie['poster'],
                'imdb_url' = 'https://www.imdb.com/title/' + omdb_data.movie['imbdID']
                'imdb_rating' = omdb_data.movie['imdbRating'],
            }
            if  not is_title_year_in_db(cnx, cursor, par): #check if (title,year) is not present in the table 'movie'
            #    add_title_year_to_db(cnx, cursor, )
                
            # if is_hbo_service_available:
            #         #print('need to add omdb_search')
            #         continue
            #     else:
            #         service_id = get_streamingServiceId(cursor, name) 
            #         movie_id = get_movieId(cursor, par)
            #         watch_url = 'https://fi.hbonordic.com/movies/' + par[0].replace(" ","+") + '/' + par[2] #substitute par[0] with the movie with the title from omdb
            #         add_movie_as_available(cnx, cursor, movie_id, service_id, watch_url)
                    

        if content.select('errorCode'):
            flag = False        
    return
