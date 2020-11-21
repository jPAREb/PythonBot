from acces_tweepy.autenticacio import api
import tweepy
import time


def revisar_seguidors():
    seguidors = []
    for seguidor in api.followers("CatalanFlagUnic"):
        time.sleep(5)
        seguidors.append(seguidor.screen_name)
    return len(seguidors)
