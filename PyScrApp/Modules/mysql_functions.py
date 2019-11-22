import mysql.connector


def connect_to_database(file):
    """
    Open a database connection reading the credential from a file
    """
    with open(file,'r') as f:
        cred = f.read().splitlines()

    print("connecting to the mysql local container")
    cnx = mysql.connector.connect(user=cred[0], password=cred[1], host=cred[2], database=cred[3])
    print("initializing the cursor to the database")
    cursor =  cnx.cursor(buffered=True)

    return cnx, cursor

def disconnect_database(cnx, cursor):
    print("closing database cursor")
    cursor.close()
    print("closing connection to database")
    cnx.close()
    return

# def add_to_db(cnx, cursor, par):
#     """ 
#     Add the title of a movie to mysql database
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
    query = "SELECT movie.name FROM movie WHERE movie.name = %s AND movie.year = %s"
    pars = (movie['title'], movie['year'])
    cursor.execute(query,(pars))
    cursor.fetchall()
    if cursor.rowcount > 0 :
        return True
    else:
        return False

def get_streamingServiceId(cursor, service):
    """ Get streaming service id with name """
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
    """ Get movie id with name and year """
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
    """ Get movie streaming service id(s) where movie is available to watch with name and year """
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
    """ Add movie to be available on given streaming service """
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
    """ Insert a new movie """
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
#     """ 
#     Add the title and year of a movie to mysql database
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
    """ Insert new review """
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
    """ Link movie to genre """
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
    """ Add new genre """
    query = ('INSERT INTO genre '
             '(name) '
             'VALUES (%s)')
    params = (name,)
    cursor.execute(query, (params))
    result = cursor.lastrowid
    if result != None:
        print("Added new genre to table: ", name)
        cnx.commit()
        return 
    else:
        print("genre NOT ADDED")
        return False

def get_genreId(cursor, name):
    """ Get genre id with name"""
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

# def add_hbo_to_steamingService(cnx, cursor, url):
#     add = ('INSERT INTO streaming_services IF NOT EXISTS '
#            '(name, scrape_url, type) '
#            'VALUES (%s,%s)')
#     pars = ('hbo', url)
#     cursor.execute(add, (pars))
#     cnx.commit()
#     return 
