from ichrome import AsyncChromeDaemon, AsyncChrome
import asyncio

async def main():
    aerolinea = 'Arkia' #El parámetro
    opiniones = []
    hook_comments_js = '''
        function(){  
            for (const readMore of document.getElementsByClassName("location-review-review-list-parts-ExpandableReview__cta--2mR2g"))
                readMore.click()
            let opiniones = []
            for (let x = 0; x < 5; x++) {
                opiniones.push({
                    titulo: document.getElementsByClassName("location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT")[x].children[0].children[0].textContent,
                    cuerpo: document.getElementsByClassName("location-review-review-list-parts-ExpandableReview__reviewText--gOmRC")[x].children[0].textContent,
                    nota: document.getElementsByClassName("location-review-review-list-parts-RatingLine__bubbles--GcJvM")[x].getElementsByClassName("ui_bubble_rating")[0].classList[1][7]
                })
            }
            return opiniones;
        }()
        '''
    async with AsyncChromeDaemon(headless=True):
        async with AsyncChrome() as chrome:
            tab = await chrome.new_tab(url="https://www.tripadvisor.es/Search?q="+aerolinea)
            async with tab():
                await asyncio.sleep(10)
                await tab.set_url("https://www.tripadvisor.es"+await tab.get_value('''document.querySelector(".result-title").onclick.toString().split("'")[3]'''))
                for i in range(0, 5):
                    await asyncio.sleep(5)
                    await tab.wait_loading(2)
                    opiniones.extend(await tab.get_value(hook_comments_js))
                    await tab.js(f'document.querySelector(".pageNumbers").children[{i+1}].click()')
                    await asyncio.sleep(1)
                await tab.close()
            await chrome.close_browser()
    print(opiniones) #Aquí ya está el JSON final, que es 'opiniones'

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())