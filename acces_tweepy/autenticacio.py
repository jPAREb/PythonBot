import tweepy
from acces_tweepy.dades import credencials

auth = tweepy.OAuthHandler(credencials.api_key, credencials.api_key_secret)
auth.set_access_token(credencials.access_token, credencials.access_token_secret)
api = tweepy.API(auth)
