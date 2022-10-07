import requests

pres_url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers = {
    'Cache-control': 'no-cache',
    'Accept': 'application/json; charset=utf-8;',
    'X-Requested-With': ' XMLHttpRequest'
}
soup = requests.get(pres_url, headers=headers)
print(soup.text)