from flask import Flask, jsonify, request, abort
from textblob import TextBlob
from flask_cors import CORS, cross_origin
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


app=Flask(__name__)
CORS(app)
@cross_origin()

@app.route('/vader_texto', methods=['POST'])
def vader_texto():
    texto = request.json['texto']
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

if __name__ == '__main__':
    app.run(debug = True)
