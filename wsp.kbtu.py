import requests
import fake_useragent
from bs4 import BeautifulSoup

link = "https://wsp.kbtu.kz/#!LoginView/"

data = {
    'gwt-uid-4': 'your_username',
    'gwt-uid-6': 'your_password'
}