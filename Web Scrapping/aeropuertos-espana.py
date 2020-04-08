import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def main():
    browser = await launch()
    page = await browser.newPage()
    link = "https://www.flightstats.com/go/weblet?guid=d56928966b03ae86:-3be13f33:1197c2fe4bc:38ea&imageColor=black&language=Spanish&weblet=status&action=AirportFlightStatus&airportCode=MAD&airportQueryType=0"
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
