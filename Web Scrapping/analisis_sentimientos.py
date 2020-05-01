from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def vader_texto(texto):
    blob = TextBlob(texto)
    lanDet = blob.detect_language()
    if(lanDet != 'en'):
        lan = blob.translate(to = 'en')
    else:
        lan = blob
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(lan)
    compound = score['compound']
    neg = score['neg']*100
    pos = score['pos']*100
    neu = score['neu']*100
    if score['compound'] >= 0.05 : 
        conclu = "Positivo"
    elif score['compound'] <= - 0.05 : 
        conclu = "Negativo"
    else : 
        conclu = "Neutral"
    
    return ({'idioma': lanDet, 'texto' : str(lan),'compound': compound ,'%neg': neg, '%pos': pos, '%neu': neu, 'conclusion': conclu})   

