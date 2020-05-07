from ichrome import AsyncChromeDaemon, AsyncChrome
import asyncio

async def main():
    aerolineas = ["ANA","ASL Airlines Belgium","Aeroflot","Aerolineas Argentinas","Aeromexico","Air Austral"] #Array de ejemplo de aerolíneas
    data={}
    data['comentarios'] = []
    hook_comments_js = '''
        function(){  
            for (const readMore of document.getElementsByClassName("location-review-review-list-parts-ExpandableReview__cta--2mR2g"))
                readMore.click()
            let opiniones = []
            for (let x = 0; x < 5; x++) {
                opiniones.push({
                    id_aerolinea: '',
                    cuerpo: document.getElementsByClassName("location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT")[x].children[0].children[0].textContent + " " + document.getElementsByClassName("location-review-review-list-parts-ExpandableReview__reviewText--gOmRC")[x].children[0].textContent,
                    valoracion: document.getElementsByClassName("location-review-review-list-parts-RatingLine__bubbles--GcJvM")[x].getElementsByClassName("ui_bubble_rating")[0].classList[1][7]
                })
            }
            return opiniones;
        }()
        '''
    async with AsyncChromeDaemon(headless=True):
        async with AsyncChrome() as chrome:
            for aero in aerolineas:
                working = True
                aerolinea = aero #El parámetro
                print(aero) #Para ir viendo por qué aerolínea va
                tab = await chrome.new_tab(url="https://www.tripadvisor.es/Search?q="+aero)
                async with tab():
                    await asyncio.sleep(3)
                    if(await tab.get_value('''document.querySelector(".result-title").onclick.toString()''') == None): #Caso de que no pueda encontrarse enlace a la aerolínea (por falta de resultados por ejemplo)
                        print("Error: Aerolínea no encontrada")
                        working = False
                    else:
                        await tab.set_url("https://www.tripadvisor.es"+await tab.get_value('''document.querySelector(".result-title").onclick.toString().split("'")[3]'''))
                        await asyncio.sleep(3)
                        await tab.wait_loading(2)
                        if(await tab.get_value(hook_comments_js) == None): #Caso de que falle en la primera página de comentarios (por falta de los mismos por ejemplo)
                            print("Error: Comentarios no encontrados")
                            working = False
                        i = 0
                        opiniones_aux = []
                        while(working == True and i < 5):
                            i = i+1
                            await asyncio.sleep(3)
                            await tab.wait_loading(2)
                            if(await tab.get_value(hook_comments_js) == None): #Caso de que falle en una página de comentarios (por falta de los mismos por ejemplo)
                                print("Error: Comentarios no encontrados")
                                working = False
                            else:
                                opiniones_aux.extend(await tab.get_value(hook_comments_js))
                                await tab.js(f'document.querySelector(".pageNumbers").children[{i+1}].click()')
                        for i in opiniones_aux:
                            i['id_aerolinea']=aerolinea
                        data['comentarios'].extend(opiniones_aux)
                print(len(data['comentarios'])) #Imprime el total de comentarios recogidos hasta el momento
            await chrome.close_browser()
    print(data) #Imprime todos los comentarios. Aquí tocaría el post.

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())