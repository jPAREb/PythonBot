import psycopg2
from postgres.p_connexio import conn
from datetime import datetime
from datetime import date


def afegir_usuari(id_usuari, nom):
    try:
        cur = conn.cursor()
        insert = "insert into usuaris values('"+str(id_usuari)+"', '" +str(nom)+"')"
        cur.execute(insert)
        conn.commit()
        ret = "Afegit l'usuari: "+str(nom)+" amb id: "+str(id_usuari)
        return ret
    except:
        conn.rollback()
        return "Ha hagut un error en afegir l'usuari"

def afegir_tweet(id_tweet, missatge):
    try:
        cur = conn.cursor()
        insert = "insert into tweets values('"+str(id_tweet)+"', '" +str(missatge)+"')"
        cur.execute(insert)
        conn.commit()
        ret = "Afegit el tweet: "+str(missatge)+" amb id: "+str(id_tweet)+", s'ha afegit a la base de dades"
        return ret
    except:
        conn.rollback()
        return "Ha hagut un error en afegir el tweet"

def tweet_normal(id_tweet, data, hora):
    try:
        cur = conn.cursor()
        insert = str('insert into "tweets normals" values (DEFAULT, ')+"'"+str(id_tweet)+"', '"+ str(data)+"', '"+ str(hora)+"')"
        cur.execute(insert)
        conn.commit()
        return "El tweet s'ha catalogat com normal"
    except:
        conn.rollback()
        return "Ha hagut un error en catalogar el tweet com a normal"

def tweet_usuaris(id_usuari,id_tweet, data, hora):
    try:
        cur = conn.cursor()
        insert = str('insert into "tweets usuaris" values (DEFAULT, ')+"'"+str(id_tweet)+"', '"+ str(id_usuari)+"', '"+ str(data)+"', '"+str(hora)+"')"
        cur.execute(insert)
        conn.commit()
        return "El tweet s'ha catalogat com usuari"
    except:
        conn.rollback()
        return "Ha hagut un error en catalogar el tweet com a usuari"

def tweet_resposta(id_usuari,id_tweet, data, hora):
    try:
        cur = conn.cursor()
        insert = str('insert into "tweets resposta" values (DEFAULT, ')+"'"+str(id_tweet)+"', '"+ str(id_usuari)+"', '"+ str(data)+"', '"+str(hora)+"')"
        cur.execute(insert)
        conn.commit()
        return "El tweet s'ha catalogat com una resposta"
    except:
        conn.rollback()
        return "Ha hagut un error en catalogar el tweet com una resposta"


def afegir_seguidor(id_usuari, data, hora):
    try:
        cur = conn.cursor()
        insert = str('insert into seguidors values (DEFAULT, ')+"'"+ str(id_usuari)+"', '"+ str(data)+"', '"+str(hora)+"')"
        cur.execute(insert)
        conn.commit()
        return "S'ha catalogat l'usuari com a seguidor"
    except:
        conn.rollback()
        return "Ha hagut un error en catalogar l'usuari com a seguidor"

def afegir_unfollow(id_usuari, data, hora):
    try:
        cur = conn.cursor()
        insert = str('insert into unfollow values (DEFAULT, ')+"'"+ str(id_usuari)+"', '"+ str(data)+"', '"+str(hora)+"')"
        cur.execute(insert)
        conn.commit()
        return "S'ha catalogat l'usuari com a unfollow"
    except:
        conn.rollback()
        return "Ha hagut un error en catalogar l'usuari com a unfollow"

def afegir_bloqueig(id_usuari, data, hora):
    try:
        cur = conn.cursor()
        insert = str('insert into "usuaris blocats" values (DEFAULT, ')+"'"+ str(id_usuari)+"', '"+ str(data)+"', '"+str(hora)+"')"
        cur.execute(insert)
        conn.commit()
        return "S'ha catalogat l'usuari com usuari blocat"
    except:
        conn.rollback()
        return "Ha hagut un error en catalogar l'usuari com a blocat"

def afegir_estadistiques(id_tweet, agradaments, retweets, data, hora):
    try:
        cur = conn.cursor()
        insert = str('insert into estadistiques values (DEFAULT, ')+"'"+ str(id_tweet)+"', '"+ str(agradaments)+"', '"+str(retweets)+"', '"+str(data)+"', '"+str(hora)+"')"
        cur.execute(insert)
        conn.commit()
        return "S'ha afegit les estadistiques"
    except:
        conn.rollback()
        return "No s'han afegit les estadistiques"

def actualitzar_estadistiques(id_tweet, agradaments, retweets, data, hora):
    try:
        cur = conn.cursor()
        insert = "update estadistiques set "+'"'+str("m'agrada")+'"'+ " = "+str(agradaments)+", retweet = "+str(retweets) + ", data = '" + str(data) + "', hora = '"+ str(hora) + "' where " +str('"id tweet"')+" like '"+str(id_tweet)+"'"
        cur.execute(insert)
        conn.commit()
        return "S'han actualitzat les estadistiques"
    except:
        conn.rollback()
        return "No s'han actualitzat les estadistiques"


def bloquejar_usuari(id_usuari, motiu, data, hora):
    try:
        cur = conn.cursor()
        insert = str('insert into "usuaris blocats" values (DEFAULT, ')+"'"+ str(id_usuari)+"', '"+ str(motiu)+"', '"+str(data)+"', '"+str(hora)+"')"
        cur.execute(insert)
        conn.commit()
        return "Usuari bloquejat afegit en la base de dades"
    except:
        conn.rollback()
        return "No s'ha pogut afegir l'usuari en la base de dades"

def data_actual ():
    avui = date.today()
    return str(avui.strftime("%Y-%m-%d"))

def hora_actual ():
    ara = datetime.now()
    return str(ara.strftime("%H:%M:%S"))