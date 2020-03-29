# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:29:43 2020

@author: camii
"""
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import json

consumer_key = 'Y11e8yrSe2s6PsA0K6bX5GlTk'
consumer_secret = 'ld3Xu6h8JMDs9fHF33is95iHG5imJkqDBEaQBbeiWTpqdshEG0'
access_token = '805623734-svhgkst8CoLqR44X5Xmxuxdh8Lw5dMEgrM8zm9XR'
access_token_secret = 'AWM4LzNZICFq1e6MFwsLZnaLQpDRHN4rIjreleYptwC0C'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
aerolineas = ['Iberia','Ryanair_ES','LATAM_ES', 'AirEuropa', 'AviancaEuropa']

for j in range(len(aerolineas)):
    it = 1
    search = api.user_timeline(screen_name = aerolineas[j], count = 10) 
    print("-------------------------------------")
    print(aerolineas[j])
    for i in search:
        print(it,": ... + ", i.text)
        it = it+1
    print("-------------------------------------")
    