from twython import Twython
import requests
import analisis_sentimientos

data = {}
data['opiniones'] = []

consumer_key = 'WinKm5pQsOCDXIeAulJzO16oN'
consumer_secret = 'ganVeYBL1hnH4Icth8ceWb0UUEfcNswgrcJONuoe1g8G9LtXKx'
access_token = '805623734-2k3zeIULrBolBTNIjXgZoHbxWZnNemCPz5TKWM8S'
access_token_secret = 'BvvkJSmEz4jRy294LIYDz2nGQGY15NOzer4ZhCCLji5Hq'

twitter = Twython(consumer_key, consumer_secret,
                  access_token, access_token_secret)
aerolineas = []
ruta_rel = "Web Scrapping\\Archivos_JSON\\"
archivo = open(ruta_rel + "Aerolineas" + ".txt","r", encoding="utf-8")

for line in archivo:
    lineas = archivo.readlines()
    for i in lineas:
        aero = i.split("\n")
        aerolineas.append(aero[0])

for j in range(len(aerolineas)):
    query = aerolineas[j] + " cliente -filter:retweets AND -filter:replies AND -filter:links"
    search = twitter.search(q=query, tweet_mode='extended', count="10")
    it = 0
    print(query)
    for se in search['statuses']:
        print(it, ": ", se['full_text'])
        # analisis = analisis_sentimientos.vader_texto(se['full_text'])
        # print(analisis['conclusion'])
        data['opiniones'].append({
            'nombreAerolinea': aerolineas[j],
            'comentario': se['full_text']
            # 'analisis' : analisis['conclusion']
        })
        it = it +1

print(data)
# requests.post('http://127.0.0.1:8000/api/comentarios/twitter',json=data)

