import requests


def clone_index_page():
    endereco = input("De qual site você deseja obter o clone da página inicial?\n")

    try:
        requisicao = requests.get(endereco)

        file = open("../index.html", 'w')
        file.write(requisicao.text)
        file.close()

        print("O arquivo index.html pode ser encontrado na raiz desse projeto.")
    except Exception as err:
        print(f"Não foi possível fazer requisição no endereço {endereco}. Erro: {err}")
