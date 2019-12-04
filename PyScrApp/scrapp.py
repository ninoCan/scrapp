# loading package dependencies
from Modules.hbo import hbo_scraper, hbo_series_scraper 
from Modules.mysql_functions import connect_to_database, disconnect_database 
# from Modules.requests_soup import *
from Modules.viaplay import viaplay_scraper, viaplay_series_scraper 


def main():
    """ This is going to connect to mysql database and
        scrape data from the various services
    """

    cnx, cursor = connect_to_database("database_credential.key")

    print('Scraping data from the internet...')
    print("Scraping movies from HBO")
    hbo_scraper(cnx, cursor)
    print("Scraping movies from viaplay")
    viaplay_scraper(cnx, cursor)
    # print("Scraping tv series from hbo")
    # hbo_series_scraper(cnx, cursor)
    # print("Scraping tv series from viaplay")
    # viaplay_series_scraper(cnx, cursor)
    print('Scraping complete!')

    disconnect_database(cnx, cursor)
    return


if __name__ == "__main__":
    main()
