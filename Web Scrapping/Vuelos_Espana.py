import asyncio
import requests
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

        for vuelo in id_vuelos:

            page = requests.get(vuelo)
            soup = BeautifulSoup(page.content, 'html.parser')

            id_vuelo = soup.select("div.text-helper__TextHelper-s8bko4a-0.ekVwAR")
            aerolinea = soup.select("div.text-helper__TextHelper-s8bko4a-0.dNaxcH")
            siglas_origen = soup.select("div.route-with-plane__RouteGroup-s154xj1h-0.geSBNm div:nth-child(1) a.route-with-plane__AirportLink-s154xj1h-3.dBXRil")
            siglas_destino = soup.select("div.route-with-plane__RouteGroup-s154xj1h-0.geSBNm div:nth-child(3) a.route-with-plane__AirportLink-s154xj1h-3.dBXRil")
            origen = soup.select("div.route-with-plane__RouteGroup-s154xj1h-0.geSBNm div:nth-child(1) div.text-helper__TextHelper-s8bko4a-0.eFnGmW")
            destino = soup.select("div.route-with-plane__RouteGroup-s154xj1h-0.geSBNm div:nth-child(3) div.text-helper__TextHelper-s8bko4a-0.eFnGmW")
            estado1 = soup.select("div.text-helper__TextHelper-s8bko4a-0.kWxgTv")
            estado2 = soup.select("div.text-helper__TextHelper-s8bko4a-0.yeKfN")

            hora_prog_est_origen = soup.select("div.ticket__TicketContent-s1rrbl5o-6.ccpWcM div:nth-child(1) div.ticket__InfoSection-s1rrbl5o-8.igyRqP div.text-helper__TextHelper-s8bko4a-0.cCfBRT")
            hora_prog_est_destino = soup.select("div.ticket__TicketContent-s1rrbl5o-6.ccpWcM div:nth-child(2) div.ticket__InfoSection-s1rrbl5o-8.igyRqP div.text-helper__TextHelper-s8bko4a-0.cCfBRT")
            
            # hora_prog_origen = soup.select("div.ticket__TicketContent-s1rrbl5o-6.ccpWcM div:nth-child(1) div.ticket__TimeGroupContainer-s1rrbl5o-11.ckbilY div:nth-children(1) div.text-helper__TextHelper-s8bko4a-0.cCfBRT")
            # hora_est_origen = soup.select("div.ticket__TicketContent-s1rrbl5o-6.ccpWcM div:nth-child(1) div.ticket__TimeGroupContainer-s1rrbl5o-11.ckbilY div:nth-children(2) div.text-helper__TextHelper-s8bko4a-0.cCfBRT")
            
            terminal_origen = soup.select("div.ticket__TicketContent-s1rrbl5o-6.ccpWcM div:nth-child(1) div.ticket__TGBSection-s1rrbl5o-14.bcEbYB.ticket__InfoSection-s1rrbl5o-8.isGpsI div.ticket__TGBValue-s1rrbl5o-16.icyRae.text-helper__TextHelper-s8bko4a-0.cCfBRT")
            gate_origen = soup.select("div.ticket__TicketContent-s1rrbl5o-6.ccpWcM div:nth-child(1) ticket__TGBSection-s1rrbl5o-14.gOacyS.ticket__InfoSection-s1rrbl5o-8.isGpsI div.ticket__TGBValue-s1rrbl5o-16.icyRae.text-helper__TextHelper-s8bko4a-0.cCfBRT")
            
            terminal_destino = soup.select("div.ticket__TicketContent-s1rrbl5o-6.ccpWcM div:nth-child(2) div.ticket__TGBSection-s1rrbl5o-14.bcEbYB.ticket__InfoSection-s1rrbl5o-8.isGpsI div.ticket__TGBValue-s1rrbl5o-16.icyRae.text-helper__TextHelper-s8bko4a-0.cCfBRT")
            gate_destino = soup.select("div.ticket__TicketContent-s1rrbl5o-6.ccpWcM div:nth-child(2) ticket__TGBSection-s1rrbl5o-14.gOacyS.ticket__InfoSection-s1rrbl5o-8.isGpsI div.ticket__TGBValue-s1rrbl5o-16.icyRae.text-helper__TextHelper-s8bko4a-0.cCfBRT")
            
            try:
                print("---------------------------------")
                print("Link vuelo: " + vuelo)
                print("[Datos vuelo]")
                print("Id: " + id_vuelo[0].text)
                print("Aerolínea: " + aerolinea[0].text)
                print("Estado: " + estado1[0].text + " " + estado2[0].text)
                print("\n")
                print("[Datos origen]")
                print("Siglas origen: " + siglas_origen[0].text)
                print("Origen: " + origen[0].text)
                print("Hora programada: " + hora_prog_est_origen[0].text)
                print("Hora estimada: " + hora_prog_est_origen[1].text)
                print("Terminal: " + terminal_origen[0].text)
                print("Gate: " + gate_origen)
                print("\n")
                print("[Datos destino]")
                print("Siglas destino: " + siglas_destino[0].text)
                print("Destino: " + destino[0].text)
                print("Hora programada: " + hora_prog_est_destino[0].text)
                print("Hora estimada: " + hora_prog_est_destino[1].text)
                print("Terminal: " + terminal_destino[0].text)
                print("Gate: " + gate_destino[0].text)
                print("---------------------------------")
                print("\n")
            
            except:
                print("Algo malo ocurrió")

        await browser.close()

asyncio.get_event_loop().run_until_complete(main())
