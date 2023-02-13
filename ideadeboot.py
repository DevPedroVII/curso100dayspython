import tweepy
import random

consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

responses = ["Resposta 1", "Resposta 2", "Resposta 3", "Resposta 4", "Resposta 5"]

mentions = api.mentions_timeline()
for mention in mentions:

   if not mention.favorited:
        # Marque o tweet como favorito
        mention.favorite()
        # Gere uma resposta aleatória
        response = random.choice(responses)
        # Responda ao tweet
        api.update_status(f"@{mention.user.screen_name} {response}", mention.id)

