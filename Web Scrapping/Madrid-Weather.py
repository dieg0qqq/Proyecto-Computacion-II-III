import asyncio
import requests

from pyppeteer import launch
from bs4 import BeautifulSoup

page = requests.get('https://www.worldweatheronline.com/madrid-weather/madrid/es.aspx?day=20&tp=1')
soup = BeautifulSoup(page.content, 'html.parser')
    # Hour: 1 | Forecast: 2 | Temp: 3 | Rain: 5 | Cloud: 7 | Wind: 8 | Humidity: 11 | Pressure: 12
data = {}
data['clima'] = []
for i in range(1,25):
        hora = {
            'hour': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(1)').text,
            'forecast': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(2) > img').get('alt'),
            'temp': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(3)').text.replace(" °c", ""),
            'rain': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(5)').text.replace(" mm", ""),
            'cloud': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(7)').text.replace("%", ""),
            'wind': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(8)').text.replace(" km/h",""),
            'gust': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(9)').text.replace(" km/h",""),
            'dir': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(10) .flex_coll').getText(),
            'humidity': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(11)').text.replace("%", ""),
            'pressure': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(12)').text.replace(" mb", ""),
        }
        data['clima'].append(hora)
print(data)
requests.post('http://127.0.0.1:8000/api/clima/datos',json=data)

