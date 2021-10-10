import oauth2
import json
import pprint


def realizar_autorizacao_retornar_client():
    try:
        api_key = json.load(open("apiKey.json"))
    except Exception as err:
        print("Ocorreu um erro ao abrir o arquivo:", err)
    else:
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

    corpo_resposta = res_client.request(f"{base_url}?q={palavra_chave}")[1]
    corpo_decodificado = corpo_resposta.decode()
    corpo_dict = json.loads(corpo_decodificado)
    return corpo_dict


if __name__ == '__main__':
    pprint.pprint(retornar_corpo_de_tweets("brasil"))
