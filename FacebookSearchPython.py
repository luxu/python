#@@@@@Sorry: this code has been deprecated in 2015, April 30 with new Facebook 2.0 API version
import urllib.request
import json

def search(texto):
    #pegue o access_token
    #em https://developers.facebook.com/tools/explorer
    token = 'EAANtG5nmr70BAOKqxZA4tmbWrjMMZBxHplcxmZBeQ08ApqVNdYPZClSfCSNnzjHEXZAlt1IUThZBeqWnRVdD5L7Spl9TtRjERqkymTsp8uQ4BlXAbnw0lDhtF7UyXl5zWXWnVct8xegLosJZAHlaCzHDAnxtqT9X0eZCunw6fUGZBZCup4S5Er5xiXhvNygvINOk8DFPPVoQohFpezKzl7eDdy9fy80LZBYB6qaZAZC6ZCORPd1AZDZD'
    # Token de cliente = 3a1dd086eaafca5f3f0dcd13a8df746f
    # Token de acesso = 964390243708861|kmyQ5gtWJDeNcdkOPRjWip06IQY
    url = r'https://graph.facebook.com/search?q='
    # tail = '&type=post&access_token=3a1dd086eaafca5f3f0dcd13a8df746f'
    tail = '&type=post&access_token='+token
    # resp = urllib.request.urlopen(url + texto + tail).read()
    resp = urllib.request.urlopen(url)
    print(resp)
    # data = json.loads(resp.decode('utf-8'))
    # return data['data']

# for resp in search('informatica'):
#     if 'message' in resp:
#         print (resp['from']['name'] + ': ' + resp['message'] + '\n')
search('informatica')