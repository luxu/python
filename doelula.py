import requests
import json

url = 'https://doe.lula.com.br/api/campaign/doadores'

d = requests.get(url).json()
cont = 1
total = 0.0
for doador in d:
	print(doador['nome'],doador['cpf'],
		doador['valor'],doador['data_envio'])
	total += float(doador['valor'])
	print('Cont.: {}'.format(cont))
	print('*'*60)
	# print('\n')
	cont+=1
print(total)