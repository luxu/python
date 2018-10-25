# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from bs4 import BeautifulSoup as bs
import urllib.request

# url = 'http://jenisandrade.blogspot.com.br/2018/01/publicado-os-editais-dos-concursos-de.html'
url = 'http://jenisandrade.blogspot.com/2018/10/convocacao-dos-aevps-nomeados-em-10-08.html'
site = urllib.request.urlopen(url)
soup = bs(site, 'html.parser')

nv = []
# lista = soup.select(".post-outer")
lista = soup.select(".comments")

# print(lista.find_all('p'))
for p in lista:
    print(p)
    # print('Noticia: {}\n{}'.format(p.text,'*'*66))
    nv.append(p)

# for x in nv:
	# print('N.: {}'.format(x.split("\n")))#.find("div.class='hentry'"))
# class="post hentry"
