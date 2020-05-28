import requests
import pandas as pd

print('conexion con MySQL')
json = requests.get('http://127.0.0.1:8000/api/prediccion')

tabla = pandas.DataFrame()