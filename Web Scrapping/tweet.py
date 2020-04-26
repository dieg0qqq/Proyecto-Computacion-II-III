from datetime import date
from twython import Twython
# import sim

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
    query = aerolineas[j] + " atencion al cliente"
    # search = api.user_timeline(screen_name = aerolineas[j], count = 10)
    search = twitter.search(q=query, tweet_mode='extended')
    for se in search['statuses']:
        data['opiniones'].append({
            'nombreAerolinea': aerolineas[j],
            'comentario': se['full_text']
        })
print(data)

