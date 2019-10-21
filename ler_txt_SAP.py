# coding: utf-8

import re
import os
import sys
from pprint import pprint

def lerArquivo(arquivo):
	# set_trace()
	with open(arquivo, encoding="utf-8") as _file:
		texto = _file.readlines()
	for t in texto:
		'''Transforma o texto em
			dicionário tirando os espaços em branco'''
		t = t.split('\n')
		t = t[0].split("['")
		print(t[0])
		print('*'*66)
		'''Só pega as linhas do texto que seja maior do que 30
		e que na posição 2 do dicionário tenha a string 2018,
		qdo mudar o ano mude aqui tb'''


filename = 'error_log'
# 'remuneracao.txt'
arquivo = os.path.join(os.path.abspath('../'),filename)
from ipdb import set_trace
lerArquivo(arquivo)
