 # -*- coding: utf-8 -*-

import shutil
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def donwload(arquivo):
	# arq = 'C:\\caminho\\testes\\'+ arquivo
	diretorio = u'{}/{}'.format(os.getcwd(),'testes')
	arq = u'{}/{}'.format(diretorio,arquivo)
	# driver = webdriver.Chrome()
	driver = webdriver.Firefox()
	driver.implicitly_wait(30)
	driver.get('http://zarbi.chem.yale.edu/ligpargen/index.html')
	#driver.find_element_by_id("exampleMOLFile").click()
	driver.find_element_by_id("exampleMOLFile").clear()
	driver.find_element_by_id("exampleMOLFile").send_keys(arq)
	driver.find_element_by_xpath(
		"(.//*[normalize-space(text()) and normalize-space(.)='Molecule charge'])[1]/following::button[1]"
	).click()
	#driver.find_element_by_xpath("//input[@type='submit' and @value='something']").click()
	driver.find_element_by_xpath("//input[@type='submit' and @value='TOP']").click()
	driver.implicitly_wait(50)


def inicio():
	diretorio = os.getcwd()
	# pasta = u'{}/{}'.format(diretorio,'molecula.pdb')
	# pasta = os.listdir("C:\\caminho\\testes")
	# if not os.path.exists("testes"):
	# 	os.makedirs("testes")
	pasta = os.listdir("testes")
	dir_testes = u'{}/{}'.format(os.getcwd(),'testes')
	arquivos = [arq for arq in pasta if os.path.isfile(os.path.join(dir_testes, arq))]
	# print(arquivos)
	pdb = [arq for arq in arquivos if arq.lower().endswith(".pdb")]
	# print(pdb)
	# print (len(pdb))
	if not os.path.exists('testar'):
		os.makedirs('testar')
	else:
		os.system('rm -Rf testar/')
		os.makedirs('testar')
	for b in pdb:
		# donwload(b)
		dir = b.split(".")[0]
		os.makedirs(u'{}/{}'.format('testar',dir))
	# print(os.listdir("testar"))
	if not os.path.exists('Downloads'):
		os.makedirs('Downloads')
	else:
		os.system('rm -Rf Downloads/')
		os.makedirs('Downloads')
	for i in range(1,5):
		arquivo = u'Arquivo{}.itp'.format(i)
		os.system(u'touch Downloads/{}'.format(arquivo))
	a = os.listdir("Downloads")
	dir_testes = u'{}/{}'.format(os.getcwd(),'Downloads')
	ar = [arq for arq in a if os.path.isfile(os.path.join(dir_testes, arq))]
	jpgs = [art for art in ar if art.lower().endswith(".itp")]
	if not os.path.exists('Destino'):
		os.makedirs('Destino')
	else:
		os.system('rm -Rf Destino/')
		os.makedirs('Destino')
	'''Coloque o caminho completo abaixo'''
	origem = '/home/luxu/Área de Trabalho/Downloads/'
	[shutil.move(origem+j,'Destino') for j in jpgs]
	print(os.listdir("Destino"))

inicio()
