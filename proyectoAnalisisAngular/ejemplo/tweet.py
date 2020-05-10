# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:29:43 2020

@author: camii
"""
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 

consumer_key = 'Y11e8yrSe2s6PsA0K6bX5GlTk'
consumer_secret = 'ld3Xu6h8JMDs9fHF33is95iHG5imJkqDBEaQBbeiWTpqdshEG0'
access_token = '805623734-svhgkst8CoLqR44X5Xmxuxdh8Lw5dMEgrM8zm9XR'
access_token_secret = 'AWM4LzNZICFq1e6MFwsLZnaLQpDRHN4rIjreleYptwC0C'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text,'...\n')

# Get the User object for twitter...
user = api.get_user('twitter')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)