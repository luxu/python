#coding: utf-8

import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.mentebinaria.com.br/apoie/'

p = requests.get(url)
p.raise_for_status()
soup = BeautifulSoup(p.content, 'html.parser')
# print(soup)
lista = soup.find_all('ul',class_='ipsList_inline ipsList_noSpacing')
for l in lista[1]:
    print(l)
# d = json.loads(p.content)
# //*[@id="elCmsPageWrap"]/div/div/ul/li/div/ul
