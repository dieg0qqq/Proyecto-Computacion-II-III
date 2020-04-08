import requests
import re
from bs4 import BeautifulSoup

url = [0,6,12,18]
for i in range(len(url)):
    index = "https://www.madrid-airport.com/departures.php?tp=" + str(url[i])
    page = requests.get(index)

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]
    body = list(html.children)[3]
    rows = body.find_all('div', class_ = 'flight-row')

    destination = body.find_all('div', class_ = 'flight-col flight-col__dest-term')
    arrival = body.find_all('div', class_ = 'flight-col flight-col__hour')
    flight = body.find_all('div', class_ = 'flight-col flight-col__flight')
    airline = body.find_all('div', class_ = 'flight-col flight-col__airline')
    terminal = body.find_all('div', class_ = 'flight-col flight-col__terminal')
    #status = body.find_all(re.compile("status--\w*[\s\S]*?<a href=[\s\S]*?>(\w.*)<[\s\S]*?"))

    for i in range(len(destination)):
        print("Destino: "+ destination[i].get_text())
   
        print("Hora salida: " + arrival[i].get_text())
    
        print("Vuelo: " + flight[i].get_text())
   
        print("Aerolinea: " + airline[i].get_text()) 
   
        print("Terminal: " + terminal[i].get_text())
    # for i in range(len(status)):
    #     print(status[i].get_text())