from datetime import date
import requests
from bs4 import BeautifulSoup

aeropuerto_sigla = 'zaz' #El parámetro
page = requests.get(f'https://www.worldweatheronline.com/v2/search.ashx?qry={aeropuerto_sigla}').json()[0]
page = requests.get('https://www.worldweatheronline.com' + page['url'])
page = requests.get(page.url+'?day=20&tp=1')
soup = BeautifulSoup(page.content, 'html.parser')
data={}
data['clima'] = {
    'id_aeropuerto': aeropuerto_sigla,
    'fecha': date.today().strftime("%Y-%m-%d"),
    'datos': []
}
for i in range(1, 25):
    data['clima']['datos'].append({
        'hora': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(1)').text,
        'prevision': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(2) > img').get('alt'),
        'temperatura': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(3)').text.replace(" °c", ""),
        'lluvia': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(5)').text.replace(" mm", ""),
        'nubes': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(7)').text.replace("%", ""),
        'viento': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(8)').text.replace(" km/h",""),
        'rafagas': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(9)').text.replace(" km/h",""),
        'direccion': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(10) .flex_coll').getText(),
        'humedad': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(11)').text.replace("%", ""),
        'presion': soup.select_one(f'.tb_row:nth-child({i}) > .tb_cont_item:nth-child(12)').text.replace(" mb", ""),
    })
print(data)