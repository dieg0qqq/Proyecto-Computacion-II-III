import requests
from bs4 import BeautifulSoup

page = requests.get("https://aeropuertosdelmundo.net/europa/espana")
soup = BeautifulSoup(page.content, 'html.parser')
aeropuertos = soup.select(".btn.btn-md.btn-ranking")
for aeropuerto in aeropuertos:
    # print(aeropuerto['href'])
    link = "https://aeropuertosdelmundo.net" + aeropuerto['href']
    # print(link)
    pag = requests.get(link)
    unico = BeautifulSoup(pag.content, 'html.parser')
    
    salidas_link = unico.select('div.card-header ol li:nth-of-type(2) a')
    # print(salidas_link[0].get('href'))
    
    link_salidas = "https://aeropuertosdelmundo.net"+ salidas_link[0].get('href')
    pagina = requests.get(link_salidas)
    html = BeautifulSoup(pagina.content, 'html.parser')
    
    frame = html.select('iframe')
    print(frame[0].get('src'))