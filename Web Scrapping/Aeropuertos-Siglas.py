import requests
from bs4 import BeautifulSoup

templateLink = "https://aeropuertosdelmundo.net"
page = requests.get('https://aeropuertosdelmundo.net/europa/espana/')
soup = BeautifulSoup(page.content, 'html.parser')
htmlLinks = soup.select('.btn-md.btn-ranking')

array = []
links = {}
links['siglas'] = []

for link in htmlLinks:
    array.append(templateLink + link['href'])

for link in array:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    airport = soup.select_one(".page-title").text   
    airport = {
        'name': airport.split("(")[0].replace("  ", ""),
        'acronym': airport.split("(")[1].replace(")", "")
    }
    links['siglas'].append(airport)
print(links)
requests.post('http://127.0.0.1:8000/api/siglas/datos', json=links)