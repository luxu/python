# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from bs4 import BeautifulSoup as bs
import urllib.request

# url = 'https://olhardigital.com.br/'
url = 'http://www2.planalto.gov.br/'
site = urllib.request.urlopen(url)
soup = bs(site, 'html.parser')
# for h2 in soup.find_all('h2'):
print(soup)
# for p in soup.find_all('p'):
#     print('Nóticia: {}'.format(p.text))
# for a in soup.find_parents("a", class="link-gray")
# nv = []
# lista = soup.select(".link-gray")
# for p in lista:
    # print('Nóticia: {}'.format(p.text))
    # nv.append(p)
# for p in nv:
    # print(p.find('a'))
    # print('Nóticia: {}'.format(p.text))
    # print(100*'*')
