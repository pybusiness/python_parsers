from bs4 import BeautifulSoup
import requests

def parse():
    URL = "https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'offer-wrapper')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('a', class_ = 'marginright5 link linkWithHash detailsLink linkWithHashPromoted').get_text(strip = True)
        })

        for comp in comps:
            print(comp['title'])
parse()