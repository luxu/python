# coding: utf-8

from requests import get
from bs4 import BeautifulSoup as bs
from time import sleep
import os


def getSoup(url):
    url = 'https://statsroyale.com/profile/P9V0VC9R'
    res = get(url)
    res.raise_for_status()
    soup = bs(res.content, 'html.parser')
    return soup


def verChest(url):
    soup = getSoup(url)
    chests = [x.getText().strip() for x in soup.findAll('div', class_='chests__tooltip')]
    if (os.name != 'posix'): # for windows
        os.system("cls")
    else:
        os.system("clear")
    print(f'First chest.: {chests[0]}')
    for x in chests[1:]:
        print(x)


def acao_no_browser(url):
    # remove o arquivo ANTES de salvá-lo dnv
    # if os.path.isfile('royale.txt'):
    #     os.remove('royale.txt')
    soup = getSoup(url)
    msg_updated = soup.find(
        'div', class_="refresh__time"
    ).getText().strip()
    last_updated = soup.find(
        'div', class_="refresh__buttonContainer"
    ).find('div').getText().strip()
    # May only be updated in 2 minutes
    # Last updated 8 minutes ago
    last_updated = str(last_updated).strip()
    if not 'May only' in last_updated:
        get('https://statsroyale.com/profile/P9V0VC9R/refresh')
        updated = soup.find(
            'div', class_="refresh__time"
        ).getText().strip()
        sleep(5)
    verChest(url)


def escreverArquivo(texto):
    arq = open('royale.txt','w')
    arq.write(texto)
    arq.flush()
    arq.close()


def lerArquivo():
    with open('royale.txt') as f:
        textos = f.read()
    print(textos)

if __name__ == "__main__":
    url = 'https://statsroyale.com/profile/P9V0VC9R'
    acao_no_browser(url)
    # lerArquivo()
    # verChest(url)