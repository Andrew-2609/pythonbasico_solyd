from twitter import Twitter
import json

if __name__ == '__main__':
    api_key = None
    try:
        api_key = json.load(open("apiKey.json"))
    except Exception as err:
        print("Ocorreu um erro ao abrir o arquivo:", err)
        exit()

    consumer_key = api_key['consumer_key']
    consumer_secret = api_key['consumer_secret']
    access_token = api_key['access_token']
    access_token_secret = api_key['access_token_secret']

    twitter = Twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    print(twitter.search_tweets("#nba", "de"))
