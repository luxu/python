# coding: utf-8

import re

def lerArquivo(arquivo):
	with open(arquivo, encoding="utf8") as _file:
		texto = _file.readlines()
	for t in texto:
		'''Transforma o texto em dicionário tirando os espaços em branco'''
		t = t.split(' ')
		'''Só pega as linhas do texto que seja maior do que 30
		e que na posição 2 do dicionário tenha a string 2018,
		qdo mudar o ano mude aqui tb'''
		if len(t) > 30 and re.search(r'2018',t[2]):
			'''Daki em diante é só pegar os dados que quiser,
			aqui só printei o dicionário'''
			print(u'{}'.format(t))

arquivo = 'arquivo1.txt'
lerArquivo(arquivo)

