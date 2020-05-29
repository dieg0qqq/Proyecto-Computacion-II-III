from datetime import date
import requests
from bs4 import BeautifulSoup


siglas = []
data={}
data['clima'] = []

ruta_rel = "Web Scrapping\\Archivos_JSON\\"
archivo = open(ruta_rel + "Siglas" + ".txt","r", encoding="utf-8")

for line in archivo:
    siglas.append(line)
    aeropuerto_sigla = line #El parámetro
    page = requests.get(f'https://www.worldweatheronline.com/v2/search.ashx?qry={aeropuerto_sigla}').json()[0]
    page = requests.get('https://www.worldweatheronline.com' + page['url'])
    page = requests.get(page.url+'?day=20&tp=1')
    soup = BeautifulSoup(page.content, 'html.parser')
    print("Visto")
    datos = soup.select('.col.mr-1')
    for i in range(1, 25):
        data['clima'].append({
            'idaeropuerto': aeropuerto_sigla,
            'fecha': date.today().strftime("%Y-%m-%d"),
            'hora': datos[12+(11*(i-1))].text,
            'prevision': datos[13+(11*(i-1))].select('.img-fluid')[0].get('alt'),
            'temperatura': datos[14+(11*(i-1))].text.replace(" °c", ""),
            'lluvia': datos[18+(11*(i-1))].text.replace(" mm", ""),
            'nubes': datos[21+(11*(i-1))].text.replace("%", ""),
            'viento': datos[16+(11*(i-1))].text.replace(" km/h",""),
            'rafagas': datos[17+(11*(i-1))].text.replace(" km/h",""),
            #'direccion' ya no existe en la web
            'humedad': datos[20+(11*(i-1))].text.replace("%", ""),
            'presion': datos[21+(11*(i-1))].text.replace("%", ""),
        })
        #print(data['clima'][i-1])

print(siglas)        
print(data)
requests.post('http://127.0.0.1:8000/api/clima/datos', json=data)