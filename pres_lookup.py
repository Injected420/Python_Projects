from bs4 import BeautifulSoup
import requests

pres_url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers = {
    'Cache-control': 'no-cache'
}
req = requests.get(pres_url, headers=headers)
soup = BeautifulSoup(requests.get(req).content, "html.parser")
press = soup.find("tr").p.text
press = soup.find("tr").p.text