import requests

cookies = {
    'ASPSESSIONIDSUDQACSB': 'OHJEIEIBGJFKKPMEJIPLCPKD',
}

headers = {
    'Origin':
    'https://www.fazenda.sp.gov.br',
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Content-Type':
    'application/x-www-form-urlencoded',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control':
    'max-age=0',
    'Referer':
    'https://www.fazenda.sp.gov.br/folha/nova_folha/acessar_dce.asp?menu=dem&user=rs',
    'Connection':
    'keep-alive',
}

data = [
    ('hid_tipouser', 'rs'),
    ('txt_logindce', '11632112'),
    ('txt_senhadce', ''),
    ('enviar', 'Acessar'),
]

requests.post(
    'https://www.fazenda.sp.gov.br/folha/nova_folha/autentica.asp',
    headers=headers,
    cookies=cookies,
    data=data)

req = requests.session()
# req.post()
print(req.get())