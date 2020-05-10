from textblob import TextBlob
import textblob
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# print("coge solos los sustantivos")

# blob = TextBlob("Analytics Vidhya is a great platform to learn data science.")
# for np in blob.noun_phrases:
#   print (np)
# print("------------------------- \n tipo de palabra")
# for words, tag in blob.tags:
#   print (words, tag)
# print("-------------------------\n singulariza los sustantivos en caso de que esten en plural \n devuelve el sustantivo raiz de la palabra")
# blob1 = TextBlob("Analytics Vidhya is a great platforms to learn data science. \n It helps community through blogs, hackathons, discussions,etc.")
# print (blob1.sentences[0].words[8])
# print (blob1.sentences[0].words[8].singularize())
# print(blob1.sentences[1].words[1].lemmatize())#si colocas algo entre los paréntesis te los lematiza con lo que pongas

# print("-------------------------")

# for ngram in blob1.ngrams(2):
#     print (ngram)
# print("-------------------------")
    
# print (blob1)
# sent = blob1.sentiment
# print(sent)

# print("------------------- \n texto largo")
# blob = TextBlob('Analytics Vidhya is a thriving community for data driven industry. This platform allows \
# people to know more about analytics from its articles, Q&A forum, and learning paths. Also, we help \
# professionals & amateurs to sharpen their skillsets by providing a platform to participate in Hackathons.')

# #traducir
# blob4 = TextBlob("Produkt sa mi veľmi páčil a prišiel včas")
# lan = blob4.translate(to ='en')
# print(lan)
# print("---------------CLASIFICADOR------------------")

# training = [
# ('Tom Holland is a awesome spiderman.','pos'),
# ('a terrible Javert (Russell Crowe) ruined Les Miserables for me...','neg'),
# ('The Dark Knight Rises is the greatest superhero movie ever!','pos'),
# ('Fantastic Four should have never been made.','neg'),
# ('Wes Anderson is my favorite director!','pos'),
# ('Captain America 2 is pretty awesome.','pos'),
# ('Let\s pretend "Batman and Robin" never happened..','neg'),
# ]
# testing = [
# ('Superman was never an interesting character.'),
# ('Fantastic Mr Fox is an awesome film!'),
# ('Dragonball Evolution is simply terrible!!')
# ]

# classifier = textblob.WekaClassifier(training)
# print (classifier.accuracy(testing))
# classifier.show_informative_features(5)

# cla = TextBlob('the weather is terrible!', classifier=classifier)

# print (cla.classify())

# training = [
#     (dict(a=1,b=1,c=1), 'x'),
#     (dict(a=1,b=1,c=1), 'x'),
#     (dict(a=1,b=1,c=0), 'y'),
#     (dict(a=0,b=1,c=1), 'x'),
#     (dict(a=0,b=1,c=1), 'y'),
#     (dict(a=0,b=0,c=1), 'y'),
#     (dict(a=0,b=1,c=0), 'x'),
#     (dict(a=0,b=0,c=0), 'x'),
#     (dict(a=0,b=1,c=1), 'y'),
#     ]
# testing = [
#     (dict(a=1,b=0,c=1)), # unseen
#     (dict(a=1,b=0,c=0)), # unseen
#     (dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
#     (dict(a=0,b=1,c=0)), # seen 1 time, label=x
# ]

# classifier = nltk.classify.NaiveBayesClassifier.train(training)
# sorted(classifier.labels())
# classifier.classify_many(testing)
# for pdist in classifier.prob_classify_many(testing):
#     print('%.4f %.4f' % (pdist.prob('x'), pdist.prob('y')))
# classifier.show_most_informative_features()

analyser = SentimentIntensityAnalyzer()
sentence = TextBlob("Das Produkt hat mir sehr gut gefallen und es ist pünktlich angekommen")
# lan = str(sentence.translate(to = 'en'))
# oracion=TextBlob("Hi, everyone!")
lan1 = sentence.translate(to = 'en')
lanDete = sentence.detect_language()
print (lanDete)
# sent = lan1.sentiment

score = analyser.polarity_scores(lan1)

print(score)

print(lan1)
print("% neg: ", score['neg']*100)
print("% pos: ", score['pos']*100)
print("% neu: ", score['neu']*100)

if score['compound'] >= 0.05 : 
        print("Positive") 
elif score['compound'] <= - 0.05 : 
    print("Negative") 
else : 
    print("Neutral") 

print("------------------------")
# print(sent)