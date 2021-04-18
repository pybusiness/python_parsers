from bs4 import BeautifulSoup
import requests

def parse():
    URL = "https://jut.su/narutoo/film/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('a', class_ = "pos_rel")

    for item in items:
        print(item.get_text(strip = True))
parse()
print("\n")
def parse_2():
    URL = "https://jut.su/narutoo/season-2/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('a', class_ = "short-btn green video the_hildi")

    for item in items:
        print(item.get('title'))
parse_2()