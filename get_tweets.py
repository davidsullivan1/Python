import json as _json
import tweepy as tp
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime
from settings import consumer_key, consumer_secret, access_token, accessTokenSecret

#Chaves de Acesso - As chaves de acesso foram configuradas em um arquivo settings.py com os valores
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
accessTokenSecret = accessTokenSecret

#Definindo arquivo de saída para armazenar os tweets encontrados

dtHoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collected_Tweet_{dtHoje}.txt", "w", encoding="latin1")

#Implementando Classe para conexão com Twitter
class MyListener(tp.StreamListener):
    
    # def on_status(self, tweet):
    #     print(tweet.author.screen_name)
    #     print(tweet.text.encode("utf-8"))
    #     return True

    def on_data(self, data):
        tweet = _json.loads(data) #Necessário para transformar no formato correto do JSON
        itemString = _json.dumps(tweet)
        out.write(itemString + '\n')
        return True
 

    def on_error(self, status):
        print(status)

#implementando a função principal
if __name__ == "__main__":
    listening = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, accessTokenSecret)

    stream = Stream(auth, listening)
    stream.filter(track=["PalavrasChaves])
