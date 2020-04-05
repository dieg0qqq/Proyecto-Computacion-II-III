import requests
from bs4 import BeautifulSoup

url = [0,6,12,18]
for i in range(len(url)):
    index = "https://www.madrid-airport.com/departures.php?tp=" + str(url[i])
    page = requests.get(index)

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]
    body = list(html.children)[3]
    rows = body.find_all('div', class_ = 'flight-row')

    for j in range(len(rows)):
        print(rows[j].get_text())
    