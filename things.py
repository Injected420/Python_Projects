import requests
import random
from bs4 import BeautifulSoup

word = input(f'[*]Input your search term: \n')
url = f'https://duckduckgo.com/?t=ffab&q={word}&ia=web'
search_req = requests.get(url).text
print(search_req)