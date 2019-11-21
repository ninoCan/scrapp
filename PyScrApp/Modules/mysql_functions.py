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

def get_streamingServiceId(cursor, name):
    """ Get streaming service id with name """
    query = ('SELECT streaming_service.id AS "id"'
              'FROM streaming_service'
              'WHERE streaming_service.name %s')
    params = (name)
    result = cursor.execute(query, params)
    if result.rowcount >= 1:
        return result.id
    else:
        return None

def get_movieId(cursor, par):
    """ Get movie id with name and year """
    query = ('SELECT movie.id AS "id"'
             'FROM movie'
             'WHERE movie.name %s AND movie.year %s')

    result = cursor.execute(query, (par))
    if result.rowcount >= 1:
        return result.id
    else:
        return None

def get_movieServiceIds(cursor, par):
    """ Get movie streaming service id(s) where movie is available to watch with name and year """
    query = ('SELECT movie_streaming_service_selection.streaming_service_id AS "id"'
             'FROM movie_streaming_service_selection'
             'LEFT JOIN movie' 
             'ON movie.id = movie_streaming_service_selection.movie_id'
             'WHERE movie.name = %s AND movie.year = %s')
    
    result = cursor.execute(query, (par))
    if result.rowcount >= 1:
        return result
    else:
        return None

def get_genreId(name):
    """ Get genre id with name"""
    query = ('SELECT genre.id AS "id"'
             'FROM genre WHERE genre.name = %s')

    params = (name,)
    result = cursor.execute(query, (params))
    if result.rowcount >= 1:
        return result.id
    else:
        return None

def add_movie_as_available(cnx, cursor, movie_id, service_id, watch_url):
    """ Add movie to be available on given streaming service """
    query = ('INSERT INTO movie_streaming_service_selection (movie_id, streaming_service_id, url)'
             'VALUES (%s, %s, %s)')

    params = (movie_id, service_id, watch_url)
    result = cursor.execute(query, (params))
    if result.rowcount >= 1:
        return True
    else:
        return False

def add_new_movie(name, description, year, poster_url):
    """ Insert a new movie """
    query = ('INSERT INTO movie'
             '(name, description, year, poster_url)'
             'VALUES (%s, %s, %s, %s)')
    params = (name, description, year, poster_url)
    result = cursor.execute(query, (params))
    if result.rowcount >= 1:
        return true
    else:
        return false

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

def add_movieReview(movie_id, reviewer_id, rating):
    """ Insert new review """
    query = ('INSERT INTO movie_review'
             '(movie_id, reviewer_id, rating)'
             'VALUES (%s, %s, %s)')

    params = (movie_id, reviewer_id, rating)
    result = cursor.execute(query, (params))
    if result.rowcount >= 1:
        return True
    else:
        return False

def add_genre_to_movie(movie_id, genre_id):
    """ Link movie to genre """
    query = ('INSERT INTO movie_genre'
             '(movie_id, genre_id)'
             'VALUES (%s, %s)')

    params = (movie_id, genre_id)
    result = cursor.execute(query, (params))
    if result.rowcount >= 1:
        return True
    else:
        return False

def add_new_genre(name):
    """ Add new genre """
    query = ('INSERT INTO genre'
             '(name)'
             'VALUES (%s)')
    params = (name,)
    result = cursor.execute(query, (params))
    if result.rowcount >= 1:
        return True
    else:
        return False

# def add_hbo_to_steamingService(cnx, cursor, url):
#     add = ('INSERT INTO streaming_services IF NOT EXISTS'
#            '(name, url)'
#            'VALUES (%s,%s)')
#     pars = ('hbo', url)
#     cursor.execute(add, (pars))
#     cnx.commit()
#     return 
