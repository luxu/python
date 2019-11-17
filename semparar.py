# coding: utf-8

import requests
from bs4 import BeautifulSoup as bs
import os, json
from pprint import pprint


api = 'https://minhaconta.semparar.com.br/minhaconta/api/login'

'''
html = get(url)

soup = bs(html.content, 'html.parser')

field_cpf = 'text-field-hero-input-cpf'
field_password = 'text-field-hero-input-password'
btn_submit = 'btn-access-pf'



cookies = {
    'f5avrbbbbbbbbbbbbbbbb': 'OHFNBEKDJNEKHFNFCDKJCLHGMBHBMJBKPDMOGLHOCCFGINDGKABEKELOLIDGLDHBMLEAOOAHPFODKOHJBEKHGBNDAEBANGKIOOIFKBJMALHIIKNMBNBEJFMJBDCMHJMP',
    'clienteLogado': '0',
    'onboarding8976359': 'falso',
    'VtexRCMacIdv7': '49fb4220-085f-11ea-9ccd-8d852c7e2674',
    'VtexFingerPrint': '59e9c0388fada7a1ae5fa58cd2eb75ae',
    '_gcl_au': '1.1.1057927662.1573901600',
    '_ga': 'GA1.3.459976758.1573901600',
    '_gid': 'GA1.3.78870134.1573901600',
    'CookieAwin': 'outro',
    'lmd_orig': 'organic',
    'lmd_traf': 'organic-1573901602416',
    'cto_lwid': 'c332a8d4-efd6-4ed8-822b-073d5d714da3',
    'stc120568': 'tsa:0:20191116112326|env:1%7C20191217105326%7C20191116112326%7C1%7C1100957:20201115105326|uid:1573901606572.1702767095.168718.120568.459876799.4:20201115105326|srchist:1100957%3A1%3A20191217105326:20201115105326',
    '_fbp': 'fb.2.1573901608961.2094101185',
    '_hjid': 'd597ce04-a9da-4fcb-af67-b9dbf009655e',
    'chaordic_browserId': 'a87a7779-3183-4247-81e9-d93117495258',
    'cto_bundle': 'RikBzF9TMjBpU1RzTmFmMnJHZ25TaTdqJTJGZ0lPeUNKeVlKZ1ZMS0tsRm9tUTNpdlFGOTVKTTVPMHJJY0pyR1dCd2N5ZlhmZE12MWNBdWRwY21pNUYxc0JkSktNaG5yMU1MN1N6RFNxT25kOExUS01aa1ZHa29INGszdWFXSm5MR2ZHbWpF',
    '_spl_pv': '1',
    '_cm_ads_activation_retry': 'false',
    'sback_browser': 'a87a7779-3183-4247-81e9-d93117495258-1573901617',
    'sback_client': '5926f3ea82b21c2a325bd05a',
    'sback_customer': '$2AUxkVUhJzbZNVbjJVaXhmTXpnaNBDVa9UYxUVTadUUORVbBp1SEVzTxp2dsdDREpVSxMVSmdFOZBVMwMWOEVmT2$12',
    'sback_access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuc2JhY2sudGVjaCIsImlhdCI6MTU3MzkwMTYxOSwiZXhwIjoxNTczOTg4MDE5LCJhcGkiOiJ2MiIsImRhdGEiOnsiY2xpZW50X2lkIjoiNTkyNmYzZWE4MmIyMWMyYTMyNWJkMDVhIiwiY2xpZW50X2RvbWFpbiI6InNlbXBhcmFyLmNvbS5iciIsImN1c3RvbWVyX2lkIjoiNWRjZmQ1MzM5NWM0ZjY4YzlkNWJhNTc0IiwiY3VzdG9tZXJfYW5vbnltb3VzIjp0cnVlLCJjb25uZWN0aW9uX2lkIjoiNWRjZmQ1MzM5NWM0ZjY4YzlkNWJhNTc1IiwiYWNjZXNzX2xldmVsIjoiY3VzdG9tZXIifX0.94d_YDqE3qMkenm2XW25widtM0Erk8lLPKHxphKIUHo.WrWrDrEiKqHeqBWruyWrHe',
    'sback_partner': 'false',
    'sback_current_session': '1',
    'sback_total_sessions': '1',
    'sb_days': '1573901624570',
    'sback_customer_w': 'true',
    'cookie_custom': '!k6kL3/D/SOVooRZcud1KzNsjdV76X86N3T60VggfjhEhylhI/oT+d82pe7hcJQx3iyGAhQz6df4LFQ==',
    'TS016b6a4f': '014fda1367412d94f70fd459218973620eb24492c13c56f27be31e722e31441f9fc1db2c033c59660e914d1ee047e24e552983c77d0cd98f52878823ab37797e2972c7aba8d1a6e7a608060cb4a75e90f2f80561f114a19b021772bdf16e801eefa506c1cc2051702cb5260bf9a06f14a22fe02896bdff203ee0a5e2cbf4f1d348c4af7fd2b0364593bb2015326140e0d975ec4d0130b35c2c53c3697c484d3baa6fad3234',
    'visid_incap_1822685': 'YjPUBj2uRPaqB0ZNWbWJsDrVz10AAAAAQUIPAAAAAACR5EEptVx8VXdu0Y/ZvR1X',
    'incap_ses_685_1822685': 'rCwoaqEwbAukX53V452BCTrVz10AAAAAyW3XRQeO5V1eZ71uIXueHw==',
    'TSPD_101': '082a7ab28fab2800e8d84d0fe9003bc15b58bd84e3159edd74861a651add8a70962b0417b21c84c71d0058e29a6284de:082a7ab28fab2800e8d84d0fe9003bc15b58bd84e3159edd74861a651add8a70962b0417b21c84c71d0058e29a6284de08b7799e900638001e2e202e73471b493c017321f5ca430b6cd1a871fae91f3c75397161e60c7a151da91372062028ba0a0286be8422aed7464742640a7c8eb9',
    'JSESSIONID': 'BU5z-1RmW-BbihgBN2dIezffLtW_NbTBePECP_iAlYkPMAVC429e!-1240097128!1307930189',
    'G_ENABLED_IDPS': 'google',
    'userId': '8976359',
    '_gat_UA-117845630-3': '1',
    'ADRUM_BTa': 'R:46|g:f4fbb3b1-e419-407c-8ca4-a21615c960c3|n:semparar_31ad92ff-4bb1-44f0-a429-314e4808b341',
    'ADRUM_BT1': 'R:46|i:412053|e:268',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://minhaconta.semparar.com.br',
    'Connection': 'keep-alive',
    'Referer': 'https://minhaconta.semparar.com.br/minhaconta/',
    'TE': 'Trailers',
}

dataDisparo = '2019-11-09T11:32:59.089Z'
dataFim = '2019-11-16T11:32:59.089Z'
quantidade = 100

data = r'{}"dataDisparo":"{}", \
		"dataFim":"{}","index":1, \
		"quantidade":{}{}'.format('{',dataDisparo, dataFim, quantidade, '}')

response = post(
	'https://minhaconta.semparar.com.br/minhaconta/api/disparoPersonalizadoContaConsumoTrio',
	headers=headers,
	cookies=cookies,
	data=data
)

'''

# consumo = get(
# 'https://minhaconta.semparar.com.br/minhaconta/#/conta-consumo-trio')

# soup = bs(consumo.content,'html.parser')


cookies = {
    'clienteLogado': '0',
    'VtexRCSessionIdv7': '0%3A49f8f830-085f-11ea-9ccd-8d852c7e2674',
    'VtexRCMacIdv7': '49fb4220-085f-11ea-9ccd-8d852c7e2674',
    'VtexRCRequestCounter': '1',
    'VtexFingerPrint': '59e9c0388fada7a1ae5fa58cd2eb75ae',
    '_gcl_au': '1.1.1057927662.1573901600',
    '_ga': 'GA1.3.459976758.1573901600',
    '_gid': 'GA1.3.78870134.1573901600',
    'CookieAwin': 'outro',
    'lmd_orig': 'organic',
    'lmd_traf': 'organic-1573901602416',
    'cto_lwid': 'c332a8d4-efd6-4ed8-822b-073d5d714da3',
    'stc120568': 'tsa:0:20191116112326|env:1%7C20191217105326%7C20191116112326%7C1%7C1100957:20201115105326|uid:1573901606572.1702767095.168718.120568.459876799.4:20201115105326|srchist:1100957%3A1%3A20191217105326:20201115105326',
    '_fbp': 'fb.2.1573901608961.2094101185',
    '_hjid': 'd597ce04-a9da-4fcb-af67-b9dbf009655e',
    'chaordic_browserId': 'a87a7779-3183-4247-81e9-d93117495258',
    'impulsesuite_session': '1573901615037-0.67973215899707',
    'cto_bundle': 'RikBzF9TMjBpU1RzTmFmMnJHZ25TaTdqJTJGZ0lPeUNKeVlKZ1ZMS0tsRm9tUTNpdlFGOTVKTTVPMHJJY0pyR1dCd2N5ZlhmZE12MWNBdWRwY21pNUYxc0JkSktNaG5yMU1MN1N6RFNxT25kOExUS01aa1ZHa29INGszdWFXSm5MR2ZHbWpF',
    '_st_ses': '9058366954002292',
    '_sptid': '2222',
    '_spcid': '2181',
    '_st_no_user': '1',
    '_st_no_script': '1',
    '_spl_pv': '1',
    '_cm_ads_activation_retry': 'false',
    'sback_browser': 'a87a7779-3183-4247-81e9-d93117495258-1573901617',
    'sback_client': '5926f3ea82b21c2a325bd05a',
    'sback_customer': '$2AUxkVUhJzbZNVbjJVaXhmTXpnaNBDVa9UYxUVTadUUORVbBp1SEVzTxp2dsdDREpVSxMVSmdFOZBVMwMWOEVmT2$12',
    'sback_access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuc2JhY2sudGVjaCIsImlhdCI6MTU3MzkwMTYxOSwiZXhwIjoxNTczOTg4MDE5LCJhcGkiOiJ2MiIsImRhdGEiOnsiY2xpZW50X2lkIjoiNTkyNmYzZWE4MmIyMWMyYTMyNWJkMDVhIiwiY2xpZW50X2RvbWFpbiI6InNlbXBhcmFyLmNvbS5iciIsImN1c3RvbWVyX2lkIjoiNWRjZmQ1MzM5NWM0ZjY4YzlkNWJhNTc0IiwiY3VzdG9tZXJfYW5vbnltb3VzIjp0cnVlLCJjb25uZWN0aW9uX2lkIjoiNWRjZmQ1MzM5NWM0ZjY4YzlkNWJhNTc1IiwiYWNjZXNzX2xldmVsIjoiY3VzdG9tZXIifX0.94d_YDqE3qMkenm2XW25widtM0Erk8lLPKHxphKIUHo.WrWrDrEiKqHeqBWruyWrHe',
    'sback_partner': 'false',
    'sback_current_session': '1',
    'sback_total_sessions': '1',
    'sb_days': '1573901624570',
    'sback_customer_w': 'true',
    'cookie_custom': '!k6kL3/D/SOVooRZcud1KzNsjdV76X86N3T60VggfjhEhylhI/oT+d82pe7hcJQx3iyGAhQz6df4LFQ==',
    'f5avrbbbbbbbbbbbbbbbb': 'BNKKKAHOLLGBKHCHLIDGKFFPHMNGLODDCMJJPAHEKFIIEDEMHIDDGFHCCKAMLEHDCKJABAPMPFHDNPNPHNCFKIEBHCAAAKDHPEGGBGPMFIJKLNIFONHPKOBKNNLIBCJM',
    'TS016b6a4f': '014fda1367e7c66709fa72f1122923399d906bea41d381f000bf371f449b132b948c8d1ce7588ff5d2fae5d833aa5d591b6dcf4d24632843eefff40e640833668eed1ef739d5ea114c0dfa58f97f3054bc478a7d858c7e4f9b31ba230b4c2d1cf4d8e1ad701f7a20fc2b437f0842f815a49fc49433b7770e3ef73cacddf2f4314d749d8e52',
    'visid_incap_1822685': 'YjPUBj2uRPaqB0ZNWbWJsDrVz10AAAAAQUIPAAAAAACR5EEptVx8VXdu0Y/ZvR1X',
    'incap_ses_685_1822685': 'rCwoaqEwbAukX53V452BCTrVz10AAAAAyW3XRQeO5V1eZ71uIXueHw==',
    'TSPD_101': '082a7ab28fab2800e8d84d0fe9003bc15b58bd84e3159edd74861a651add8a70962b0417b21c84c71d0058e29a6284de:082a7ab28fab2800e8d84d0fe9003bc15b58bd84e3159edd74861a651add8a70962b0417b21c84c71d0058e29a6284de08b7799e900638001e2e202e73471b493c017321f5ca430b6cd1a871fae91f3c75397161e60c7a151da91372062028ba0a0286be8422aed7464742640a7c8eb9',
    'JSESSIONID': 'kkFz2UdicVx4FLngvPvaS1pwqYilCQNx9K-8AhiS5NgHZZUfrMP0!-1240097128!1307930189',
    'G_ENABLED_IDPS': 'google',
    '_gat_UA-117845630-3': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://minhaconta.semparar.com.br',
    'Connection': 'keep-alive',
    'Referer': 'https://minhaconta.semparar.com.br/minhaconta/',
}


data = '{"login":"20443596859","senha":"222222","nome":"","tipoCliente":1}'


def logar(html):
	s = requests.Session()
	r = s.post(html, headers=headers, cookies=cookies, data=data)
    # r = session(html, headers=headers, cookies=cookies, data=data)
	resultado = r.json()
	return resultado


def acessar_pagina(token, page):
    head = {f'Authorization': 'token {token}'}
    response = session(
    	page,
    	headers=head
	)
    print(response.text)

if __name__ == '__main__':
    token = logar(api)
    pprint(token)
    # page = 'https://minhaconta.semparar.com.br/minhaconta/api/obterSaldoPrepago'
    # acessar_pagina(token, page)
    # if 'status' not in token:
       # acessar_pagina(token, page)
    # else:
        # os.system('cls')
        # print('{}\nERRO.: {}\n{}'.format('*'*66,token['message'],'*'*66))
