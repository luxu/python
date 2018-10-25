#Import the necessary methods from tweepy library
# from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import configparser

# Carrega as configurações de arquivo externo
config = configparser.ConfigParser()
config.read('config.ini')

#Variables that contains the user credentials to access Twitter API
access_token = config['twitter']['accesstoken']
access_token_secret = config['twitter']['accesstokensecret']
consumer_key = config['twitter']['consumerkey']
consumer_secret = config['twitter']['consumersecret']

#This is a basic listener that just prints received tweets to stdout.
# class StdOutListener(StreamListener):

#     def on_data(self, data):
#         print(data)
#         return True

#     def on_error(self, status):
#         print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    # l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    user = api.get_user('carlacecato')
    user2 = api.get_user('DeniseCToledo8')

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

    # for follower in tweepy.Cursor(api.followers).items():
    #    follower.follow()

    # print(user.screen_name,user.followers_count)
    # print(user2.screen_name,user2.followers_count)
    # for friend in user2.friends():
    #    print(friend.screen_name)

    # stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=['python', 'javascript', 'ruby'])
    # stream.filter(track=['DeniseCToledo8'])
    # stream.filter(track=['CarlaBigatto'])