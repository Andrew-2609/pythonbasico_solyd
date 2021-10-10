from apikey import ApiKey
from twitter import Twitter

if __name__ == '__main__':
    api_key = ApiKey.return_api_key_file()
    consumer_key = api_key.get("consumer_key")
    consumer_secret = api_key.get("consumer_secret")
    access_token = api_key.get("access_token")
    access_token_secret = api_key.get("access_token_secret")

    twitter = Twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    print(twitter.search_tweets("#nba", "de"))
