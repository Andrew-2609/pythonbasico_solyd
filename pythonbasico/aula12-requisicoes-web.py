import datetime

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


def requisicao_get(endereco, cabecalhos=None, cookies=None):
    requisicao = None

    try:
        requisicao = requests.get(endereco, headers=cabecalhos, cookies=cookies)
        return requisicao.text
    except Exception as err:
        print(f"Não foi possível realizar a requisição para {requisicao}. Erro: {err}")


def requisicao_post(endereco, dados, cabecalhos=None, cookies=None):
    requisicao = None

    try:
        requisicao = requests.post(endereco, data=dados, headers=cabecalhos, cookies=cookies)
        return requisicao.text
    except Exception as err:
        print(f"Não foi possível realizar a requisição para {requisicao}. Erro: {err}")


if __name__ == '__main__':
    meus_cabecalhos = {"user-agent": "Windows 15"}
    meus_cookies = {"ultima-visita": str(datetime.datetime.now())}
    endereco_requisicao = input("Digite um endereço para fazer as requisições: ")

    usuario = input("Digite um usuário para a requisição POST: ")
    senha = input("Digite uma senha para fazer a requisição POST: ")

    meus_dados = {
        "usuario": usuario,
        "senha": senha
    }

    resposta_get = requisicao_get(endereco_requisicao, meus_cabecalhos, meus_cookies)
    resposta_post = requisicao_post(endereco_requisicao, meus_dados, meus_cabecalhos)

    print("\n### RESPOSTA GET ###")
    print(resposta_get)

    print("\n### RESPOSTA POST ###")
    print(resposta_post)

    print("\n", "#" * 7, "Fim da execução", "#" * 7)
