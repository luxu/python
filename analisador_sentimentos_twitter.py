from textblob import TextBlob as tb
import tweepy
import numpy as np
import configparser

# Carrega as configurações de arquivo externo
config = configparser.ConfigParser()
config.read('config.ini')

access_token = config['twitter']['accesstoken']
access_token_secret = config['twitter']['accesstokensecret']
consumer_key = config['twitter']['consumerkey']
consumer_secret = config['twitter']['consumersecret']

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

# Variável que irá armazenar todos os Tweets com a palavra escolhida
# na função search da API
# public_tweets = api.search('suco_de_uva')
# public_tweets = api.search('DeniseCToledo8')
# public_tweets = api.search('carlacecato')
public_tweets = api.search('CarlaBigatto')

# Variável que irá armazenar as polaridades

analysis = None

for tweet in public_tweets:
    print(tweet.text)
    analysis = tb(tweet.text)
    print(analysis.sentiment.polarity)
# A função sentiment.polarity retornará um número entre -1 e 1, 
# onde quanto maior esse número, menos putassa a pessoa está, basicamente.    

print('MÉDIA DE SENTIMENTO: ' + 
str(np.mean(analysis.sentiment.polarity)))

