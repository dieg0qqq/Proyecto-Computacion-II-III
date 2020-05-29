import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

def entrenamiento():
    

    ruta='Web Scrapping\\vuelos_tiempo.csv'

    csv = pd.read_csv(ruta, sep=';')

    print('conexion con MySQL')
    json = requests.get('http://127.0.0.1:8000/api/prediccion').json()

    # print(json)

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
        print(horaProgramada)
        hora_programada.append(horaProgramada)

        # coger solo la identificacion de la aerolinea
        codigo_aerolinea = json[i]['IdVuelo'].split(" ")[0]
        print(codigo_aerolinea)
        cd_aero.append(codigo_aerolinea)

        # crear columna hora cambiar : por un . del vuelo
        horaClima = json[i]['hora'].replace(':', '.')
        print(horaClima)
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

        if (json[i]['HoraEstOrigen'] != "--" and horaProgramada != "--"):
            print("resta")
            resta = float(horaProgramada) - float(json[i]['HoraEstOrigen'][0:6].replace(':', '.'))
            if(resta < 0):
                retraso = "Si"
            else:
                retraso = "No"
            print(retraso)
        else:
            print(json[i]['Estado1'])
            estado1 = json[i]['Estado1']
            estado2 = json[i]['Estado2']
            if (estado2 == "On time"):
                retraso = "No"
            else:
                retraso = "Si"

        arrayRetraso.append(retraso)

        print("-----------------------------------------------")

    dictionario = {
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

    datosNuevos = pd.DataFrame(dictionario)

    tabla = csv.append(datosNuevos, ignore_index=True)

    print(tabla)

    columnas_texto = ['retraso', 'id_vuelo', 'destino', 'codigo_aerolinea']

    diccionario = {}

    #for: en cada columna de texto miramos los datos que hay que no se repiten
    for columna in columnas_texto:
        conjunto = set(tabla[columna])
        diccionario[columna] = {}  #diccionario dentro de diccionario diccionario:{'rertaso': {'si':1, 'no':0}, ...}
        
        #Se le da un valor numerico a cada categoria en la columna ej: diccionario[retraso][si]=1, diccionario[retraso][no]=0
        i=1
        for categoria in conjunto:
            diccionario[columna][categoria] = i
            i=i+1
        
        #Sustituye la categoria por su valor numerico
        for i in range(len(tabla[columna])):
            tabla[columna][i] = diccionario[columna][tabla[columna][i]]
            
        #Cambia el tipo del dato de objeto a int
        tabla[columna] = tabla[columna].astype('int32')

    print(tabla)
    print("-------------------------------")
    X = tabla.drop('retraso',axis=1)
    y = tabla['retraso']
    contador_ejemplares = len(tabla[columna])
    print(contador_ejemplares)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    #Calcula del clasificador
    clasificador = KNeighborsClassifier(n_neighbors=5)
    # clasificador = KNeighborsClassifier(n_neighbors=1)
    clasificador.fit(X_train, y_train)
    print(clasificador)

    #Evalucacion del modelo
    y_pred = clasificador.predict(X_test)

    print('--------------------------------------------')
    print(classification_report(y_test, y_pred))
    print('--------------------------------------------')
    matriz2 = confusion_matrix(y_test, y_pred).sum(axis=0)
    matriz3 = confusion_matrix(y_test, y_pred).sum(axis=1)
    valorDivisionE = matriz2[1]
    valorDivisionR = matriz3[1]
    valorD = confusion_matrix(y_test, y_pred)[1][1]
    valorA = confusion_matrix(y_test, y_pred)[0][0]
    exactitud = valorD / valorDivisionE
    recall = valorD / valorDivisionR
    valorDivisionP = sum(matriz2)
    precision = (valorD + valorA) / valorDivisionP
    print('--------------------------------------------')

    return({'clasificador': clasificador, 'diccionario': diccionario, 
        'exactitud':exactitud, 'recall': recall, 'precision': precision, 
        'contadorEjemplo': contador_ejemplares})


if __name__ == "__main__":
    entrenamiento = entrenamiento()