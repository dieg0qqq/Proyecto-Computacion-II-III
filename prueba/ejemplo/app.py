from flask import Flask, jsonify, request, abort
from textblob import TextBlob



app=Flask(__name__)

actividades=[
	{'id' :1,
	'titulo': u'primero',
	},
	{'id' :2,
	'titulo': u'Produkt sa mi veľmi páčil a prišiel včas',
	}
]

@app.route('/index', methods=['GET'])
def index():
    return jsonify({'resultado' : 'Hola Mundo'})

@app.route('/actividades' , methods=['GET'])
def get_actividades():
	return jsonify({'actividades': actividades})

@app.route('/actividades/<int:id>' , methods=['GET'])
def get_actividad(id):
	actividad=list(filter(lambda t: t['id'] == id, actividades))
	if len(actividad) == 0:
		abort(404)
	return jsonify ({'actividades': actividad[0]})

@app.route('/actividades' , methods=['POST'])
def create_actividad():
	if not request.json or not 'titulo' in request.json:
		abort(400)
	actividad={
		'id' : actividades[-1]['id'] + 1,
		'titulo' : request.json ['titulo']
	}
	actividades.append(actividad)
	return jsonify({'actividades' : actividad}), 201

@app.route('/actividades/<int:id>' , methods=['DELETE'])
def delete_actividad(id):
	actividad=list(filter(lambda t: t['id'] == id, actividades))
	if len(actividad) == 0:
		abort(404)
	actividades.remove(actividad[id])
	return jsonify({'result': True})

@app.route('/analisis/<int:id>' , methods=['GET'])
def analisis(id):
    actividad=list(filter(lambda t: t['id'] == id, actividades))
    if len(actividad) == 0:
        abort(404)
    blob = TextBlob(actividad[0]['titulo'])
    lan = blob.translate(to ='en')
    print(lan)
    sent = lan.sentiment
    return jsonify({'text': str(lan), "polarity":sent.polarity, "subjetivity": sent.subjectivity})
	
@app.route('/ana_texto', methods=['POST'])
def ana_texto():
	texto = request.json['texto']
	blob = TextBlob(texto)
	lan = blob.translate(to='es')
	print(lan)
	sent = lan.sentiment
	return jsonify({"tx": str(lan), "polarity":sent.polarity, "subjetivity": sent.subjectivity})

    

if __name__ == '__main__':
    app.run(debug = True)
