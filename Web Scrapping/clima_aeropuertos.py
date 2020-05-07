import requests
from bs4 import BeautifulSoup
import re
import datetime

page = requests.get("https://aeropuertosdelmundo.net/europa/espana/")
soup = BeautifulSoup(page.content, 'html.parser')
aeropuertos = soup.select(".btn.btn-md.btn-ranking")
linkd_presultados = []
nombre_aeropuertos= []
for aeropuerto in aeropuertos:
    hey = re.sub(" ", "+", aeropuerto.text)
    link = "https://www.eltiempo.es/buscar?q="+hey
    pag = requests.get(link)
    be = BeautifulSoup(pag.content, 'html.parser')
    nombre_aeropuertos.append(aeropuerto.text)
    links_por_pagina = be.select("ul.m_search_results > li:nth-of-type(1) > a")


    if (len(links_por_pagina) == 0):
        hey1 = re.sub("Aeropuerto de ", "", aeropuerto.text)
        hey = re.sub(" ", "+", hey1)
        link = "https://www.eltiempo.es/buscar?q="+hey
        pag = requests.get(link)
        be = BeautifulSoup(pag.content, 'html.parser')
        links_por_pagina = be.select("ul.m_search_results > li:nth-of-type(1) > a")
        linkd_presultados.append(links_por_pagina[0].get('href'))
    else:
        linkd_presultados.append(links_por_pagina[0].get('href'))
for i in range(len(linkd_presultados)):
    li = requests.get(linkd_presultados[i])
    be = BeautifulSoup(li.content, 'html.parser')
    por_hora = be.select('section.m_nav.m_nav-tabs > ul > li:nth-of-type(2) > a')
    linkd_presultados[i] = por_hora[0].get('href')

for i in linkd_presultados:
    print(i)
    x = datetime.datetime.now()
    hora = int(x.strftime("%H"))
    print(hora)
    minutos = int(x.strftime("%M"))
    if minutos > 45:
        hora = hora+1

    total_filas = (23 - hora) + 2
    print(total_filas)
    li = requests.get(i)
    be = BeautifulSoup(li.content, 'html.parser')
    horas = be.select("div.m_table_weather_hour_detail_hours")
    prevision = be.select("div.m_table_weather_hour_detail_pred")
    viento= be.select("div.m_table_weather_hour_detail_wind")
    velocidad =be.select("div.m_table_weather_hour_detail_med")
    rachas = be.select("div.m_table_weather_hour_detail_gust.m_table_weather_hour_detail_child_mobile span:nth-of-type(2)")
    lluvia = be.select("div.m_table_weather_hour_detail_rain.m_table_weather_hour_detail_child_mobile span:nth-of-type(2)")
    nieve=be.select("div.m_table_weather_hour_detail_snow.m_table_weather_hour_detail_child_mobile span:nth-of-type(2)")
    nubes =be.select("div.m_table_weather_hour_detail_clouds.m_table_weather_hour_detail_child_mobile span:nth-of-type(2)")
    tormenta = be.select("div.m_table_weather_hour_detail_thunder.m_table_weather_hour_detail_child_mobile > span:nth-of-type(2)")
    humedad = be.select("div.m_table_weather_hour_detail_child.m_table_weather_hour_detail_hum span:nth-of-type(2)")
    presion = be.select("div.m_table_weather_hour_detail_child.m_table_weather_hour_detail_preas span:nth-of-type(2)")
    precipitacion = be.select("div.modules div:nth-child(2) div:nth-child(14) > span:nth-child(2)")

    print(horas)

    for k in range(1, total_filas):
        it = k-1
        print(aeropuerto)
        print(horas[k].text)
        print("prevision: ",prevision[k].text.replace("°", ""))

        pattern = re.compile("<i\sclass=\"icon\sicon-[a-z-0-9_]*\s(.*)\"><\/i>")
        z = pattern.findall(str(viento[k]))
        print("direccion del viento: ",z[0])

        print("velocidad: ",velocidad[k].text.replace(" km/h", ""))

        print("rachas: ",rachas[it].text.replace(" km/h", ""))
        print("lluvias: ",lluvia[it].text.replace(" mm", ""))
        print("nieve: ",nieve[it].text.replace(" cm", ""))
        print("nubes: ", nubes[it].text.replace("%", ""))
        print("tormentas: ", tormenta[it].text.replace("%", ""))
        print("Humedad: ", humedad[it].text.replace("%", ""))
        print("presion: ", presion[it].text.replace(" hPa", ""))
        print("prob. de precipitacion: " , precipitacion[k].text.replace("%", "") )

        print("-----------------------")