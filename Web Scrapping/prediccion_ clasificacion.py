import prediccion_entrenamiento as entrenamiento
import requests
import pandas as pd

faseEntrenamiento = entrenamiento.entrenamiento()

diccionario = faseEntrenamiento['diccionario']
clasificador = faseEntrenamiento['clasificador']

print('conexion con MySQL')
json = requests.get('http://127.0.0.1:8000/api/clasificador').json()

print(json)

destino = []
cd_aero = []
id_vuelo = []
hora_programada = []
arrayRetraso = []
anio = []
mes = []
dia = []
h_clima = []
grados = []
velo_viento=[]
rachas = []
lluvia = []
nubes=[]
humedad=[]
presion=[]

for i in range(len(json)):
    # crear columnas anio, mes, dia
    fecha_anio = json[i]['fecha'].split('-')[0]
    fecha_mes = json[i]['fecha'].split('-')[1]
    fecha_dia = json[i]['fecha'].split('-')[2]

    anio.append(fecha_anio)
    mes.append(fecha_mes)
    dia.append(fecha_dia)

    # crear columna hora_programada cambiar : por un . del vuelo
    horaProgramada = json[i]['HoraProgOrigen'][0:6].replace(':', '.')
    # print(horaProgramada)
    hora_programada.append(horaProgramada)

    # coger solo la identificacion de la aerolinea
    codigo_aerolinea = json[i]['IdVuelo'].split(" ")[0]
    # print(codigo_aerolinea)
    cd_aero.append(codigo_aerolinea)

    # crear columna hora cambiar : por un . del vuelo
    horaClima = json[i]['hora'].replace(':', '.')
    # print(horaClima)
    h_clima.append(horaClima)

    destino.append(json[i]['Destino'])
    id_vuelo.append(json[i]['IdVuelo'])
    grados.append(json[i]['temperatura'])
    velo_viento.append(json[i]['viento'])
    rachas.append(json[i]['rafagas'])
    lluvia.append(json[i]['lluvia'])
    nubes.append(json[i]['nubes'])
    humedad.append(json[i]['humedad'])
    presion.append(json[i]['presion'])
    arrayRetraso.append("")

dicc = {
   "destino" : destino,
    "codigo_aerolinea": cd_aero,
    "id_vuelo": id_vuelo,
    "hora_programada": hora_programada,
    "retraso": arrayRetraso,
    "anio": anio,
    "mes": mes,
    "dia": dia,
    "hora": h_clima,
    "grados": grados,
    "velocidad_viento": velo_viento,
    "rachas_viento": rachas,
    "lluvia": lluvia,
    "nubes": nubes,
    "humedad": humedad,
    "presion": presion 
}

tabla = pd.DataFrame(dicc)

print(tabla)

tabla_copia = tabla.copy()

columnas_texto = ['retraso', 'id_vuelo', 'destino', 'codigo_aerolinea']

for columna in columnas_texto:
#Sustituye la categoria por su valor numerico
    for i in range(len(tabla[columna])):
        texto = tabla[columna][i]
        if texto in diccionario[columna].keys():
            tabla[columna][i] = diccionario[columna][texto]
        else:
            tabla[columna][i] = 0   #texto no esta en el diccionario -> 0

tabla[columna].astype('int32')

X = tabla.drop('retraso',axis=1)
y_pred = clasificador.predict(X)

print(y_pred)

data = {}
data['prediccion'] = []

for i in range(len(y_pred)):
    
    if (y_pred[i] == diccionario['retraso']['Si']):
        c3 = "si"
        retraso = 'Si'
    elif (y_pred[i] == diccionario['retraso']['No']):
        c3 = "no"
        retraso = 'No'
    else:
        c3="??"
        retraso = '??'
    
    fecha= tabla_copia['anio'][i]+"-"+tabla_copia['mes'][i]+"-"+tabla_copia['dia'][i]

    data['prediccion'].append({
        'identificador_vuelo' :  json[i]['id'],
        'idVuelo' : tabla_copia['id_vuelo'][i],
        'origen': json[i]['Origen'],
        'destino': tabla_copia['destino'][i],
        'fecha': fecha,
        'hora_programada': str(tabla_copia['hora_programada'][i]).replace(".",":"),
        'retraso': retraso
    })
print(data)

requests.post('http://127.0.0.1:8000/api/prediccion', json= data )

