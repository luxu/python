# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import requests
from bs4 import BeautifulSoup

def run(link, nrrodada):
    if link is None:
        return
    rodada="rodada-{}".format(nrrodada)
    lista = []
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    layout = soup.find_all(class_=rodada)
    for l in layout:
        rodada = l.find("h3").text
        data = l.find("h4").text.split()
        jogos = l.find_all(class_="row")
        for game in jogos:
            nova = game.find_all(class_="full-game")
            for g in nova:
                divhorario = game.find(class_="full-game-time")
                horario = divhorario.find("span").text.strip()
                divnro_jogo = game.find(class_="full-game-location")
                nro_jogo = divnro_jogo.find("strong").text.strip()
                timeCasa = g.find(class_="game-team-1")
                timeFora = g.find(class_="game-team-2")
                timeDaCasa = timeCasa.find("span").text
                timeDeFora = timeFora.find("span").text
                jogo = "{} {} {} : {}".format(nro_jogo, horario, timeDaCasa, timeDeFora)
                lista.append(jogo)
                lista.append(timeDaCasa)
                lista.append(timeDeFora)
    return lista

if __name__ == "__main__":
    base_url = 'https://cbf.com.br/competicoes/brasileiro-serie-a/tabela/2018'
    rodada = 1
    lista = run(base_url,rodada)
# print(lista)

import json
lista_salvar = [ dict(partida=l[:7], horario=l[8:13], jogo=l[14:]) for l in lista ]
dict_salvar = json.dumps(lista_salvar, indent=4, ensure_ascii=False)
diretorio = os.path.abspath('../tabelabr2018/static')
arquivo = diretorio+"/tabelas.json"
try:
    file = open(arquivo, "w", encoding='utf8')
    file.write(dict_salvar)
    file.close()
except Exception as erro:
    print("Ocorreu um erro ao carregar o arquivo.")
    print("O erro é: {}".format(erro))
