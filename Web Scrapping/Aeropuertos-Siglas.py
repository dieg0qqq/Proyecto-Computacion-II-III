import requests
from bs4 import BeautifulSoup

lista = []
templateLink = "https://aeropuertosdelmundo.net"
page = requests.get('https://aeropuertosdelmundo.net/europa/espana/')
soup = BeautifulSoup(page.content, 'html.parser')
htmlLinks = soup.select('.btn-md.btn-ranking')
links = []
for link in htmlLinks:
    links.append(templateLink + link['href'])
for link in links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    airport = soup.select_one(".page-title").text   
    airport = {
        'name': airport.split("(")[0].replace("  ", ""),
        'acronym': airport.split("(")[1].replace(")", "")
    }
    lista.append(airport)
print(lista)