import oauth2
import json

try:
    apiKey = json.load(open("apiKey.json"))
except Exception as err:
    print("Ocorreu um erro ao abrir o arquivo:", err)
else:
    base_url = "https://api.twitter.com/1.1/search/tweets.json"
    consumer_key = apiKey['consumer_key']
    consumer_secret = apiKey['consumer_secret']
    access_token = apiKey['access_token']
    access_token_secret = apiKey['access_token_secret']

    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    token = oauth2.Token(access_token, access_token_secret)

    client = oauth2.Client(consumer, token)

    req = client.request(f"{base_url}?brasil")
    print(req)
