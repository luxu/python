# -*- coding: utf-8 -*-

import requests

s = requests.session()

# request para igual o do site
headers={
    'Accept': (
        'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/webp,image/apng,*/*;q=0.8'
    ),
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': (
        'pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4,it;q=0.2'
    ),
    # 'Origin': 'http://webgiz.uemg.br',
    'Origin': 'http://controle.luxu.com.br/includes/login.php',    

    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'webgiz.uemg.br',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Referer': 'http://webgiz.uemg.br/index.php',
    'Referer': 'http://controle.luxu.com.br/includes/login.php',
    'Pragma': 'no-cache',
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/61.0.3163.100 Safari/537.36'
    )
}

# pega os cookies do site simulando fazendo o acesso a pagina
# response = s.get('http://webgiz.uemg.br/index.php')
response = s.get('http://controle.luxu.com.br/includes/login.php')
assert response.status_code == 200
# faz o post para logar

response = s.post(
    # url='http://webgiz.uemg.br/index.php?option=com_aixgen',
    url='http://controle.luxu.com.br/includes/login.php',
    data={
        'task': 'loginauth',
        'userType': 'A',
        # 'username': 'teste',
        'username': '',
        'passwd': '',
        # 'passwd': 'teste',
        'instituicao': '0',
        'Turing': ''
    }
)
html = response.content.decode('utf-8')
alert_message = ''
if '<div class="alert-message">' in html:
    alert_message = html.split(
        '<div class="alert-message">')[1].split('</div>')[0]
    alert_message = alert_message.replace('<br>', '\n')
print(alert_message)