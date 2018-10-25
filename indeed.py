#!/usr/bin/env python3
# coding: utf-8

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pprint
import json
import os

url = 'https://www.indeed.com.br/empregos-de-python-em-londrina'

def verChest(url):
    res = requests.get(url)
    res.raise_for_status()
    return BeautifulSoup(res.content, 'html.parser')

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

soup = verChest(url)