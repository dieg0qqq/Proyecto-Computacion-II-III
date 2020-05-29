import requests
from bs4 import BeautifulSoup

templateLink = "https://aeropuertosdelmundo.net"
page = requests.get('https://aeropuertosdelmundo.net/europa/espana/')
soup = BeautifulSoup(page.content, 'html.parser')
htmlLinks = soup.select('.btn-md.btn-ranking')

array = []
lista_siglas = []
links = {}
links['siglas'] = []

for link in htmlLinks:
    array.append(templateLink + link['href'])

for link in array:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    airport = soup.select_one(".page-title").text 
    airport2 = airport.split("(")[1].replace(")", "")  
    airport = {
        'name': airport.split("(")[0].replace("  ", ""),
        'acronym': airport.split("(")[1].replace(")", "")
    }
    
    lista_siglas.append(airport2)
    links['siglas'].append(airport)

# ruta_rel = "Web Scrapping\\Archivos_JSON\\"
# archivo = open(ruta_rel + "Siglas.txt","w", encoding="utf-8")
# for e in lista_siglas:
#     archivo.write(e + "\n")
# archivo.close()
print(lista_siglas)
print(links)
requests.post('http://127.0.0.1:8000/api/siglas/datos', json=links)