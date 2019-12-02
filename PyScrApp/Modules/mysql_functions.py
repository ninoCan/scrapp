import mysql.connector


def connect_to_database(file):
    """ Open a database connection reading the credential from a file
    """
    with open(file,'r') as f:
        cred = f.read().splitlines()

    print("connecting to the mysql local container")
    cnx = mysql.connector.connect(user=cred[0], password=cred[1], host=cred[2], database=cred[3])
    print("initializing the cursor to the database")
    cursor =  cnx.cursor(buffered=True)
    
    return cnx, cursor

def disconnect_database(cnx, cursor):
    """ Close connection with the database
    """
    print("closing database cursor")
    cursor.close()
    print("closing connection to database")
    cnx.close()
    return

# def add_to_db(cnx, cursor, par):
#     """ Add the title of a movie to mysql database
#     """
#     add_movie=("INSERT INTO movie"
#                "(name, description)"
#                "VALUES (%s, ' ')")

#     cursor.execute(add_movie,(par))
#     print(par[0] + " inserted")
#     #save insertion to database
#     cnx.commit()
#     return 

def is_title_year_in_db(cursor, movie):
    """ Check if there is already a title with a year in the database
    """
    query = "SELECT movie.name FROM movie WHERE movie.name = %s AND movie.year = %s"
    pars = (movie['title'], movie['year'])
    cursor.execute(query,(pars))
    cursor.fetchall()
    if cursor.rowcount > 0 :
        return True
    else:
        return False

def get_streamingServiceId(cursor, service):
    """ Get streaming service id with name 
    """
    query = ('SELECT streaming_service.id AS "id" '
              'FROM streaming_service '
              'WHERE streaming_service.name = %s')
    par = (service, )
    cursor.execute(query, (par))
    result = cursor.fetchall()
    if result != None:
        return result.pop()[0]
    else:
        return None

def get_movieId(cursor, movie):
    """ Get movie id with name and year 
    """
    query = ('SELECT movie.id AS "id" '
             'FROM movie '
             'WHERE movie.name = %s AND movie.year = %s')
    pars = (movie['title'], movie['year'])
    
    cursor.execute(query, (pars))
    result = cursor.fetchall()
    if result != None:
        return result.pop()[0]
    else:
        return None

def get_movieServiceIds(cursor, par):
    """ Get movie streaming service id(s) where movie is available to watch with name and year 
    """
    query = ('SELECT movie_streaming_service_selection.streaming_service_id AS "id" '
             'FROM movie_streaming_service_selection '
             'LEFT JOIN movie ' 
             'ON movie.id = movie_streaming_service_selection.movie_id '
             'WHERE movie.name = %s AND movie.year = %s')
    
    result = cursor.execute(query, (par))
    if result.rowcount >= 1:
        return result
    else:
        return None

def is_genre_in_database(cursor, name):
    """ Check if genre already exists in the genre table
    """
    query = ('SELECT genre.name '
             'FROM genre '
             'WHERE genre.name = %s')
    par = (name, )
    cursor.execute(query, (par))
    result = cursor.fetchall()
    # check = len(result) != 0
    # print("Result from genre-check is going to be: ", result, " and the check is going to be: ", check)
    if len(result) != 0:
        return True
    else: 
        return False

def add_movie_as_available(cnx, cursor, movie, service, url):
    """ Add movie to be available on given streaming service 
    """
    add_service = ('INSERT INTO movie_streaming_service_selection '
                   '(movie_id, streaming_service_id, url) '
                   'VALUES (%s, %s, %s)')

    pars = (get_movieId(cursor, movie), get_streamingServiceId(cursor, service), url)
    cursor.execute(add_service, (pars))
    result = cursor.lastrowid
    if result != None:
        cnx.commit()
        print(service + ' streaming available for ' +movie['title'])
        return 
    else:
        return False

def add_new_movie(cnx, cursor, movie):
    """ Insert a new movie 
    """
    add_movie = ('INSERT INTO movie '
            # '(name, description, year, poster_url, imdb_url) '
             '(name, description, year, poster, imdb_id) '
             'VALUES (%s, %s, %s, %s, %s)')
    pars = (movie['title'], movie['description'], movie['year'], movie['poster_url'], movie['imdb_id'])
    result = cursor.execute(add_movie, (pars))
    if result != None:
        print(movie['title'] + ' (' + movie['year'] + ') inserted')
        cnx.commit()
        return 
    else:
        return #print result.id to error_table
    
# def add_title_year_to_db(cnx, cursor, par):
#     """ Add the title and year of a movie to mysql database
#     """
#     add_movie=("INSERT INTO movie "
#                "(name, year, description) "
#                "VALUES (%s, %s, ' ')")
#     cursor.execute(add_movie,(par))
#     print(par[0] + " ("+par[1]+") inserted")
#     #save insertion to database
#     cnx.commit()
#     return 

def add_movieReview(movie_id, reviewer_id, rating):
    """ Insert new review 
    """
    query = ('INSERT INTO movie_review '
             '(movie_id, reviewer_id, rating) '
             'VALUES (%s, %s, %s)')

    params = (movie_id, reviewer_id, rating)
    result = cursor.execute(query, (params))
    if result.rowcount >= 1:
        return True
    else:
        return False

def add_genre_to_movie(cnx, cursor, movie_id, genre_id):
    """ Link movie to genre 
    """
    add = ('INSERT INTO movie_genre '
             '(movie_id, genre_id) '
             'VALUES (%s, %s)')

    pars = (movie_id, genre_id)
    cursor.execute(add, (pars))
    result = cursor.lastrowid
    if result != None:
        print("Movie has new genre")
        cnx.commit()
        return 
    else:
        return False

def add_new_genre(cnx, cursor, name):
    """ Add new genre 
    """
    add = ('INSERT INTO genre '
             '(name) '
             'VALUES (%s)')
    par = (name,)
    cursor.execute(add, (par))
    result = cursor.lastrowid
    if result != None:
        print("Added new genre to table: ", name)
        cnx.commit()
        return 
    else:
        print("genre NOT ADDED")
        return False

def get_genreId(cursor, name):
    """ Get genre id with name
    """
    query = ('SELECT genre.id AS "id" '
             'FROM genre WHERE genre.name = %s')

    params = (name,)
    cursor.execute(query, (params))
    result = cursor.fetchall()
    #print("For ", name, " we get ",result)
    if len(result) != 0:
        return result.pop()[0]
    else:
        return False


def add_error(cnx, cursor, title, year, service_id, omdb_data, string):
    """ Insert error to error table 
    """
    add = ('INSERT INTO scrape_insertion_error '
           '(scrape_title, year, scrape_service_id, omdb_data, information) '
           'VALUES (%s, %s, %s, %s, %s)'
    )
    pars = (title, year, service_id, omdb_data, string)
    
    cursor.execute(add, (pars))
    result = cursor.lastrowid
    if result != None:
        print("Added new error for the title: ", title, year)
        cnx.commit()
        return 
    else:
        print("FAILED to add error")
        return False

def is_service_in_database(cursor, name):
    """ Check if reviewer already exists in the reviewer table
    """
    query = ('SELECT streaming_service.name '
             'FROM streaming_service '
             'WHERE streaming_service.name = %s')
    par = (name, )
    cursor.execute(query, (par))
    result = cursor.fetchall()
    # check = len(result) != 0
    # print("Result from genre-check is going to be: ", result, " and the check is going to be: ", check)
    if len(result) != 0:
        return True
    else: 
        return False

def add_service_to_steamingService(cnx, cursor, service, json):
    """ Insert  a service to the streaming service table
    """
    add = ('INSERT INTO streaming_service '
           '(name, scrape_data) '
           'VALUES (%s,%s)')
    pars = (service, json)
    cursor.execute(add, (pars))
    cnx.commit()
    return 

def is_reviewer_in_database(cursor, name):
    """ Check if reviewer already exists in the reviewer table
    """
    query = ('SELECT reviewer.name '
             'FROM reviewer '
             'WHERE reviewer.name = %s')
    par = (name, )
    cursor.execute(query, (par))
    result = cursor.fetchall()
    # check = len(result) != 0
    # print("Result from genre-check is going to be: ", result, " and the check is going to be: ", check)
    if len(result) != 0:
        return True
    else: 
        return False

def add_new_reviewer(cnx, cursor, name):
    """ Add new reviewer to the reviewer table
    """
    add = ('INSERT INTO reviewer '
             '(name) '
             'VALUES (%s)')
    par = (name,)
    cursor.execute(add, (par))
    result = cursor.lastrowid
    if result != None:
        print("Added new reviewer to table: ", name)
        cnx.commit()
        return 
    else:
        print("reviewer NOT ADDED")
        return False

def get_reviewerId(cursor, name):
    """ Get reviewer id with name
    """
    query = ('SELECT reviewer.id AS "id" '
             'FROM reviewer '  
             'WHERE reviewer.name = %s')

    par = (name,)
    cursor.execute(query, (par))
    result = cursor.fetchall()
    #print("For ", name, " we get ",result)
    if len(result) != 0:
        return result.pop()[0]
    else:
        return False

def add_score_to_movie(cnx, cursor, score, movie_id, reviewer_id):
    """ Link movie to score
    """
    add = ('INSERT INTO movie_review '
             '(rating, movie_id, reviewer_id) '
             'VALUES (%s, %s, %s)')

    pars = (score, movie_id, reviewer_id)
    cursor.execute(add, (pars))
    result = cursor.lastrowid
    if result != None:
        print("Movie has new rating")
        cnx.commit()
        return 
    else:
        return False

def is_service_available_for_movie(cursor, service_id, movie):
    """ Check whether a service is listed for a movie, if not add it to the table
    """
    query = ('SELECT movie_streaming_service_selection.id AS "rows" '
             'FROM movie_streaming_service_selection ' 
             'LEFT JOIN movie '
             'ON movie.id = movie_streaming_service_selection.movie_id '
             'WHERE movie.name = %s AND movie.year = %s AND movie_streaming_service_selection.streaming_service_id = %s')
    pars = (movie['title'], movie['year'], service_id)
    cursor.execute(query, (pars))
    cursor.fetchall()
    if cursor.rowcount >= 1:
        return True
    else:
        return False 


## ##################################################### ##
##                  tv series                            ##
## ##################################################### ##


def is_series_in_db(cursor, series):
    """ Checks if the tv series is already in the database
    """
    query = "SELECT tv_series.name FROM tv_series WHERE tv_series.name = %s AND tv_series.year = %s"
    pars = (series['title'], series['year'])
    cursor.execute(query,(pars))
    cursor.fetchall()
    if cursor.rowcount > 0 :
        return True
    else:
        return False

def add_new_series(cnx, cursor, series):
    """ Insert a new tv series 
    """
    add = ('INSERT INTO tv_series '
            # '(name, description, year, poster_url, imdb_url) '
             '(name, description, year, poster, imdb_id) '
             'VALUES (%s, %s, %s, %s, %s)')
    pars = (series['title'], series['description'], series['year'], series['poster_url'], series['imdb_id'])
    result = cursor.execute(add, (pars))
    if result != None:
        print("New series:",series['title'] + ' (' + series['year'] + ') inserted')
        cnx.commit()
        return 
    else:
        return #print result.id to error_table

def is_service_available_for_series(cursor, service_id, movie):
    """ Check if the streaming service is already available for the tv series
    """
    query = ('SELECT tv_series_streaming_service_selection.id AS "rows" '
             'FROM tv_series_streaming_service_selection ' 
             'LEFT JOIN tv_series '
             'ON tv_series.id = tv_series_streaming_service_selection.tv_series_id '
             'WHERE tv_series.name = %s AND tv_series.year = %s '
             'AND tv_series_streaming_service_selection.streaming_service_id = %s')
    pars = (movie['title'], movie['year'], service_id)
    cursor.execute(query, (pars))
    cursor.fetchall()
    if cursor.rowcount >= 1:
        return True
    else:
        return False 

def add_series_as_available(cnx, cursor, movie, service, url):
    """ Add series to be available on given streaming service 
    """
    add_service = ('INSERT INTO tv_series_streaming_service_selection '
                   '(tv_series_id, streaming_service_id, url) '
                   'VALUES (%s, %s, %s)')

    pars = (get_seriesId(cursor, movie), get_streamingServiceId(cursor, service), url)
    cursor.execute(add_service, (pars))
    result = cursor.lastrowid
    if result != None:
        cnx.commit()
        print(service + ' streaming available for the series ' +movie['title'])
        return 
    else:
        return False

def get_seriesId(cursor, movie):
    """ Get series id with name and year 
    """
    query = ('SELECT tv_series.id AS "id" '
             'FROM tv_series '
             'WHERE tv_series.name = %s AND tv_series.year = %s')
    pars = (movie['title'], movie['year'])
    
    cursor.execute(query, (pars))
    result = cursor.fetchall()
    if result != None:
        return result.pop()[0]
    else:
        return None

def add_genre_to_series(cnx, cursor, movie_id, genre_id):
    """ Link tv series to genre
    """
    add = ('INSERT INTO tv_series_genre '
             '(tv_series_id, genre_id) '
             'VALUES (%s, %s)')

    pars = (movie_id, genre_id)
    cursor.execute(add, (pars))
    result = cursor.lastrowid
    if result != None:
        print("Tv series has new genre")
        cnx.commit()
        return 
    else:
        return False

def add_score_to_series(cnx, cursor, score, movie_id, reviewer_id):
    """ Link movie to tv series
    """
    add = ('INSERT INTO tv_series_review '
             '(rating, tv_series_id, reviewer_id) '
             'VALUES (%s, %s, %s)')

    pars = (score, movie_id, reviewer_id)
    cursor.execute(add, (pars))
    result = cursor.lastrowid
    if result != None:
        print("Tv series has new rating")
        cnx.commit()
        return 
    else:
        return False
