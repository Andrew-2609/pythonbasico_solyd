import requests


def clonar_pagina_principal():
    endereco = input("De qual site você deseja obter o clone da página inicial?\n")

    try:
        requisicao = requests.get(endereco)

        arquivo = open("../index.html", 'w')
        arquivo.write(requisicao.text)
        arquivo.close()

        print("O arquivo index.html pode ser encontrado na raiz desse projeto.")
    except Exception as err:
        print(f"Não foi possível fazer requisição no endereço {endereco}. Erro: {err}")
