from flask import Flask
import requests
# import dotenv
# import os
import json

app = Flask (__name__)

# Obtener la clave de la API.
# dotenv.load_dotenv ()
# apiKey = os.environ["RAPIDAPI_API_KEY"]

@app.route ("/")
def llamadaAPI ():
    # URL de la API.
    url = "https://hargrimm-wikihow-v1.p.rapidapi.com/steps"

    # Numero de pasos a obtener.
    querystring = {"count":"5"}

    # Headers de la peticion.
    headers = {
        "X-RapidAPI-Key": "906d5f12b4mshdf7dae85990c1b1p12b97fjsnb6fec604a413",
        "X-RapidAPI-Host": "hargrimm-wikihow-v1.p.rapidapi.com"
    }

    # Peticion a la API.
    response = requests.request("GET", url, headers=headers, params=querystring)
    respuestaJSON = response.text

    # Formateamos el JSON a un diccionario de Python.
    datos = json.loads (respuestaJSON)

    return f"<div align='left'><h1>Cinco pasos aleatorios de tutoriales de WikiHow</h1><br><ol><li>{datos['1']}</li><li>{datos['2']}</li><li>{datos['3']}</li><li>{datos['4']}</li><li>{datos['5']}</li></ol></div>"


app.run (port=5000, host="0.0.0.0")
