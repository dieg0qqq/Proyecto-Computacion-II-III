from datetime import date
from twython import Twython
import requests
import analisis_sentimientos

data = {}
data['opiniones'] = []

consumer_key = 'Y11e8yrSe2s6PsA0K6bX5GlTk'
consumer_secret = 'ld3Xu6h8JMDs9fHF33is95iHG5imJkqDBEaQBbeiWTpqdshEG0'
access_token = '805623734-svhgkst8CoLqR44X5Xmxuxdh8Lw5dMEgrM8zm9XR'
access_token_secret = 'AWM4LzNZICFq1e6MFwsLZnaLQpDRHN4rIjreleYptwC0C'

twitter = Twython(consumer_key, consumer_secret,
                  access_token, access_token_secret)

aerolineas = ['Iberia', 'Ryanair',
              'LATAM', 'AirEuropa', 'Avianca']

for j in range(len(aerolineas)):
    query = aerolineas[j] + " cliente -filter:retweets AND -filter:replies"
    search = twitter.search(q=query, tweet_mode='extended')
    it = 0
    for se in search['statuses']:
        print(it, ": ", se['full_text'])
        analisis = analisis_sentimientos.vader_texto(se['full_text'])
        print(analisis['conclusion'])
        data['opiniones'].append({
            'nombreAerolinea': aerolineas[j],
            'comentario': se['full_text'],
            'analisis' : analisis['conclusion']
        })
        it = it +1

# print(data)
requests.post('http://127.0.0.1:8000/api/comentarios/twitter',json=data)

