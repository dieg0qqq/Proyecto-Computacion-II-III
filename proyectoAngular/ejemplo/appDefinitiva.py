# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 00:21:30 2020

@author: camii
"""
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analisis(texto):
    print(texto)
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(texto)
    print("Compound: ",score['compound'])
    print("% neg: ", score['neg']*100)
    print("% pos: ", score['pos']*100)
    print("% neu: ", score['neu']*100)
    print("------------------------")
    if score['compound'] >= 0.05 : 
        print("Positive") 
    elif score['compound'] <= - 0.05 : 
        print("Negative") 
    else : 
        print("Neutral") 




def main():
    sentence = TextBlob("Das Produkt hat mir sehr gut gefallen und es ist pünktlich angekommen")
    # sentence = TextBlob("Hi, everyone!")
    lanDet = sentence.detect_language()
    if(lanDet != 'en'):
        lan = sentence.translate(to='en')
        analisis(lan)
    else:
        analisis(sentence)
        
    

if __name__ == "__main__": 
	# calling main function 
	main()