import requests

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# ambos 'x-test' e 'x-test2' são enviados
s.get(
	'http://httpbin.org/headers',
	headers={
		'x-test2': 'true'
	}
)

