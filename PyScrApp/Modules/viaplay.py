from .requests_soup import *
from .mysql_functions import *
from .omdb import *
#from bs4 import BeautifulSoup
import json
import time

movie_base = 'https://content.viaplay.fi/pcdash-fi/leffat/kaikki?blockId=20822ace006b61ea5811662ab365729e&partial=1&sort=alphabetically&pageNumber='
series_base='https://content.viaplay.fi/pcdash-fi/sarjat/kaikki?blockId=0e0111c1a5e0fb362a4aa9115e974409&partial=1&pageNumber='
scrape_data = {
    'type' : 'json',
    'movie_scrape_url' : movie_base,
    'tv_series_scrape_url' : series_base
    }

def viaplay_first_contact(base):
    """ Contact the viaplay to get the number of pages and how many elements are contained in a single page
    """
        raw = simple_get(base + '1')                              #get the raw page
        content = json.loads(raw[1])                              #parse the content as a python-json dict 
        return (content['pageCount'], content['productsPerPage'])#return the numbers of pages and product/page

def viaplay_scraper(cnx, cursor):
    """ Scraper from VIAPLAY movies
    """

    vp_base = scrape_data['movie_scrape_url']

    if not is_service_in_database(cursor, 'viaplay'):
        add_service_to_steamingService(cnx, cursor, 'viaplay', json.dumps(scrape_data))

    page_lim, counter_lim = viaplay_first_contact(vp_base)
    i=1                                                 #counter to loop through the pages
    
    for i in range(1,page_lim):                         #last page contains less than counter_lim movies, it needs to be treated differently
        time.sleep(1.5)

        url = vp_base + str(i) 
        raw = simple_get(url)                           #get the raw page
        content = json.loads(raw[1])                    #parse the content as a python-json dict 
    
        
        for j in range(counter_lim):
            vp_movie = content['_embedded']['viaplay:products'][j]

            pars = (                                     #extract title and year from the viaplay page
                vp_movie['content']['title'],
                vp_movie['content']['production']['year'],
                vp_movie['publicPath'],
                vp_movie['content']['imdb']['id']
            )
            print("Scraped ", pars[0], pars[1], pars[2], " from viaplay")
            
            failed = False
            omdb_data = omdb_search(pars[0],pars[1])      #search for the movie on the Online Movie DataBase
            # omdb_data = omdb_search_by_id(par[0],par[3])  #search for the movie by the imdbID on the OMDb
            # print(par[0], omdb_data)
            if failed:                                          #BUG it doesn't get inside this loop
                    print(pars[0],'failed to be found on OMDB!')
                    add_error(cnx, cursor, par[0],par[1], get_streamingServiceId(cursor,'viaplay'), 'NONE', 'Failed to be found on OMDB!')

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
                
                movie['poster_url'] =  omdb_poster(movie) + '.jpg'

                if len(movie['year']) > 4:
                    print("This should be a tv series!")
                    with open('tv_series_from_viaplay.json','a+') as f:
                        json.dump(movie, f)
                        f.write('\n')
                    add_error(cnx, cursor, movie['title'], movie['year'][:4], get_streamingServiceId(cursor,'viaplay'), json.dumps(omdb_data.movie.attrs), 'This is probably a tv series')
                    print("Added to the viaplay tv series JSON file!")
                    continue

                else:
                    if  not is_title_year_in_db(cursor, movie): 
                                                        #check if (title,year) is not present in the table 'movie'
                        add_new_movie(cnx, cursor, movie)

                    if not is_service_available_for_movie(cursor, get_streamingServiceId(cursor, 'viaplay'), movie):
                            watch_url = 'https://viaplay.fi/leffat/' +  pars[2]
                            add_movie_as_available(cnx, cursor, movie, 'viaplay', watch_url)

                    for genre in movie['genres']:
                        if not is_genre_in_database(cursor, genre):
                            add_new_genre(cnx, cursor, genre)
                        add_genre_to_movie(cnx, cursor, get_movieId(cursor,movie), get_genreId(cursor, genre))

                    if not is_reviewer_in_database(cursor, 'imdb'):
                        add_new_reviewer(cnx, cursor, 'imdb')
                    add_score_to_movie(cnx, cursor, movie['imdb_rating'], get_movieId(cursor, movie), get_reviewerId(cursor, 'imdb'))
                        
                    if not is_reviewer_in_database(cursor, 'metacritic'):
                        add_new_reviewer(cnx, cursor, 'metacritic')
                    add_score_to_movie(cnx, cursor, movie['metacritic_rating'], get_movieId(cursor, movie), get_reviewerId(cursor, 'metacritic'))
    
    # implementing last page scraping
    time.sleep(1.5)

    url = vp_base + str(page_lim)
    raw = simple_get(url)                           #get the raw page
    content = json.loads(raw[1])                    #parse the content as a python-json dict 

    
    for j in range(page_lim % counter_lim -1):
        vp_movie = content['_embedded']['viaplay:products'][j]

        par = (                                     #extract title and year from the viaplay page
            vp_movie['content']['title'],
            vp_movie['content']['production']['year'],
            vp_movie['publicPath'],
            vp_movie['content']['imdb']['id']
        )
        print("Scraped ", par[0], par[1], par[2], " from viaplay")
        
        failed = False
        omdb_data = omdb_search(par[0],par[1])      #search for the movie on the Online Movie DataBase
        # omdb_data = omdb_search_by_id(par[0],par[3])
        # print(par[0], omdb_data)
        if failed:                                          #BUG it doesn't get inside this loop
                print(par[0],'failed to be found on OMDB!')
                add_error(cnx, cursor, par[0],par[1], get_streamingServiceId(cursor,'viaplay'), 'NONE', 'Failed to be found on OMDB!')

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

            movie['poster_url'] =  omdb_poster(movie) + '.jpg'

            if len(movie['year']) > 4:
                print("This should be a tv series!")
                with open('tv_series_from_viaplay.json','a+') as f:
                    json.dump(movie, f)
                    f.write('\n')
                add_error(cnx, cursor, movie['title'], movie['year'][:4], get_streamingServiceId(cursor,'viaplay'), json.dumps(omdb_data.movie.attrs), 'This is probably a tv series')
                print("Added to the viaplay tv series JSON file!")
                continue

            else:
                if  not is_title_year_in_db(cursor, movie): 
                                                    #check if (title,year) is not present in the table 'movie'
                    add_new_movie(cnx, cursor, movie)

                if not is_service_available_for_movie(cursor, get_streamingServiceId(cursor, 'viaplay'), movie):
                        watch_url = 'https://viaplay.fi/leffat/' +  par[2]
                        add_movie_as_available(cnx, cursor, movie, 'viaplay', watch_url)

                for genre in movie['genres']:
                    if not is_genre_in_database(cursor, genre):
                        add_new_genre(cnx, cursor, genre)
                    add_genre_to_movie(cnx, cursor, get_movieId(cursor,movie), get_genreId(cursor, genre))

                if not is_reviewer_in_database(cursor, 'imdb'):
                    add_new_reviewer(cnx, cursor, 'imdb')
                add_score_to_movie(cnx, cursor, movie['imdb_rating'], get_movieId(cursor, movie), get_reviewerId(cursor, 'imdb'))
                    
                if not is_reviewer_in_database(cursor, 'metacritic'):
                    add_new_reviewer(cnx, cursor, 'metacritic')
                add_score_to_movie(cnx, cursor, movie['metacritic_rating'], get_movieId(cursor, movie), get_reviewerId(cursor, 'metacritic'))
    return

## ##################################################### ##
##                  tv series                            ##
## ##################################################### ##
    
def viaplay_series_scraper(cnx, cursor):
    """ Scraper from VIAPLAY tv series
    """

    vp_base = scrape_data['tv_series_scrape_url']

    if not is_service_in_database(cursor, 'viaplay'):
        add_service_to_steamingService(cnx, cursor, 'viaplay', json.dumps(scrape_data))

    page_lim, counter_lim = viaplay_first_contact(vp_base)
    i=1                                                 #counter to loop through the pages
    
    for i in range(1,page_lim):                         #last page contains less than counter_lim movies, it needs to be treated differently
        time.sleep(1.5)

        url = vp_base + str(i) 
        raw = simple_get(url)                           #get the raw page
        content = json.loads(raw[1])                    #parse the content as a python-json dict 
    
        
        for j in range(counter_lim):
            vp_series = content['_embedded']['viaplay:products'][j]
            
            pars = (
                vp_series['content']['series']['title'],
                vp_series['content']['production']['year'],
                vp_series['publicPath'],
                vp_series['content']['series']['seasons']
            )
            print("Scraped ", pars[0], pars[1], " from viaplay")

            failed = False
            omdb_data = omdb_search(pars[0],pars[1])      #search for the movie on the Online Movie DataBase
            # print(par[0], omdb_data)
            if failed:                                          #BUG it doesn't get inside this loop
                print(pars[0],'failed to be found on OMDB!')
                add_error(cnx, cursor, pars[0],pars[1], get_streamingServiceId(cursor,'viaplay'), 'NONE', 'Failed to be found on OMDB!')

            if omdb_data:
                series = {
                    'title' : omdb_data.movie['title'],
                    'year' : pars[1],
                    'description' : omdb_data.movie['plot'],
                    'poster_url' : 'nocover.png', #omdb_data.movie['poster'],
                    'imdb_id' : omdb_data.movie['imdbID'],
                    # 'imdb_rating' : omdb_data.movie['imdbRating'],
                    'genres' : omdb_data.movie['genre'].split(', '),
                    'imdb_rating' : omdb_data.movie['imdbRating'],
                    'seasons' : pars[4]
                }
            
                if  not is_series_in_db(cursor, series): 
                                                        #check if (title,year) is not present in the table 'movie'
                    add_new_series(cnx, cursor, series)

                if not is_service_available_for_series(cursor, get_streamingServiceId(cursor, 'viaplay'), series):
                        watch_url = 'https://viaplay.fi/sarjat/' +  pars[2]
                        add_series_as_available(cnx, cursor, series, 'viaplay', watch_url)

                for genre in series['genres']:
                    if not is_genre_in_database(cursor, genre):
                        add_new_genre(cnx, cursor, genre)
                    add_genre_to_series(cnx, cursor, get_seriesId(cursor,series), get_genreId(cursor, genre))

                if not is_reviewer_in_database(cursor, 'imdb'):
                    add_new_reviewer(cnx, cursor, 'imdb')
                add_score_to_series(cnx, cursor, series['imdb_rating'], get_seriesId(cursor, series), get_reviewerId(cursor, 'imdb'))

    # implementing last page scraping

    time.sleep(1.5)


    url = vp_base + page_lim 
    raw = simple_get(url)                           #get the raw page
    content = json.loads(raw[1])                    #parse the content as a python-json dict                 
    
    for j in range(counter_lim):
        vp_series = content['_embedded']['viaplay:products'][j]
        
        pars = (
            vp_series['content']['series']['title'],
            vp_series['content']['production']['year'],
            vp_series['publicPath'],
            vp_series['content']['series']['seasons']
        )
        print("Scraped ", pars[0], pars[1], " from viaplay")

        failed = False
        omdb_data = omdb_search(par[0],par[1])      #search for the movie on the Online Movie DataBase
        # print(par[0], omdb_data)
        if failed:                                          #BUG it doesn't get inside this loop
            print(par[0],'failed to be found on OMDB!')
            add_error(cnx, cursor, par[0],par[1], get_streamingServiceId(cursor,'viaplay'), 'NONE', 'Failed to be found on OMDB!')

        if omdb_data:
            series ={
                'title' : omdb_data.movie['title'],
                'year' : pars[1],
                'description' : omdb_data.movie['plot'],
                'poster_url' : 'nocover.png', #omdb_data.movie['poster'],
                'imdb_id' : omdb_data.movie['imdbID'],
                # 'imdb_rating' : omdb_data.movie['imdbRating'],
                'genres' : omdb_data.movie['genre'].split(', '),
                'imdb_rating' : omdb_data.movie['imdbRating'],
                'seasons' : pars[4]
            }
        
        if  not is_series_in_db(cursor, series): 
                                                #check if (title,year) is not present in the table 'movie'
            add_new_series(cnx, cursor, series)

        if not is_service_available_for_series(cursor, get_streamingServiceId(cursor, 'viaplay'), series):
                watch_url = 'https://viaplay.fi/sarjat/' +  par[2]
                add_series_as_available(cnx, cursor, series, 'viaplay', watch_url)

        for genre in series['genres']:
            if not is_genre_in_database(cursor, genre):
                add_new_genre(cnx, cursor, genre)
            add_genre_to_series(cnx, cursor, get_seriesId(cursor,series), get_genreId(cursor, genre))

        if not is_reviewer_in_database(cursor, 'imdb'):
            add_new_reviewer(cnx, cursor, 'imdb')
        add_score_to_series(cnx, cursor, series['imdb_rating'], get_seriesId(cursor, series), get_reviewerId(cursor, 'imdb'))
    
    return

