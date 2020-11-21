import tweepy
from acces_tweepy.autenticacio import api

espanya = 23424950
barcelona = 753692
tendencies = 2*[50*['0']]
def tendencies_espanya_barcelona (zona):
    trends = api.trends_place(zona)
    
    for value in trends: 
        i = 0
        for trend in value['trends']:
            if (zona == 23424950):
                tendencies[0][i] = trend['name']
            else:
                tendencies[1][i] = trend['name']
            i = i +1
             

def tendenciesf(zona):
    if (zona == "BCN"):
        tendencies_espanya_barcelona(753692)
    elif (zona == "ES"):
        tendencies_espanya_barcelona(23424950)
    
    
    return tendencies
