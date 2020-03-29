import requests
import re
from bs4 import BeautifulSoup

url = [0,6,12,18]
for i in range(len(url)):
    index = "https://www.madrid-airport.com/arrivals.php?tp=" + str(url[i])
    page = requests.get(index)

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]
    body = list(html.children)[3]
    rows = body.find_all('div', class_ = 'flight-row')

    origin = body.find_all('div', class_ = 'flight-col flight-col__dest-term')
    arrival = body.find_all('div', class_ = 'flight-col flight-col__hour')
    flight = body.find_all('div', class_ = 'flight-col flight-col__flight')
    airline = body.find_all('div', class_ = 'flight-col flight-col__airline')
    terminal = body.find_all('div', class_ = 'flight-col flight-col__terminal')
    status = body.find_all('a', class_ = 'flight-col flight-col__terminal')

    for i in range(len(origin)):
        print(origin[i].get_text())
    for i in range(len(arrival)):  
        print(arrival[i].get_text())
    for i in range(len(flight)):
        print(flight[i].get_text())
    for i in range(len(airline)):
        print(airline[i].get_text()) 
    for i in range(len(terminal)):
        print(terminal[i].get_text())
    for i in range(len(status)):
        print(status[i].get_text())