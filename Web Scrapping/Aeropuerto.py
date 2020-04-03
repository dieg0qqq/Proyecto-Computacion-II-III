import requests
from bs4 import BeautifulSoup

url1 = [0,3,6,9,12,15,18,21]
url2 = [3,6,9,12,15,18,21,0]

for i in range(len(url1)):

    index = "https://www.aeropuertomadrid-barajas.com/salidas.html?t="+str(url1[i])+ "-"+str(url2[i])+"%2B1&a="
    page = requests.get(index)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]

    # hora = body.find_all('span', class_ = 'color:#6a8ec8')
    hora_destino = body.find_all('div', class_ = 'flightListOtherAirport')
    terminal = body.find_all('div', class_ = 'flightListTerminal')
    estatus = body.find_all('div', class_ = 'flightListTimeStatus')
    identificador = body.find_all('div', class_ = 'flightListFlightIDs')

    for j in range(len(hora_destino)):
        print("Hora - Destino: " + hora_destino[j].get_text())   
        print("Terminal: " + terminal[j].get_text())
        print("Estado: " + estatus[j].get_text())
        print("ID: " + identificador[j].get_text()+("\n"))
        print("\n")
        