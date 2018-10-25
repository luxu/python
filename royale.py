#!/usr/bin/env python3
# coding: utf-8

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pprint
# import rows
import json
import os

url = 'https://statsroyale.com/profile/P9V0VC9R'

def verChest(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, 'html.parser')
    listaChest = soup.select('.chests__tooltip')
    # listaChest = soup.select('.chests__queue')
    # listaChest = listaChest1.select('div')
    stri = ''
    for x in listaChest:
        stri+=''.join(x.text)
    ultimo = stri[:-1].split()
    arq = open('royale.txt','w')
    arq.write('next:'+ultimo[0]+ultimo[1]+'\n')
    arq.write(ultimo[2]+ultimo[3]+ultimo[4]+'\n')
    arq.write(ultimo[5]+ultimo[6]+ultimo[7]+'\n')
    arq.write(ultimo[8]+ultimo[3]+ultimo[4]+'\n')
    arq.write(ultimo[11]+ultimo[12]+ultimo[13]+'\n')
    arq.write(ultimo[14]+ultimo[15]+ultimo[16]+'\n')
    arq.write(ultimo[17]+ultimo[18]+ultimo[19]+'\n')
    arq.write(ultimo[20]+ultimo[21]+ultimo[22]+'\n')
    arq.write(ultimo[23]+ultimo[24]+ultimo[25]+'\n')
    arq.write(ultimo[26]+ultimo[27]+ultimo[28]+'\n')
    arq.write(ultimo[29]+ultimo[30]+ultimo[31]+ultimo[32]+'\n')
    # arq.write(ultimo[33]+ultimo[34]+ultimo[35]+'\n')
    # arq.write(ultimo[36]+ultimo[37]+ultimo[38]+'\n')
    # arq.write(ultimo[39]+ultimo[40]+ultimo[41]+'\n')
    arq.close()

def escreverArquivo(texto):
    arq = open('royale.txt','w')
    arq.write(texto)
    arq.flush()
    arq.close()

def lerArquivo():
    dicionario = {}
    # cont = 1
    with open('royale.txt') as f:
        textos = f.read()
    print(textos)

def acao_no_browser(url):

    # remove o arquivo ANTES de salvá-lo dnv
    if os.path.isfile('royale.txt'):
        os.remove('royale.txt')
    browser = webdriver.Chrome()
    browser.get(url)
    try:
        btnAtualizar = browser.find_element_by_xpath('//*[@id="refresh-profile-text"]/div[2]')
        btnAtualizar.click()
    except Exception as e:
        print('Erro.: {}'.format(e))

    sleep(5)

    verChest(url)

acao_no_browser(url)
# lerArquivo()
# verChest(url)