import mysql.connector


def connect_to_database(file):
    """
    Open a database connection reading the credential from a file
    """
    with open("file",'r') as f:
        lines = f.read().splitlines()

    print("connecting to the mysql local container")
    cnx = mysql.connector.connect(lines[0],lines[1],lines[2],lines[4])
    print("initializing the cursor to the database")
    cursor =  cnx.cursor(buffered=True)

    return (cnx, cursor)

def disconnect_database(cnx, cursor):
    print("closing database cursor")
    cursor.close()
    print("closing connection to database")
    cnx.close()
    return


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

def get_streamingServiceId(name):
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