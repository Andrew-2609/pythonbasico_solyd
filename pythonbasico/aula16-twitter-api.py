import json
import urllib.parse
from datetime import datetime

import oauth2

from apikey import ApiKey


def realizar_autorizacao_retornar_client():
    api_key = ApiKey.return_api_key_file()
    consumer_key = api_key['consumer_key']
    consumer_secret = api_key['consumer_secret']
    access_token = api_key['access_token']
    access_token_secret = api_key['access_token_secret']

    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    token = oauth2.Token(access_token, access_token_secret)

    client = oauth2.Client(consumer, token)
    return client


def retornar_corpo_de_tweets(palavra_chave):
    res_client = realizar_autorizacao_retornar_client()
    base_url = "https://api.twitter.com/1.1/search/tweets.json"

    palavra_chave = urllib.parse.quote(palavra_chave)

    corpo_resposta = res_client.request(f"{base_url}?q={palavra_chave}")[1]
    corpo_decodificado = corpo_resposta.decode()
    corpo_dict = json.loads(corpo_decodificado)
    return corpo_dict


def definir_query_e_retornar_tweets():
    query = input("Por favor, diga o que você deseja pesquisar no Twitter: ")
    resultados = retornar_corpo_de_tweets(query)['statuses']
    return resultados


def formatar_e_exibir_tweets(lista_tweets):
    print("\n### Resultados")
    for tweet in lista_tweets:
        print(f"----\nUsuário: @{tweet['user']['screen_name']}")
        print(f"\tTweet: {tweet['text']}\n")
    print("### Fim")


def formatar_data_novo_tweet(data):
    data_simplificada = str(data).split(" +")[0]
    formato_data_twitter = "%a %b %d %H:%M:%S"
    formato_data_convertido = f"%d/%m/{datetime.now().year} %H:%M:%S"

    data_convertida = datetime.strptime(data_simplificada, formato_data_twitter).strftime(formato_data_convertido)
    return data_convertida


def criar_novo_tweet(mensagem):
    res_client = realizar_autorizacao_retornar_client()
    base_url = "https://api.twitter.com/1.1/statuses/update.json"
    mensagem = urllib.parse.quote(mensagem)

    corpo_resposta = res_client.request(f"{base_url}?status={mensagem}", method="POST")[1]
    corpo_decodificado = corpo_resposta.decode()
    corpo_dict = json.loads(corpo_decodificado)

    if corpo_dict.get('created_at'):
        data_e_hora_tweet = formatar_data_novo_tweet(corpo_dict['created_at'])
        print("\n ### O tweet foi feito com sucesso. Segue abaixo:")
        print(f"\tUsuário: @{corpo_dict['user']['screen_name']}")
        print(f"\tTweet: {corpo_dict['text']}")
        print(f"\tData e hora (UTC): {data_e_hora_tweet}")
    else:
        print("\n ### Ocorreu um problema. Objeto retornado:")
        print(corpo_dict)
    print("###\n")


if __name__ == '__main__':
    print("Bem-vindo a minha implementação básica da Twitter API!")
    opcao = input("Escolha uma opção (0 - Pesquisar tweets | 1 - Criar novo tweet): ")

    if opcao == '0':
        tweets = definir_query_e_retornar_tweets()
        formatar_e_exibir_tweets(tweets)
    elif opcao == '1':
        msg = input("Digite uma mensagem para o seu tweet: ")
        criar_novo_tweet(msg)
    else:
        print("Opção inválida, encerrando o programa...")
