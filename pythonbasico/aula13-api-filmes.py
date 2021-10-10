import requests
import json
from apikey import ApiKey

api_key = ApiKey.return_api_key_file().get("api-filmes")


def retornar_dados_do_filme(titulo):
    try:
        req = requests.get(f"https://www.omdbapi.com/?t={titulo}&apikey={api_key}&type=movie")
        dict_filme = json.loads(req.text)
        return dict_filme
    except Exception as err:
        print("Connection error:", err)
        exit()


def retornar_lista_de_filmes(titulo):
    try:
        req = requests.get(f"https://www.omdbapi.com/?s={titulo}&apikey={api_key}&type=movie")
        dict_filme = json.loads(req.text)
        return dict_filme['Search']
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


def printar_dados_dos_filmes_na_lista(lista):
    print("## Imprimindo lista de filmes da primeira página:\n")

    for f in lista:
        print("Título:", f['Title'])
        print("Ano:", f['Year'])
        print("")

    print("## Fim da lista :)")


def selecionar_e_detalhar_filme():
    sair = False
    while not sair:
        opcao = input("Escreva o nome de um filme para retornar seus dados, ou SAIR para sair do programa: ")

        if opcao == "SAIR":
            print("Saindo...")
            sair = True
        else:
            filme_selecionado = retornar_dados_do_filme(opcao)
            printar_resumo_do_filme(filme_selecionado)


def pesquisar_lista_de_filmes_por_titulo():
    pesquisa = input("Pesquisar filmes com a palavra-chave: ")
    print("\n")
    lista_de_filmes = retornar_lista_de_filmes(pesquisa)
    printar_dados_dos_filmes_na_lista(lista_de_filmes)


if __name__ == '__main__':
    pesquisar_lista_de_filmes_por_titulo()
