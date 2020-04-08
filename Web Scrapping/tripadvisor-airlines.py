import asyncio
from pyppeteer import launch
from datetime import date
from pyppeteer_stealth import stealth

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await stealth(page)
    await page.goto('https://www.tripadvisor.es/Search?q=Iberia', {'waitUntil': 'networkidle2'}) #Se puede cambiar Iberia por cualquiera
    nextLink = await page.evaluate('''"https://www.tripadvisor.es"+document.querySelector(".result-title").onclick.toString().split("'")[3]''')
    await page.goto(nextLink, {'waitUntil': 'networkidle2'})
    nextLink = await page.evaluate('document.querySelector(".pageNumbers").children[1].href')
    hookComments = '''() => {
        let j = 0
        while (document.getElementsByClassName("location-review-review-list-parts-ExpandableReview__cta--2mR2g")[j])
            document.getElementsByClassName("location-review-review-list-parts-ExpandableReview__cta--2mR2g")[j++].click()
        let opiniones = []
        for (let x = 0; x < 5; x++) {
            opiniones.push({
                titulo: document.getElementsByClassName("location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT")[x].children[0].children[0].textContent,
                cuerpo: document.getElementsByClassName("location-review-review-list-parts-ExpandableReview__reviewText--gOmRC")[x].children[0].textContent,
                nota: document.getElementsByClassName("location-review-review-list-parts-RatingLine__bubbles--GcJvM")[x].getElementsByClassName("ui_bubble_rating")[0].classList[1][7]
            })
        }
        return opiniones;
    }'''
    opiniones = await page.evaluate(hookComments)
    await page.goto(nextLink, {'waitUntil': 'networkidle2'})
    nextLink = await page.evaluate('document.querySelector(".pageNumbers").children[2].href')
    opiniones.extend(await page.evaluate(hookComments))
    await page.goto(nextLink, {'waitUntil': 'networkidle2'})
    nextLink = await page.evaluate('document.querySelector(".pageNumbers").children[3].href')
    opiniones.extend(await page.evaluate(hookComments))
    await page.goto(nextLink, {'waitUntil': 'networkidle2'})
    nextLink = await page.evaluate('document.querySelector(".pageNumbers").children[4].href')
    opiniones.extend(await page.evaluate(hookComments))
    await browser.close()
    # print(opiniones)
    ruta_rel = "Web Scrapping\\Archivos JSON\\"
    dateStr = date.today().strftime("%Y-%m-%d")
    archivo = open(ruta_rel + "TripAdvisor" + dateStr+ ".json", "w", encoding="utf-8")
    archivo.write(str(opiniones)) 
    archivo.close()
    
asyncio.get_event_loop().run_until_complete(main())
