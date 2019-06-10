# coding=utf-8

from requests import get, session, request
import random
from pprint import pprint
from datetime import datetime, timedelta

def get_proxys():
    url = 'https://hidemy.name/ru/loginx'
    url1 = 'https://hidemy.name/api/proxylist.txt?out=plain&lang=ru'
    data = {'c':'976402971148490'}
    s = session()
    s.get(url1)
    s.post(url,data=data)
    res = s.get(url1)
    result = res.text.split('\r\n')
    return result

def is_bad_proxy(pip,url):
    try:
        res = get(
        	url,
        	proxies={'http':pip},
        	headers={'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'},
        	timeout=10
    	)
    except Exception as detail:
        print(f"ERROR.:{detail}")
        return 1
    if res.status_code ==200:
        return 0
    else:
        print(res.status_code)
        return 1


def validate_proxies(proxies,url):
    proxys = []
    random.shuffle(proxies)
    stime = datetime.now()+timedelta(minutes=30)
    for proxy in proxies:
        if stime < datetime.now():
            break
        bad_proxy = is_bad_proxy(proxy,url)
        if not bad_proxy:
            print(proxy, "APPROVED!")
            proxys.append({'http':proxy})
            if len(proxys)==10:
                break
        elif str(bad_proxy)[0]=='5' and len(proxys)==0:
            print('This service is now unavailable (site from scraping is unavailable)')
    if len(proxys)==0:
        return 0
    return proxys


def choice_proxy(proxies):
	return proxies[random.randint(0,len(proxies)-1)]


def proxies(q, mode='json'):
		url = f'http://proxy.tekbreak.com/{q}/{mode}'
		print(url)
		r = get(url)
		proxy = list()
		from ipdb import set_trace
		set_trace()

		x = random.randrange(0, len(r.json()))

		proxy = '%s://%s:%s' % (r.json()[x]['type'].lower(), r.json()[x]['ip'], r.json()[x]['port'])
		proxies = {r.json()[x]['type'].lower():proxy}
		return proxies

if __name__ == '__main__':
	# proxies = proxies(q=10)
	url = 'http://ipinfo.io'
	proxies = get_proxys()
	proxies = validate_proxies(proxies,url)
	if proxies!=0:
		response = get(url,proxies=choice_proxy(proxies))
	else:
		response = get(url)
	print(f'{"*"*66}\n{response.text}')
	# r = get('http://ipinfo.io', proxies=proxies)
	# print(r.content)
