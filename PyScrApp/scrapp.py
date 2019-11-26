#loading package dependencies
from Modules.hbo import *
from Modules.mysql_functions import *
from Modules.requests_soup import *
from Modules.viaplay import *
import mysql.connector

def main():
    """
    This is going to connect to mysql database and scrape data from the various services
    """
    
    cnx, cursor = connect_to_database("database_credential.key")

    print('Scraping data from the internet...')
    #print("Scraping movies from HBO")
    #hbo_scraper(cnx,cursor)
    print("Scraping movies from viaplay")
    viaplay_scraper(cnx, cursor)
    print('Scraping complete!')

    disconnect_database(cnx, cursor)
    return

if __name__ == "__main__":
    main()