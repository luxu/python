import twitter_scraper

user = u'DeniseCToledo8'

listas = twitter_scraper.get_tweets(user)
for lista in listas:
	print(u'{} - {} \n {}'.format(lista['time'],lista['text'],('*')*60))
