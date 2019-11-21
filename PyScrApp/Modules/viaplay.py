import mysql.connector
from bs4 import BeautifulSoup


def viaplay_scraper():
    vp_base='https://content.viaplay.fi/pcdash-fi/leffat/kaikki?blockId=20822ace006b61ea5811662ab365729e&partial=1&pageNumber=1&sort=recently_added'

    return