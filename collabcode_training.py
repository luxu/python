# coding: utf-8

from requests import post, get
from bs4 import BeautifulSoup as bs
import os


def logar(html, params):
    r = post(html, data=params)
    resultado = r.json()
    return resultado


def acessar_pagina(token):
    headers = {
        'Referer': 'http://www.collabcode.training/dashboard',
        'Accept-Encoding': 'identity;q=1, *;q=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Range': 'bytes=0-',
        'chrome-proxy': 'frfr',
    }
    # url = 'https://s3-sa-east-1.amazonaws.com/do-front-ao-end/01-aula/01-terminal/02-preparando-o-campo.mp4'
    url = 'http://www.collabcode.training/dashboard'
    response = get(url, headers=headers)
    print(response.status_code)

if __name__ == '__main__':
    params = {
        'email': 'zicadopv@gmail.com',
        'password': '22222222'
    }
    html = 'https://collabcode-auth-api.herokuapp.com/auth/login'
    token = logar(html, params)
    # print(len(token['code']))
    acessar_pagina(token)
    # acessar_pagina()
