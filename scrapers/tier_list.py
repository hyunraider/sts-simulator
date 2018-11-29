from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import ssl
import httplib

def scrape(character):
    # name -> (score, rarity)
    # rarity: 0 - common, 1 - uncommon, 2 - rare
    dict = {}
    url = "https://spirelogs.com/stats/{}/tierlist.php".format(character)
    print(url)
    html_page = httplib.HTTPSConnection(url)
    soup = bs(html_page, features='html.parser')

    all_tables = soup.find_all("div", {"class": "percent33"})
    print(all_tables)

scrape("defect")
