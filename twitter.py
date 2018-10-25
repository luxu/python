import twitter
import configparser

# Carrega as configurações de arquivo externo
config = configparser.ConfigParser()
config.read('config.ini')

access_token = config['twitter']['accesstoken']
access_token_secret = config['twitter']['accesstokensecret']
consumer_key = config['twitter']['consumerkey']
consumer_secret = config['twitter']['consumersecret']

'''
api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)
'''
# print(api.VerifyCredentials())

# users = api.GetFriends()
# print([u.name for u in users])

# status = api.PostUpdate('Eu amo python-twitter!')
# print(status.text)
'''
    # raw_query="q=Denise Campos de Toledo%20&result_type=recent&since=2017-08-01&count=100")
results = api.GetSearch(
    raw_query="l=&q=Denise%20Campos%20de%20Toledo%20since%3A2017-08-01%20until%3A2017-12-06")

cont = 0
for x in results:
    # print(x['created_at'])
    print(x.text)
    # print(cont)
    # cont += 1
'''