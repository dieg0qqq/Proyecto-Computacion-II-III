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
            'hora': datos[11+(10*(i-1))].text,
            'prevision': datos[12+(10*(i-1))].text.rstrip(),
            'temperatura': datos[13+(10*(i-1))].text.replace(" °c", ""),
            'lluvia': datos[17+(10*(i-1))].text.split(" ")[0],
            'nubes': datos[19+(10*(i-1))].text.replace("%", ""),
            'viento': datos[15+(10*(i-1))].text.replace(" km/h",""),
            'rafagas': datos[16+(10*(i-1))].text.replace(" km/h",""),
            #'direccion' ya no existe en la web
            'humedad': datos[18+(10*(i-1))].text.replace("%", ""),
            'presion': datos[20+(10*(i-1))].text.replace(" mb", ""),
        })
        #print(data['clima'][i-1])

print(siglas)        
print(data)
requests.post('http://127.0.0.1:8000/api/clima/datos', json=data)