import tweepy
from acces_tweepy import api

def missatge (text,resposta,rec):
    
    array_text = []
    text_separacio = ''
    i = 0
    for char in text:
        if(i<=270):
            text_separacio += char
        else:
            i = 0
            text_separacio += '¡'
            text_separacio += char
        i = i +1
    array_text = []
    posicions_array = 0
    if('¡' in text_separacio):
        array_text = text_separacio.split('¡')
        posicions_array = len(array_text)
    

    if(resposta):
        id_tweet = api.update_status(text,resposta)
        ret = "Tweet publicat: "
        ret += text
        if (rec == True):
            return id_tweet.id_str
        else:
            return ret
                 
    elif (posicions_array>0):
        for tweet in array_text:    
            resposta = missatge(tweet,resposta,True)
        ret = "Tweets publicats: "
        ret += text
        return ret

    else:
        id_tweet = api.update_status(text)
        ret = "Tweet publicat: "
        ret += text
        if(rec == True):
            return id_tweet.id_str
        else:
            return ret

