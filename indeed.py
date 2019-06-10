# coding: utf-8

from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
import pprint
import json
import os



def verChest(url):
    res = get(url)
    res.raise_for_status()
    html = bs(res.content, 'html.parser')
    from ipdb import set_trace
    set_trace()
    return html


def escreverArquivo(texto):
    arq = open('royale.txt','w')
    arq.write(texto)
    arq.flush()
    arq.close()


def lerArquivo():
    dicionario = {}
    with open('royale.txt') as f:
        textos = f.read()
    print(textos)

if __name__ == '__main__':
    url = 'https://www.indeed.com.br/empregos-de-python-em-londrina'
    soup = verChest(url)