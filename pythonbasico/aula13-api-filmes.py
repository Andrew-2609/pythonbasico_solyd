import requests
import json


def carregar_api_key():
    try:
        api_key = open("apiKey.txt").read()
        return api_key
    except Exception as err:
        print("Couldn't read the file. Error:", err)
        exit()


def retornar_dados_do_filme(titulo):
    try:
        req = requests.get(f"https://www.omdbapi.com/?t={titulo}&apikey={carregar_api_key()}")
        return req
    except Exception as err:
        print("Connection error:", err)
        exit()


filme = input("De qual filme você deseja saber os dados? Informe: ")

dicionario = json.loads(retornar_dados_do_filme(filme).text)

print(dicionario)
