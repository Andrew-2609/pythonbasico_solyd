import requests
import json

base_url = "https://economia.awesomeapi.com.br/last"


def retornar_dados_da_conversao(moeda):
    try:
        req = requests.get(f"{base_url}/{moeda}")
        return json.loads(req.text)
    except Exception as err:
        print(f"Houve um erro na requisição: {err}")


def formatar_e_retornar_resposta(moedas, res):
    erro = False
    base_body = None
    try:
        base_body = res[moedas]
    except KeyError:
        erro = True

    print("\n###")
    if not erro:
        nome_origem = str(base_body['name']).split('/')[0]
        nome_conversao = str(base_body['name']).split('/')[1]
        valor_conversao = round(float(base_body['high']), 2)
        porcentagem_conversao = float(base_body['pctChange'])
        data_referencia = base_body['create_date']

        print("Moeda de origem:", nome_origem)
        print("Sendo convertida para:", nome_conversao)
        print(f"1 {nome_origem} vale aproximadamente {valor_conversao} {nome_conversao}")
        print(f"Taxa de variação: aproximadamente {porcentagem_conversao}%")
        print(f"Data de referência da conversão: {data_referencia}")
    else:
        print(f"Erro {res['status']}: {res['message']}")
    print("###\n")


def perguntar_qual_moeda_converter():
    print("Realizar conversão entre quais moedas? Utilize o padrão 'BRL', 'USD', etc.")
    moeda_origem = input("Converter de: ")
    moeda_convertida = input("para: ")
    conversao = retornar_dados_da_conversao(f"{moeda_origem}-{moeda_convertida}")
    formatar_e_retornar_resposta(moeda_origem + moeda_convertida, conversao)


if __name__ == '__main__':
    perguntar_qual_moeda_converter()
