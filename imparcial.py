# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import os
import os.path

# remove o arquivo ANTES de salvá-lo dnv
if os.path.isfile('resultado.html'):
    os.remove("resultado.html")

# pega o html do conteudo da pagina
html = requests.get(
    'http://www.imparcial.com.br/classificados'
).content.decode('utf-8')

# separa o html em uma lista das galerias que existe "categorias"
html_gallery_item = html.split('"gallery-item"')[1:]

# variavei que vai conter a minha lista de resultados
categorias = []

# loopa as partes do html que contem cada categoria
for gi in html_gallery_item:
    # cria um dicionario com o nome da gategorias e uma lista vazia dos anuncios
    categoria = dict(
        # procura na parte a cadeia de caracteres "<div.." pega o que tem depois,
        # procura no resultado a cadadei de caractes "<" e pega o q tem antes
        titulo=gi.split('<div class="title">')[1].split('<')[0],
        anuncios=[]
    )
    # separa o html em uma lista dos anuncios que existe na categoria que esta
    html_itens = gi.split('<div class="col-md-12 col-sm-12">')[1:]
    for item in html_itens:
        # se nao tiver os caracteres de um anuncio ignora
        if '<div class="title"><span class="block-intitle">' not in item:
            continue
        anuncio = dict(
            # procura na parte a cadeia de caracteres "<div.." pega o que tem depois,
            # procura no resultado a cadadei de caractes "<" e pega o q tem antes
            subcategoria=item.split(
                '<div class="title"><span class="block-intitle">'
            )[1].split('</span>')[0].strip(),
            # procura na parte a cadeia de caracteres "<div.." pega o que tem depois,
            # procura no resultado a cadadei de caractes "<" e pega o q tem antes
            titulo=item.split('</span>')[1].split('</div>')[0].strip(),
            # procura na parte a cadeia de caracteres "<div.." pega o que tem depois,
            # procura no resultado a cadadei de caractes "<" e pega o q tem antes
            descricao=item.split(
                '<div class="contents">'
            )[1].split('</div>')[0].strip(),
        )
        categoria['anuncios'].append(anuncio)
    categorias.append(categoria)

# pronto agora basta usar seus dados
listas = []
# anda no seu objeto imprimindo
for categoria in categorias:
    for anuncio in categoria['anuncios']:
        if anuncio['subcategoria'] == 'EMPREGOS':
            # print('Emprego: {}'.format(anuncio))
            # print('-'*100)
            listas.append(anuncio['titulo']),
            listas.append(anuncio['descricao']),
            listas.append('-'*100),

# Salvando os arquivo resultado.js para o programador front-end web fazer a pagina
import cgi

def escape_html(data):
    return cgi.escape(data).encode(
        'ascii', 'xmlcharrefreplace').decode('utf-8')

# open('resultado.js', 'w').write(json.dumps(dict(resultados=categorias)))

# Salvando arquivo html do resultado
fobj = open('resultado.html', 'w')
fobj.write(
    '<html>\n' +
    '<table>\n' +
    '  <thead>\n' +
    '    <tr>\n<th>' +
    '</th>\n      <th>'
    '    </tr>\n' +
    '  </thead>\n'+
    '  <tbody>\n'
)
for x in listas:
    fobj.write(
            '    <tr>\n<td>' +
            '</td>\n      <td>'.join([
                escape_html(x),
            ]) +
            '    </tr>\n'
        )
fobj.write(
    '  </tbody>\n' +
    '</table>\n' +
    '</html>\n'
)
fobj.close()

import webbrowser

new = 2
diretorio = os.path.abspath('.')
pagina = "resultado.html"
url = f'{diretorio}/{pagina}'
webbrowser.open(url, new=new)
# time.sleep(15)

# for file in glob.glob("*.html"):
    # print(file)

# print(url)
# filedirlist = os.listdir(".")
# filelist = [os.path.abspath(f) for f in filedirlist if os.path.isfile(f)]
# dirlist  = [os.path.abspath(d) for d in filedirlist if os.path.isdir(d)]

# Lista de arquivos com path completo.
#for i in filelist:
  #  print(i)

# Lista de diretórios com path completo.
#for i in dirlist:
  #  print(i)

