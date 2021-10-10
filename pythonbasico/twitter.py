import oauth2


class Twitter:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.token = oauth2.Token(access_token, access_token_secret)
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.client = oauth2.Client(self.consumer, self.token)
