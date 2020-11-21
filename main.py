#FUNCIONS CONFIGURADES:
#   - print(data_actual()) --> Avui és dd de mm de aaaa
#   - tendenciaf(zona) --> Actualment hi ha 2 zones: "BCN" i "MD", quan s'envia en el parametre zona, retorna els 50 trending topics
#   - revisar_seguidors() --> Retorna la suma de seguidors. Millor no abusar d'aquesta comanda (menys en un bucle) perquè peta fàcilment
#   - missatge(text,False/True,Flase) --> Fa un tweet. En la variable text s'escriu el contingut, si es un tweet que respon a un altre tweet, s'ha d'escriure "True", sino "False"
#                                         No és necessari prestar atencio en la cantitat de caràcters, ja que si et passes crea un fil de tweets.
#   - cur.execute("consulta/accio") --> S'executa la comanda que s'especifiqui. Si la comanda es una acció que modifica la base de dades, cal executar el conn.commit()
#                                       Exemple: conn.execute("create table test()") -- NO S'EXUCTA FINS....-- conn.commit --LA TALA ARA SÍ QUE S'HA CREAT--
#   - afegir_usuari("id_usuari", "nom") --> Afegir usuari a la base de dades
#   - afegir_tweet("id_tweet","text") --> Afegir el text d'un tweet amb un ID
#   - tweet_normal("id_tweet",data_actual(),"hh:mm:ss") --> Especificar si el tweet ha estat escrit per mi
#   - tweet_usuaris("22","9999", data_actual(), hora_actual()) --> Especificar si el tweet ha estat escrit per un altre usuari
#   - tweet_resposta("22","9999", data_actual(), hora_actual()) --> Especificar si el tweet és una resposta
#   - afegir_seguidor("1", data_actual(), hora_actual()) --> Afegir seguidor en la base de dades
#   - afegir_unfollow("1", data_actual(), hora_actual()) --> Afegir un exseguidor
#   - afegir_bloqueig("1", data_actual(), hora_actual()) --> Afegir l'usuari en la llista negra
#   - afegir_estadistiques("1","15","20", data_actual(), hora_actual()) --> Afegir dades d'un tweet id_tweet, m'agrada, retweet, data, hora
#   - actualitzar_estadistiques("1", "100", "120", data_actual(), hora_actual()) --> Actualitzar les dades dels meus tweets
#   - bloquejar_usuari("1","motiu", data_actual(), hora_actual()) --> Afegir a la base de dades l'usuari com a bloquejats



#LLIBRERIES EXTERNES
import tweepy
from datetime import datetime
from datetime import date

#LLIBRERIES PERSONALS
from acces_tweepy.autenticacio import api
from eines_personals.dia_actual import data_actual_tweet
from eines_personals.trending import tendenciesf
from eines_personals.llista_seguidors import revisar_seguidors
from tweet.missatge import missatge
from postgres.p_connexio import conn
from postgres.interaccio import afegir_usuari
from postgres.interaccio import afegir_tweet
from postgres.interaccio import tweet_normal
from postgres.interaccio import tweet_usuaris
from postgres.interaccio import tweet_resposta
from postgres.interaccio import afegir_seguidor
from postgres.interaccio import afegir_unfollow
from postgres.interaccio import afegir_bloqueig
from postgres.interaccio import afegir_estadistiques
from postgres.interaccio import actualitzar_estadistiques
from postgres.interaccio import bloquejar_usuari
from postgres.interaccio import data_actual
from postgres.interaccio import hora_actual

#text = "Bones gent! Sóc un Bot que gestiona aquest perfil de Twitter. El meu desenvolupador, és a dir, el meu pare, m'ha explicat que vol fer una sol·licitud a @unicode perquè la senyera sigui icona pel WhatsApp, Facebook, Twitter... Com que la sol·licitud es podrà enviar després del dia 2 d'abril de l'any 2021 (si el coronavirus ens deixa), el meu creador, està estructurant aquest projecte perquè estiguem tots implicats. Inclús jo! Que tot i ser un bot, el meu creador m'ha donat la confiança d'administrar el perfil de Twitter per tal què aquest missatge arribi beeeeen lluny."
#print(missatge(text,False,False))

print(tendenciesf("BCN"))

#print(missatge("Bon dia! "+data_actual_tweet()+". Com esteu? Comenteu!",False,False))
