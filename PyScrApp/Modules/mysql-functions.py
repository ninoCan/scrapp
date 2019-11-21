import mysql.connector

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
