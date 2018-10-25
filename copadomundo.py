import requests
import pandas as pd

import requests

cookies = {
    'check': 'true',
    's_rd_serialize': 'rtdriekrtm5',
    'AMCVS_4435697753736FB20A490D45^%^40AdobeOrg': '1',
    's_rd_refcp': 'Direto',
    'camp_medium': 'empty',
    'camp_source': 'empty',
    's_cc': 'true',
    'aam_uuid': '31625630632712135074252421937134918360',
    '_ga': 'GA1.3.635154751.1536146688',
    '_gid': 'GA1.3.1260483971.1536146688',
    'AAMC_itau_0': 'AMSYNCSOP^%^7C411-17787',
    'btpdb.YdB4XyS.dGZjLjI2MTIwMzY': 'VVNFUg',
    'btpdb.YdB4XyS.dGZjLjU5MjY5MjI': 'VVNFUg',
    's_fid': '6E92554BB8A6A932-0BFF538CEC036F55',
    'ASP.NET_SessionId': 'ozedm4ui2ap4l1k5aufop0jx',
    'URLEncapsulada': '',
    'AMCV_4435697753736FB20A490D45^%^40AdobeOrg': '-179204249^%^7CMCIDTS^%^7C17780^%^7CMCMID^%^7C31354402266843196924279368692945462487^%^7CMCAAMLH-1536751485^%^7C4^%^7CMCAAMB-1536776792^%^7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y^%^7CMCOPTOUT-1536179192s^%^7CNONE^%^7CMCAID^%^7CNONE',
    's_rd_LastVisit': '1536175048858',
    's_rd_LastVisit_s': 'Less^%^20than^%^201^%^20day',
    's_rd_getNewRepeat': '1536175048859-Repeat',
    's_rd_gpv_v4': 'UR^%^3AWEB^%^3ANLOG^%^3AHome',
    's_rd_visit': '1',
    's_rd_ppvl': 'UR^%^253AWEB^%^253ANLOG^%^253AHome^%^2C12^%^2C12^%^2C439^%^2C1440^%^2C439^%^2C1440^%^2C900^%^2C1^%^2CP',
    'mbox': 'PC^#283cdd1d0550457ca9e0216c014e8c89.17_28^#1599391490^|session^#9178fd5bd2fa49668bbc7080c0f93173^#1536176910',
    '_gat_UA-27731496-8': '1',
    's_rd_ppv': 'UR^%^253AWEB^%^253ANLOG^%^253AHome^%^2C9^%^2C9^%^2C439^%^2C1440^%^2C439^%^2C1440^%^2C900^%^2C1^%^2CP',
    's_rd_ptc': '0.82^%^5E^%^5E0.00^%^5E^%^5E0.00^%^5E^%^5E0.00^%^5E^%^5E0.12^%^5E^%^5E0.00^%^5E^%^5E14.32^%^5E^%^5E0.01^%^5E^%^5E15.29',
    's_rd_tps': '31',
    's_rd_pvs': '30',
    's_sq': 'it-rede-geral^%^3D^%^2526c.^%^2526a.^%^2526activitymap.^%^2526page^%^253Dhttps^%^25253A^%^25252F^%^25252Fwww.userede.com.br^%^25252F^%^2526link^%^253Dentrar^%^2526region^%^253Dform-cadastro-login^%^2526.activitymap^%^2526.a^%^2526.c^%^2526pid^%^253Dhttps^%^25253A^%^25252F^%^25252Fwww.userede.com.br^%^25252F^%^2526oid^%^253Dentrar^%^2526oidt^%^253D3^%^2526ot^%^253DSUBMIT',
    'ADRUM': 's=1536175079518^&r=https^%^3A^%^2F^%^2Fwww.userede.com.br^%^2F^%^3F0',
    'ADRUM_BTa': 'R:27^|g:b0ed740f-944f-48e9-bb08-3cdfebd107a4^|n:customer1_e5ed8bbf-1ffc-461b-8857-b6d143fb54e4',
    'ADRUM_BT1': 'R:27^|i:8133^|e:177',
    'FedAuth': '77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+MCMuZnxtfDElM2IxMjU0MTgxOCUzYmpvc2VqYWlsdG9uQGdtYWlsLmNvbSUzYnRydWUlM2IsMCMuZnxtfDElM2IxMjU0MTgxOCUzYmpvc2VqYWlsdG9uQGdtYWlsLmNvbSUzYnRydWUlM2IsMTMxODEwODA2ODM0MTU5ODYyLFRydWUsUFNkSlo5SVVJRXNCdHpxY045cFpFMEcxWFptT2VmakhiWXA3cWwvWGp4SEE0OUxjR1BSN2FhNi9NcUxNN2xXalFYZVorWWJaZXN0bDJuVkxGRXpMSmlNRitxSXRFRVFYdGY3QW5CSnpNaURFMlowd3FGQWR4ZEppOTY5djVzTWtsWCtvNmIva3V4NEVJZkZvQitMeTVvYXJwMm9WcVpOUXhmM1RNc0FGbHhKdzZBWmpXRzBZUHRJWjRTdkhmSzRkWWRad215dGNhOVQzOTBrL0xQQkNvWDdYN01XcjlVTlJOSzNFbHV6bVcxcEE3Sys3TmlqSXRCNisyRUJrVTcvYmVocFZXNEI0RkxUa0duZlZPRHdTcUtLem5QMlBmVVFldDgrakR6RnpDZHhSYTRxdWhsOFNqeVRlNGNydmVRb0l6N2RKZlZNR016YXR5SUcwRVJvbktBPT0saHR0cHM6Ly93d3cudXNlcmVkZS5jb20uYnIvc2l0ZXMvZmVjaGFkby9Ib21lU3BhL2luZGV4Lmh0bWw8L1NQPg==',
}

headers = {
    'Authorization': 'undefined undefined',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.userede.com.br/sites/fechado/HomeSpa/index.html',
    'Connection': 'keep-alive',
    'ADRUM': 'isAjax:true',
}

response = requests.get(
    'https://www.userede.com.br/sites/fechado/_vti_bin/SessaoPortal/SessaoServico.svc/consultar', headers=headers, cookies=cookies)

print(response.text)

'''
# Site onde estão os dados
url = "https://pt.wikipedia.org/wiki/Copa_do_Mundo_FIFA"

# Requisicao para obter os dados
r = requests.get(url)

# Obtém os dados do HTML da página
tabelas = pd.read_html(r.text)
# Queremos a tabela com os dados de Público Pagante das Finais da Copa do Mundo
# Essa é a 12° tabela dos dados de retorno
# Então vamos criar um DataFrame com os dados dessa tabela
# lembrando que começamos a contar de 0
df = tabelas[11]

df.head()
# Vamos ajustar o DataFrame usando a linha 0 como título das colunas

# Alterando o título das colunas
df.columns = df.iloc[0]

# Excluindo a linha 0
# O parâmetro inplace=True força que a operação seja realizada no próprio DataFrame
df.drop(df.index[0], inplace=True)

df.head()

# Vamos verificar os tipos de cada coluna
# df.info()

# Qual o maior público pagante?
# print(df['Público pagante'].max())

# Precisamos converter a coluna 'Público pagante' para int
# Mas a conversão não vai ser possível diretamente por conta do '.'
# Então vamos substituir o '.' por nada, e depois converter a coluna para int
# str converte o conteúdo da célula para string (texto)
# replace substitui o '.' por uma string vazia
# astype converte o conteúdo da célula para o tipo especificado, no caso o tipo inteiro
df['Público pagante'] = df['Público pagante'].str.replace('.', '').astype(int)

# Verificando novamente os tipos
df.info()

# Verificando a final da Copa com maior público até hoje
# print(df[df['Público pagante'] == df['Público pagante'].max()])

# Agora vamos fazer um gráfico mostrando a evolução do Público pagante
# nas finais da Copa do Mundo, usando os dados do DataFrame

# Importando a biblioteca
import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib inline

# Exibindo um gráfico de linhas com marcação em cada ponto
sns.pointplot(x='Ano', y='Público pagante', data=df)

# Ajustando legenda dos anos
plt.xticks(rotation=65)
plt.show()
'''
