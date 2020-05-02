import asyncio
import requests
import numpy as np
from pyppeteer import launch
from bs4 import BeautifulSoup

lista = []

def links():   
    page = requests.get("https://aeropuertosdelmundo.net/europa/espana")
    soup = BeautifulSoup(page.content, 'html.parser')
    aeropuertos = soup.select(".btn.btn-md.btn-ranking")
    for aeropuerto in aeropuertos:
        # print(aeropuerto['href'])
        link = "https://aeropuertosdelmundo.net" + aeropuerto['href']
        # print(link)
        pag = requests.get(link)
        unico = BeautifulSoup(pag.content, 'html.parser')
        salidas_link = unico.select('div.card-header ol li:nth-of-type(2) a')
        # print(salidas_link[0].get('href'))
        link_salidas = "https://aeropuertosdelmundo.net"+ salidas_link[0].get('href')
        pagina = requests.get(link_salidas)
        html = BeautifulSoup(pagina.content, 'html.parser')
        frame = html.select('iframe')
        elem = frame[0].get('src')
        lista.append(elem)
    
if __name__ == "__main__":   
    links()
      
async def main():
    lista_aerolinea = []
    for link in lista: 
        browser = await launch()
        page = await browser.newPage()
        await page.goto(link)
        noSelect = await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select") == null')
        #print(noSelect)
        if(noSelect == True):
            id_vuelos = []
            soup = BeautifulSoup(await page.content(), 'html.parser')
            tabla = soup.select(".tableListingTable > tbody > tr")
            tabla.pop(0)
            for fila in tabla:
                id_vuelos.append(fila.select_one("td > a")['href'])
        else:
            await page.evaluate('() => {document.querySelector("#flightStatusByRouteForm > select").value=1; document.querySelector("#flightStatusByRouteForm").submit()}')
            await page.waitForNavigation()
            id_vuelos = []
            
            #Select 1
            soup = BeautifulSoup(await page.content(), 'html.parser')
            tabla = soup.select(".tableListingTable > tbody > tr")
            tabla.pop(0)
            for fila in tabla:
                id_vuelos.append(fila.select_one("td > a")['href'])
            await page.evaluate('() => {document.querySelector("#flightStatusByRouteForm > select").value++; document.querySelector("#flightStatusByRouteForm").submit()}')
            await page.waitForNavigation()

            #Select 2
            soup = BeautifulSoup(await page.content(), 'html.parser')
            tabla = soup.select(".tableListingTable > tbody > tr")
            tabla.pop(0)
            for fila in tabla:
                id_vuelos.append(fila.select_one("td > a")['href'])
            await page.evaluate('() => {document.querySelector("#flightStatusByRouteForm > select").value++; document.querySelector("#flightStatusByRouteForm").submit()}')
            await page.waitForNavigation()
            
            #Select 3
            soup = BeautifulSoup(await page.content(), 'html.parser')
            tabla = soup.select(".tableListingTable > tbody > tr")
            tabla.pop(0)
            for fila in tabla:
                id_vuelos.append(fila.select_one("td > a")['href'])
            await page.evaluate('() => {document.querySelector("#flightStatusByRouteForm > select").value++; document.querySelector("#flightStatusByRouteForm").submit()}')
            await page.waitForNavigation()
            
            #Select 4
            soup = BeautifulSoup(await page.content(), 'html.parser')
            tabla = soup.select(".tableListingTable > tbody > tr")
            tabla.pop(0)
            for fila in tabla:
                id_vuelos.append(fila.select_one("td > a")['href'])
            await page.evaluate('() => {document.querySelector("#flightStatusByRouteForm > select").value++; document.querySelector("#flightStatusByRouteForm").submit()}')
            await page.waitForNavigation()
            
            #Select 5
            soup = BeautifulSoup(await page.content(), 'html.parser')
            tabla = soup.select(".tableListingTable > tbody > tr")
            tabla.pop(0)
            for fila in tabla:
                id_vuelos.append(fila.select_one("td > a")['href'])
            await page.evaluate('() => {document.querySelector("#flightStatusByRouteForm > select").value++; document.querySelector("#flightStatusByRouteForm").submit()}')
            await page.waitForNavigation()
            
            #Select 6
            soup = BeautifulSoup(await page.content(), 'html.parser')
            tabla = soup.select(".tableListingTable > tbody > tr")
            tabla.pop(0)
            for fila in tabla:
                id_vuelos.append(fila.select_one("td > a")['href'])
            await page.evaluate('() => {document.querySelector("#flightStatusByRouteForm > select").value++; document.querySelector("#flightStatusByRouteForm").submit()}')
            await page.waitForNavigation()

            #Select 7
            soup = BeautifulSoup(await page.content(), 'html.parser')
            tabla = soup.select(".tableListingTable > tbody > tr")
            tabla.pop(0)
            for fila in tabla:
                id_vuelos.append(fila.select_one("td > a")['href'])
            await page.evaluate('() => {document.querySelector("#flightStatusByRouteForm > select").value++; document.querySelector("#flightStatusByRouteForm").submit()}')
            await page.waitForNavigation()
            
            #Select 8
            soup = BeautifulSoup(await page.content(), 'html.parser')
            tabla = soup.select(".tableListingTable > tbody > tr")
            tabla.pop(0)
            for fila in tabla:
                id_vuelos.append(fila.select_one("td > a")['href'])
            await page.evaluate('() => {document.querySelector("#flightStatusByRouteForm > select").value++; document.querySelector("#flightStatusByRouteForm").submit()}')
            await page.waitForNavigation()

        

        # aerolineas = []
        for vuelo in id_vuelos:

            page = requests.get(vuelo)
            soup = BeautifulSoup(page.content, 'html.parser')

            id_vuelo = soup.select("div.ticket__Header-s1rrbl5o-1 > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1)")
            aerolinea = soup.select("div.ticket__Header-s1rrbl5o-1 > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2)")
            siglas = soup.select("div.ticket__Header-s1rrbl5o-1 > div:nth-child(1) > div > div:nth-child(2) > div a")
            origen = soup.select(
                "div.route-with-plane__RouteGroup-s154xj1h-0.geSBNm div:nth-child(1) div.text-helper__TextHelper-s8bko4a-0.eFnGmW")
            destino = soup.select(
                "div.route-with-plane__RouteGroup-s154xj1h-0.geSBNm div:nth-child(3) div.text-helper__TextHelper-s8bko4a-0.eFnGmW")
            estado1 = soup.select("div.ticket__StatusContainer-s1rrbl5o-17 div")
            hora_prog_est_origen = soup.select(
                "div.ticket__TicketContent-s1rrbl5o-6 > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
            hora_real_origen = soup.select(
                "div.ticket__TicketContent-s1rrbl5o-6 > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2)")
            hora_prog_est_destino = soup.select(
                "div.ticket__TicketContent-s1rrbl5o-6 > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
            hora_real_destino = soup.select(
                "div.ticket__TicketContent-s1rrbl5o-6 > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2)")

            gate_origen = soup.select(
                "div.ticket__TicketContent-s1rrbl5o-6 > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2)")
            gate_destino = soup.select(
                "div.ticket__TicketContent-s1rrbl5o-6 > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2)")
            
            terminal_origen = soup.select(
                "div.ticket__TicketContent-s1rrbl5o-6 > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2)")
            terminal_destino = soup.select(
                "div.ticket__TicketContent-s1rrbl5o-6 > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2)")

            
            for i in range(len(aerolinea)):
                a = aerolinea[i].text
                lista_aerolinea.append(a)
                
                # print(a)

            # print("---------------------------------")
            # print("Link vuelo: " + vuelo)
            # print("[Datos vuelo]")
            # print("Id: " + id_vuelo[0].text)
            # print("Aerolínea: " + aerolinea[0].text)
            # print("Estado del vuelo: ",estado1[0].text, " ", estado1[1].text)
            # print("[Datos origen]")
            # print("Siglas origen: " + siglas[0].text)
            # print("Origen: " + origen[0].text)
            # print("Hora programada: " + hora_prog_est_origen[0].text)
            # print("Hora estimada: " + hora_real_origen[0].text)
            # print("Terminal: " + terminal_origen[0].text)
            # print("Gate: " + gate_origen[0].text)
            # print("\n")
            # print("[Datos destino]")
            # print("Siglas destino: " + siglas[1].text)
            # print("Destino: " + destino[0].text)
            # print("Hora programada: " + hora_prog_est_destino[0].text)
            # print("Hora estimada: " + hora_real_destino[0].text)
            # print("Terminal: " + terminal_destino[0].text)
            # print("Gate: " + gate_destino[0].text)
            # print("---------------------------------")
            # print("\n")
        # print (lista_aerolinea)
        lista_aero_unica = np.unique(lista_aerolinea)
        print(len(lista_aero_unica))
        for e in range(len(lista_aero_unica)):
            print(lista_aero_unica[e])
        await browser.close()
    print(lista_aerolinea)

asyncio.get_event_loop().run_until_complete(main())
