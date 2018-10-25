# coding=utf-8

import requests
import random
from pprint import pprint

def proxies(q, mode='json'):
		url = 'http://proxy.tekbreak.com/%s/%s' % (q,mode)
		r = requests.get(url)
		proxy = list()

		x = random.randrange(0, len(r.json()))

		proxy = '%s://%s:%s' % (r.json()[x]['type'].lower(), r.json()[x]['ip'], r.json()[x]['port'])
		proxies = {r.json()[x]['type'].lower():proxy}
		return proxies

proxies = proxies(q=10)
r = requests.get('http://ipinfo.io', proxies=proxies)
print(r.content)