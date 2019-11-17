import tweepy
from ipdb import set_trace


chave_consumidor = 'IaGxsIzsyKfpLh9T92NsKO90Z'
segredo_consumidor = 'oLhi0pmgByFY58elmbxMoPSPO8sHcehqtarCyRHZvLRV5k81OO'
token_acesso = '44365030-u1LV8UIALkYvPha7OWe2NbJl6U2j6A8ce9eR1RO5H'
token_acesso_segredo = '44365030-u1LV8UIALkYvPha7OWe2NbJl6U2j6A8ce9eR1RO5H'


autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)

autenticacao.set_access_token(token_acesso, token_acesso_segredo)

try:
	twitter = tweepy.API(autenticacao)
	print('Conected!!!')
except Exception as err:
	print(err)

# set_trace()
result = twitter.search(q='AluraOnline')
print(twitter)
