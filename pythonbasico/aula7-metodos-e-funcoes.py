def retorna_maior_valor_da_colecao(colecao):
    if type(colecao) is not dict:
        maior = colecao[0]
        for item in colecao:
            if item > maior:
                maior = item

        return maior
    else:
        return "Erro: Dicionários não são aceitos."


def retorna_menor_valor_da_colecao(colecao):
    if type(colecao) is not dict:
        menor = colecao[0]
        for item in colecao:
            if item < menor:
                menor = item

        return menor
    else:
        return "Erro: Dicionários não são aceitos."


print("### Início do programa ###\n")

lista = [1, 2, 5, 4, 3, 2, -8, 5]
tupla = (1, 2, 5, 4, 3, 2, -8, 5)
dicionario = {"numeros": [1, 2, 5, 4, 3, 2, -8, 5]}

print("## Lista de maiores números ##\n")
print("## Maior número da lista:", retorna_maior_valor_da_colecao(lista))
print("## Maior número da tupla:", retorna_maior_valor_da_colecao(tupla))
print("## Maior número do dicionario:", retorna_maior_valor_da_colecao(dicionario))

print("\n## Lista de menores números ##\n")
print("## Menor número da lista:", retorna_menor_valor_da_colecao(lista))
print("## Menor número da tupla:", retorna_menor_valor_da_colecao(tupla))
print("## Menor número do dicionario:", retorna_menor_valor_da_colecao(dicionario))

print("\n# Fim #")
