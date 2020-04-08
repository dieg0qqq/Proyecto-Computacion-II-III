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
            print(vuelo)
        await browser.close()

asyncio.get_event_loop().run_until_complete(main())
