from .requests_soup import *
from .mysql_functions import *
from .omdb import *
from bs4 import BeautifulSoup


def is_hbo_service_available(cursor, movie):
    query = ('SELECT movie_streaming_service_selection.id AS "rows" '
             'FROM movie_streaming_service_selection ' 
             'LEFT JOIN movie '
             'ON movie.id = movie_streaming_service_selection.movie_id '
             'WHERE movie.name = %s AND movie.year = %s')
    pars = (movie['title'], movie['year'])
    cursor.execute(query, (pars))
    cursor.fetchall()
    if cursor.rowcount >= 1:
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
            print("Scraped ", par[0], par[1]," from hbo")
            omdb_data = omdb_search(par[0],par[1])      #search for the movie on the Online Movie DataBase
            # print(par[0], omdb_data)
            if omdb_data:
                movie = {                                   #scrape data from omdb to suit our purposes
                    'title' : omdb_data.movie['title'],
                    'year' : omdb_data.movie['year'],
                    'description' : omdb_data.movie['plot'],
                    'poster_url' : 'foobar', #omdb_data.movie['poster'],
                    'imdb_id' : omdb_data.movie['imdbID'],
                    # 'imdb_rating' : omdb_data.movie['imdbRating'],
                    'genres' : omdb_data.movie['genre'].split(', ')
                }
                if  not is_title_year_in_db(cursor, movie): 
                                                        #check if (title,year) is not present in the table 'movie'
                    add_new_movie(cnx, cursor, movie)
                
                if not is_hbo_service_available(cursor, movie):
                    watch_url = 'https://fi.hbonordic.com/movies/' + movie['title'].replace(" ","+") + '/' + par[2]
                    add_movie_as_available(cnx, cursor, movie, 'hbo', watch_url)

                for genre in movie['genres']:
                    if not is_genre_in_database(cursor, genre):
                        # print("I got here")
                        add_new_genre(cnx, cursor, genre)
                    add_genre_to_movie(cnx, cursor, get_movieId(cursor,movie), get_genreId(cursor, genre))

        if content.select('errorCode'):
            flag = False        
    return
