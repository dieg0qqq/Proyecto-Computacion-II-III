import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def main():
    browser = await launch({'headless': True})
    page = await browser.newPage()
    link = "https://www.flightstats.com/go/weblet?guid=d56928966b03ae86:-3be13f33:1197c2fe4bc:38ea&imageColor=black&language=Spanish&weblet=status&action=AirportFlightStatus&airportCode=MAD&airportQueryType=0"
    await page.goto(link)
    await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select").value=0')
    id_vuelos = []

    #Select 1
    soup = BeautifulSoup(await page.content(), 'html.parser')
    tabla = soup.select(".tableListingTable > tbody > tr")
    tabla.pop(0)
    for fila in tabla:
        id_vuelos.append(fila.select_one("td > a")['href'])
    await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select").value++')

    #Select 2
    soup = BeautifulSoup(await page.content(), 'html.parser')
    tabla = soup.select(".tableListingTable > tbody > tr")
    tabla.pop(0)
    for fila in tabla:
        id_vuelos.append(fila.select_one("td > a")['href'])
    await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select").value++')
    
    #Select 3
    soup = BeautifulSoup(await page.content(), 'html.parser')
    tabla = soup.select(".tableListingTable > tbody > tr")
    tabla.pop(0)
    for fila in tabla:
        id_vuelos.append(fila.select_one("td > a")['href'])
    await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select").value++')
    
    #Select 4
    soup = BeautifulSoup(await page.content(), 'html.parser')
    tabla = soup.select(".tableListingTable > tbody > tr")
    tabla.pop(0)
    for fila in tabla:
        id_vuelos.append(fila.select_one("td > a")['href'])
    await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select").value++')
    
    #Select 5
    soup = BeautifulSoup(await page.content(), 'html.parser')
    tabla = soup.select(".tableListingTable > tbody > tr")
    tabla.pop(0)
    for fila in tabla:
        id_vuelos.append(fila.select_one("td > a")['href'])
    await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select").value++')
    
    #Select 6
    soup = BeautifulSoup(await page.content(), 'html.parser')
    tabla = soup.select(".tableListingTable > tbody > tr")
    tabla.pop(0)
    for fila in tabla:
        id_vuelos.append(fila.select_one("td > a")['href'])
    await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select").value++')

    #Select 7
    soup = BeautifulSoup(await page.content(), 'html.parser')
    tabla = soup.select(".tableListingTable > tbody > tr")
    tabla.pop(0)
    for fila in tabla:
        id_vuelos.append(fila.select_one("td > a")['href'])
    await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select").value++')
    
    #Select 8
    soup = BeautifulSoup(await page.content(), 'html.parser')
    tabla = soup.select(".tableListingTable > tbody > tr")
    tabla.pop(0)
    for fila in tabla:
        id_vuelos.append(fila.select_one("td > a")['href'])
    await page.evaluate('() => document.querySelector("#flightStatusByRouteForm > select").value++')

    print(id_vuelos)
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
