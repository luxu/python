# coding: utf-8

from requests import post, get
import os


def logar(html, params):
    r = post(html, data=params)
    resultado = r.json()
    return resultado


def acessar_pagina(self):
    head = {'Authorization': 'token {}'.format(self)}
    response = get('https://app.rabbiit.com/a/e7635e19d341/#/projects/3', headers=head)

    # print(response)

if __name__ == '__main__':
    params = {
        'email':'',
        'password':''
    }
    html = 'https://app.rabbiit.com/api/v1/auth'
    token = logar(html, params)
    if 'status' not in token:
       acessar_pagina(token)
    else:
        os.system('cls')
        print('{}\nERRO.: {}\n{}'.format('*'*66,token['message'],'*'*66))