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
        req = requests.get(f"https://www.omdbapi.com/?t={titulo}&apikey={carregar_api_key()}&type=movie")
        dict_filme = json.loads(req.text)
        return dict_filme
    except Exception as err:
        print("Connection error:", err)
        exit()


def printar_resumo_do_filme(filme):
    print("\n" + ("#" * 4))
    print("Título:", filme['Title'])
    print("Ano:", filme['Year'])
    print("Gênero:", filme['Genre'])
    print("Diretor:", filme['Director'])
    print("Atores:", filme['Actors'])
    print("Sinopse:", filme['Plot'])
    print(("#" * 4) + "\n")


sair = False
while not sair:
    opcao = input("Escreva o nome de um filme para retornar seus dados, ou SAIR para sair do programa: ")

    if opcao == "SAIR":
        print("Saindo...")
        sair = True
    else:
        filme_selecionado = retornar_dados_do_filme(opcao)
        printar_resumo_do_filme(filme_selecionado)
