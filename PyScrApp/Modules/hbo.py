from .requests_soup import *
from .mysql_functions import *
from .omdb import *
from bs4 import BeautifulSoup
import json

# def is_hbo_service_available(cursor, movie):
#     query = ('SELECT movie_streaming_service_selection.id AS "rows" '
#              'FROM movie_streaming_service_selection ' 
#              'LEFT JOIN movie '
#              'ON movie.id = movie_streaming_service_selection.movie_id '
#              'WHERE movie.name = %s AND movie.year = %s')
#     pars = (movie['title'], movie['year'])
#     cursor.execute(query, (pars))
#     cursor.fetchall()
#     if cursor.rowcount >= 1:
#         return True
#     else:
#         return False 
        
# def check_if_is_tv_series(movie):
#     """
#     HBO lists some tv series amongst the movies. Luckily, this can be checked against the omdb when the year has a - sign.
#     """
    # if len(movie['year']) > 4 and  movie['year'][4] == '-':
    #     print("This should be a tv series!")
    #     with open('tv_series_from_hbo.json','a+') as f:
    #         json.dump(movie, f)
    #     print("Added to the JSON file!")
    #     continue
#     else:
#         return 


def hbo_scraper(cnx,cursor):
    """
    Scraper from HBO NORDIC movies
    """

    hbo_base = 'https://api-hbon.hbo.clearleap.com/cloffice/client/web/browse/ea73aabd-24a3-473e-8f3a-39aeb7f0f93e?max=20&language=fi_hbon&offset='                    # base page 
    # add_hbo_to_steamingService(cnx, cursor, hbo_base)
    if not is_service_in_database(cursor, 'HBO'):
        add_service_to_steamingService(cnx, cursor, 'HBO', hbo_base, 'xml')


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
            failed = False
            omdb_data = omdb_search(par[0],par[1])      #search for the movie on the Online Movie DataBase
            # print(par[0], omdb_data)
            if failed:                                          #BUG it doesn't get inside this loop
                    print(par[0],'failed to be found on OMDB!')
                    add_error(cnx, cursor, par[0], par[1], get_streamingServiceId(cursor, 'HBO'), 'NONE', 'Failed to be found on OMDB!')
                   
            if omdb_data:
                movie = {                                   #scrape data from omdb to suit our purposes
                    'title' : omdb_data.movie['title'],
                    'year' : omdb_data.movie['year'],
                    'description' : omdb_data.movie['plot'],
                    'poster_url' : 'nocover.png', #omdb_data.movie['poster'],
                    'imdb_id' : omdb_data.movie['imdbID'],
                    # 'imdb_rating' : omdb_data.movie['imdbRating'],
                    'genres' : omdb_data.movie['genre'].split(', '),
                    'imdb_rating' : omdb_data.movie['imdbRating'],
                    'metacritic_rating' : omdb_data.movie['metascore']
                }
                

                if len(movie['year']) > 4:
                    print("This should be a tv series!")
                    with open('tv_series_from_hbo.json','a+') as f:
                        json.dump(movie, f)
                        f.write('\n')
                    add_error(cnx, cursor, movie['title'], movie['year'][:4], get_streamingServiceId(cursor,'HBO'), json.dumps(omdb_data.movie.attrs), 'This is probably a tv series')
                    print("Added to the HBO tv series JSON file!")
                    continue
                else:
                    if  not is_title_year_in_db(cursor, movie): 
                                                        #check if (title,year) is not present in the table 'movie'
                        add_new_movie(cnx, cursor, movie)
                
                        # if not is_hbo_service_available(cursor, movie):
                        if not is_service_available_for_movie(cursor, get_streamingServiceId('HBO'), movie):
                            watch_url = 'https://fi.hbonordic.com/movies/' + movie['title'].replace(" ","+") + '/' + par[2]
                            add_movie_as_available(cnx, cursor, movie, 'hbo', watch_url)

                        for genre in movie['genres']:
                            if not is_genre_in_database(cursor, genre):
                                # print("I got here")
                                add_new_genre(cnx, cursor, genre)
                            add_genre_to_movie(cnx, cursor, get_movieId(cursor,movie), get_genreId(cursor, genre))

                        if not is_reviewer_in_database(cursor, 'imdb'):
                            add_new_reviewer(cnx, cursor, 'imdb')
                        add_score_to_movie(cnx, cursor, movie['imdb_rating'], get_movieId(cursor, movie), get_reviewerId(cursor, 'imdb'))
                        
                        if not is_reviewer_in_database(cursor, 'metacritic'):
                            add_new_reviewer(cnx, cursor, 'metacritic')
                        add_score_to_movie(cnx, cursor, movie['metacritic_rating'], get_movieId(cursor, movie), get_reviewerId(cursor, 'metacritic'))

        if content.select('errorCode'):
            flag = False        
    return

## ##################################################### ##
##                  tv series                            ##
## ##################################################### ##


# def hbo_series_scraper(cnx, cursor):

#     hbo_base = 'https://api-hbon.hbo.clearleap.com/cloffice/client/web/browse/f5dde064-495d-41dc-8cd7-cbb76baaf8d0?max=20&language=fi_hbon&offset='
    
#      i=0                                                 #counter to loop through the page
#     flag = True                                         #flag to control the page scraper loop

#     while flag:
#         url = hbo_base + str(i) 
#         raw = simple_get(url)                           #get the raw page
#         content = BeautifulSoup(raw[1], "lxml-"+raw[0]) #parse the content with BS        
#         i += 20                                         #moves the counter to next page

#         for elem in content.select('item'):             #cycles the <item> elements in the page
                   
#             par = (                                     #extract title and year from an item of the page
#                 elem.select('title').pop().text,            
#                 elem.find('media:credit', role = "year").text, 
#                 elem.find('guid').text
#             )
#             print("Scraped tv series title: ", par[0], par[1]," from hbo")
#             failed = False