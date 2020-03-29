# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:43:11 2020

@author: camii
"""
import requests
from bs4 import BeautifulSoup

pagina = requests.get("http://www.aena.es/es/aeropuerto-madrid-barajas/servicios-pasajeros.html")
htmlP = BeautifulSoup(pagina.content,'html.parser')

arrayLinks = []
link1 = htmlP.select('div.col-md-6 div.destacadosBox > p.titServices > a')
for i in range(len(link1)):
    link = "http://www.aena.es"+link1[i].get('href')
    #print(i,":",link)
    arrayLinks.append(link)

print(len(arrayLinks))
for i in range(len(arrayLinks)):
    cu = requests.get(arrayLinks[i])
    #print(arrayLinks[i])
    html = BeautifulSoup(cu.content, 'html.parser')
    #print(html, "\npagina:",i)
    titulo = html.select("div.encabezadoTit > div.izq")
    
    #print(titulo[i].text)
    print(i)
    for a in range(len(titulo)):
        print(a,": .... +",titulo[a].text)