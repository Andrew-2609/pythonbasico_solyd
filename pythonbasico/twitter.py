import json
import urllib.parse

import oauth2


class Twitter:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.token = oauth2.Token(access_token, access_token_secret)
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.client = oauth2.Client(self.consumer, self.token)

    def tweet(self, mensagem):
        base_url = "https://api.twitter.com/1.1/statuses/update.json"
        mensagem = urllib.parse.quote(mensagem)

        corpo_resposta = self.client.request(f"{base_url}?status={mensagem}", method="POST")[1]
        corpo_decodificado = corpo_resposta.decode()
        corpo_dict = json.loads(corpo_decodificado)
        return corpo_dict

    def search_tweets(self, palavra_chave, idioma=' '):
        base_url = "https://api.twitter.com/1.1/search/tweets.json"

        palavra_chave = urllib.parse.quote(palavra_chave)

        corpo_resposta = self.client.request(f"{base_url}?q={palavra_chave}&lang={idioma}")[1]
        corpo_decodificado = corpo_resposta.decode()
        corpo_dict = json.loads(corpo_decodificado)
        return corpo_dict
