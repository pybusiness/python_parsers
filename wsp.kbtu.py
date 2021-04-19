import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()

link = "https://wsp.kbtu.kz/#!LoginView/"
user = fake_useragent.UserAgent().random
header = {
    'user-agent': user
}

data = {
    'gwt-uid-6': 'username',
    'gwt-uid-4': 'password',
    'gwt-uid-2': 'on'
}

responce = session.post(link, data = data, headers = header).text
profile_info = 'https://wsp.kbtu.kz/StudentSchedule'
profile_responce = session.get(profile_info, headers = header).text
print(profile_responce)