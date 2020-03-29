# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:15:00 2020

@author: camii
"""

import requests
from bs4 import BeautifulSoup

pagina=requests.get("http://www.aena.es/es/aeropuerto-madrid-barajas/todas-tiendas.html")
htmlP = BeautifulSoup(pagina.content, 'html.parser')

nombreTienda = htmlP.select("div.col-md-9 > div.col-md-4 > div.negocioBox > div.negocioInt > p > a")
direccionTienda = htmlP.select("div.col-md-9 > div.col-md-4 > div.negocioBox > div.negocioInt > ul > li")
for i in range(len(nombreTienda)):
    print(i ,": \n tienda:",nombreTienda[i].text, "\n direccion:" ,direccionTienda[i].text)