#loading package dependencies
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import mysql.connector

#function definitions

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_html_response(resp):
                return ('html', resp.content)
            elif is_good_xml_response(resp):
                return ('xml', resp.content)
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_html_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def is_good_xml_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('xml') > -1)

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

##

def hbo_scraper():
    """
    Scraper from hbo_nordic
    """
    #base page 
    hbo_base = 'https://api-hbon.hbo.clearleap.com/cloffice/client/web/browse/ea73aabd-24a3-473e-8f3a-39aeb7f0f93e?max=20&language=fi_hbon&offset='
    
    i=0 #counter to loop through the page
    flag = True #flag to control the page scraper loop

    while flag:
        url = hbo_base + str(i)
        raw = simple_get(url) #get the raw page
        content = BeautifulSoup(raw[1], "lxml-xml") #parse the content with BS
        i += 1
#        for elem in content.select('item'):
#            for title in elem.select('title'):
#                print(title.text)
        for elem in content.select('item'):
            print(elem.select('title').pop())#.text)
        if content.select('errorCode'):
            flag = False
    return

def viaplay_scraper():
    vp_base='https://content.viaplay.fi/pcdash-fi/leffat/kaikki?blockId=20822ace006b61ea5811662ab365729e&partial=1&pageNumber=1&sort=recently_added'

    return

def main():
    """
    This is going to scrape from pages the entries for the database
    """
    
    hbo_scraper()
    #'https://content.viaplay.fi/pcdash-fi/leffat/kaikki?blockId=20822ace006b61ea5811662ab365729e&partial=1&pageNumber=1&sort=recently_added',#viaplay
    #]
    

    #while flag:
    #    url = hbo_base + str(i)
    #    raw = simple_get(url) #get the raw page
        #if raw[0] == 'html':
        #    content = BeautifulSoup(raw[1], "lxml")
        #elif raw[0]=='xml':
        #    content = BeautifulSoup(raw[1], "lxml-xml")
    #    i += 1
    #    for elem in content.select('item'):
    #        for title in elem.select('title'):
    #            print(title.text)
    #    print(i)
    #    if content.select('errorCode'):
    #        flag = False
    return


if __name__ == "__main__":
    print('Scraping data from the internet...')
    main()
    print('Scraping complete!')
