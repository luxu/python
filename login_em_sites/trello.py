# coding: utf-8

from requests import post, get
import os


def logar(html, params):
    r = post(html, data=params)
    resultado = r.json()
    return resultado


def acessar_pagina(self):
    head = {'Authorization': 'token {}'.format(self)}
    # url = 'https://trello.com/luxu11/boards'
    url = 'https://trello.com/b/NBVLhgjA/site-ong-crescer'
    response = get(url, headers=head)

    print(response.text)

if __name__ == '__main__':
    params = {
        'factors[user]': '',
        'factors[password]': '',
        'method': 'password'
    }
    html = 'https://trello.com/1/authentication'
    token = logar(html, params)
    print(len(token['code']))
    # if 'status' not in token:
    acessar_pagina(token)
    # else:
    #     os.system('cls')
    #     print('{}\nERRO.: {}\n{}'.format('*'*66,token['message'],'*'*66))
