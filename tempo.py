# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import webbrowser
import os.path
import os, glob
import time

# remove o arquivo ANTES de salvá-lo dnv
if os.path.isfile('tempo.html'):
    os.remove("tempo.html")

def escape_html(data):
    import cgi
    return cgi.escape(data).encode('ascii','xmlcharrefreplace').decode('utf-8')

def montarHTML(lista, listaAmanha={}, listaAgora={}):
    # Salvando arquivo html do resultado

    fobj = open('tempo.html', 'w')

    fobj.write(
    '<html>\n' + '<table style="border: 1px solid black;width: 850px;">\n' +
    '  <thead style="border: 1px solid black;background-color: antiquewhite;width: 400px;">\n'
    + '    <tr>\n<th>' + '</th>\n      <th>'.join(
        escape_html('INSTITUTO, PREVISÃO, MÍNIMA, MÁXIMA, CHUVA').split(
            ',')) + '    </th>\n</tr>\n' + '  </thead>\n' +
    '  <tbody style="border: 1px solid black;background-color: aliceblue;">\n'
    + '    <tr style="text-align: center;">\n')

    for key, value in lista.items():
        fobj.write('<td>{}</td>\n'.format(escape_html(value)))

    if len(listaAmanha) > 0:
        fobj.write('  </tr>\n    <tr style="text-align: center;">\n')
        for key, value in listaAmanha.items():
            fobj.write('<td>{}</td>\n'.format(escape_html(value)))

    fobj.write('  </tr>\n    <tr style="text-align: center;">\n')
    for key, value in listaAgora.items():
        if not 'amanha' in key:
            fobj.write('<td>{}</td>\n'.format(escape_html(value)))

    fobj.write('  </tr>\n    <tr style="text-align: center;">\n')
    for key, value in listaAgora.items():
        if 'amanha' in key:
            fobj.write('<td>{}</td>\n'.format(escape_html(value)))

    fobj.write('</tbody>\n' + '</table>\n' + '</html>\n')

    fobj.close()


def soNumero(campo):
    resultado=''
    for m in campo:
        if m.isdigit():
            resultado += m
    return resultado

def diversos(texto,cidade):
    data = texto.find("div", {"class": "tit"}).text.strip()
    informacoes = texto.find("div", {"class": "prev"})
    minima = soNumero(informacoes(class_="c2")[0].text)
    maxima = soNumero(informacoes(class_="c3")[0].text)
    probabilidade = soNumero(informacoes(class_="c4")[0].text)
    # descricao_do_dia = informacoes(class_="c8")[0].text
    lista = {
        "instituto": "CLIMATEMPO",
        "Data": data,
        "Mínima": minima,
        "Máxima": maxima,
        "Probabilidade": probabilidade,
    }

    return lista

################################################# TEMPOAGORA #################################################

def tempoagora(dia):
    page = requests.get(dia)
    soup = BeautifulSoup(page.content, 'html.parser')

    popup = soup.find_all("div", {"class": "dsp-table"})[1]
    data = popup.find("h3").text
    previsao = popup.find("div", {"class": "description"})

    popupAmanha = soup.find_all("div", {"class": "dsp-table"})[2]
    dataAmanha = popupAmanha.find("h3").text
    previsaoAmanha = popupAmanha.find("div", {"class": "description"})
    # possibilidadeAmanha = previsaoAmanha.find("p").text
    probabilidadeAmanha = previsaoAmanha.find("ul", {"class": "list-inline"}).text.split()
    temp_minAmanha = probabilidadeAmanha[2]
    temp_maxAmanha = probabilidadeAmanha[4]
    probabilidadeAmanha = probabilidadeAmanha[0] + 'mm'
    previsaoAmanha = previsaoAmanha.find("li").text
    # possibilidade = previsao.find("p").text
    probabilidade = previsao.find("ul", {"class": "list-inline"}).text.split()
    temp_min = probabilidade[2]
    temp_max = probabilidade[4]
    probabilidade = probabilidade[0] + 'mm'
    # temp_min = re.findall(r'\d+', temp_min)
    # temp_max = re.findall(r'\d+', temp_max)
    listas = {
            "instituto": "TEMPOAGORA",
            "tituloPrevisaoHoje": data,
            "minimaHoje": temp_min,
            "maximaHoje": temp_max,
            "qtdadeChuvaHoje": probabilidade,
            "amanhaInstituto": "TEMPOAGORA",
            "amanhaTituloPrevisaoHoje": dataAmanha,
            "amanhaMinimaHoje": temp_minAmanha,
            "amanhaMaximaHoje": temp_maxAmanha,
            "amanhaQtdadeChuva": probabilidadeAmanha
        }
    return listas

################################################# CPTEC #################################################

def cptec(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    probabilidade = soup.find_all("div", {"class": "col-md-12"})[0]
    probabilidadeHoje = probabilidade.find_all("div", {"class": "col-md-4 text-center align-middle"})[1].text.split()
    probabilidadeAmanha = probabilidade.find_all("div",
        {"class": "row align-middle justify-content-md-center"})[3]
    dataAmanha = probabilidadeAmanha.find("h5").text
    previsaoAmanha = probabilidadeAmanha.find("figcaption").text
    probabilidade = probabilidadeHoje[3]
    data = soup.find_all("h3", {"class": "block-title"})[0].text.split()
    data = data[5]
    data = data[1:11]
    # previsao = soup.find_all("div", {"class": "p-2"})[10].text
    temperaturas = soup.find("div", {"class": "temperaturas"})
    temp = temperaturas.find_all("span", {"class": "text-center"})
    temp_min = temp[0].text
    temp_min = temp_min[:-1]
    temp_max = temp[1].text
    temp_max = temp_max[:-1]
    listas = {}
    listas = {
        "instituto": "CPTEC",
        "tituloPrevisaoHoje": data,
        "minimaHoje": temp_min,
        "maximaHoje": temp_max,
        "qtdadeChuvaHoje": probabilidade,
        "amanhainstituto": "CPTEC",
        "amanhaTituloPrevisao": dataAmanha,
        "amanhaProbabilidadeAmanha": '0',
        "amanhaMinimaHoje": '0',
        "amanhaPrevisaoAmanha": previsaoAmanha,
    }
    return listas

################################################# CLIMATEMPO #################################################

def climatempo(dia):
    page = requests.get(dia)
    soup = BeautifulSoup(page.content, 'html.parser')

    caixas = soup.find(class_="small-12 large-8 left sticky2Equalizer")
    tit = caixas.find(
        class_="left top10 bold font12 txt-darkgray medium-8 show-for-medium-up"
    ).text.split()
    tituloPrevisao = tit[2] + tit[6] + tit[7]
    qt = caixas.find(
        class_="left text-center small-12 top5 normal font12 txt-black"
    ).text.split()
    qtdadeChuva = qt[0] + qt[1]

    caixa = caixas.find(class_="columns top10 small-12 medium-6")
    maxima = caixa.find(id="tempMax0").text
    minima = caixa.find(id="tempMin0").text

    if (dia ==
            "https://www.climatempo.com.br/previsao-do-tempo/cidade/524/presidenteprudente-sp"):
        lista = {
            "instituto": "CLIMATEMPO",
            "tituloPrevisaoHoje": tituloPrevisao,
            "minimaHoje": minima,
            "maximaHoje": maxima,
            "qtdadeChuvaHoje": qtdadeChuva
        }
    else:
        lista = {
            "instituto": "CLIMATEMPO",
            "tituloPrevisaoAmanha": tituloPrevisao,
            "minimaAmanha": minima,
            "maximaAmanha": maxima,
            "qtdadeChuvaAmanha": qtdadeChuva
        }
    return lista


siteClimatempoHoje = "https://www.climatempo.com.br/previsao-do-tempo/cidade/524/presidenteprudente-sp"
listaClimatempoHoje = climatempo(siteClimatempoHoje)

siteClimatempoAmanha = "https://www.climatempo.com.br/previsao-do-tempo/amanha/cidade/524/presidenteprudente-sp"
listaClimatempoAmanha = climatempo(siteClimatempoAmanha)

siteTempoAgora = 'http://www.tempoagora.com.br/previsao-do-tempo/sp/PresidentePrudente/'
listaTempoAgora = tempoagora(siteTempoAgora)

montarHTML(listaClimatempoHoje, listaClimatempoAmanha, listaTempoAgora)

new = 2
diretorio = os.path.abspath('.')
pagina = "tempo.html"
url = f'{diretorio}/{pagina}'
webbrowser.open(url, new=new)

