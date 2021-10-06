import re
import requests


def retorna_registros_por_padrao(padrao_regex, string_de_busca):
    print("# Procurando por padrão...")
    padroes = re.findall(padrao_regex, string_de_busca)
    if padroes:
        print("## Sucesso!\nRegistros encontrados:")
        return set(padroes)
    else:
        return "Esse padrão não foi encontrado dentro da String passada =(."


if __name__ == '__main__':
    meu_regex = r"[\w.-]+@[\w-]+\.[\w.-]+"
    requisicao_web = None
    try:
        requisicao_web = requests.get("https://www.loucosporcoxinha.com.br/contato/")
    except Exception as err:
        print(f"A requisição falhou. Erro: {err}")
        exit()

    registros = retorna_registros_por_padrao(meu_regex, requisicao_web.text)
    print(registros)
