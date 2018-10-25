#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql.cursors
import pymysql
import sys
import os
import json
import configparser

# Carrega as configurações de arquivo externo
config = configparser.ConfigParser()
config.read('config.ini')


def banco_local_remoto(banco):
    if banco != 'local':
        connection = pymysql.connect(host=config['fabrizio']['host'],
                                     user=config['fabrizio']['user'],
                                     password=config['fabrizio']['password2'],
                                     db=config['fabrizio']['db'],
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    else:
        connection = pymysql.connect(host=config['local']['host'],
                                     user=config['local']['user'],
                                     password=config['local']['password'],
                                     db=config['local']['db'],
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    return connection

def conexao(connection,tbl=None):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            # sql = u"SELECT {} FROM {}".format(campos(),tabela())
            if tbl:
                sql = u"SELECT * FROM {}".format(tabela(tbl))
            else:
                sql = u"SELECT * FROM information_schema.tables WHERE table_schema = {}".format(config['fabrizio']['db'])
            # sql = "SELECT * FROM `profissionais`" # WHERE `email`=%s"
            # sql = "SELECT * FROM `agendas` WHERE `profissional_ID`=%s"
            # cursor.execute(sql, (216))
            cursor.execute(sql)
            listar_dados_banco = cursor.fetchall()
            return listar_dados_banco
    finally:
        connection.close()

def nomeTabelas(connection):
    nome = conexao(connection)
    nome_tabelas = []
    for n in nome:
        nome_tabelas.append(n['TABLE_NAME'])
    salvar = json.dumps(nome_tabelas, indent=4, ensure_ascii=False)
    arquivo = 'TabelasBanco.json'
    try:
        file = open(arquivo, "w", encoding='utf8')
        file.write(salvar)
        file.close()
    except Exception as erro:
        print("Ocorreu um erro ao carregar o arquivo.")
        print("O erro é: {}".format(erro))

def tabela(nome):
    print(u"função: Tabela.: {}".format(nome))
    return nome

def campos():
    return u"{},{},{}".format('id','nome','email')

def cabecalho(listar_dados_banco):
    cabecalho = []
    corpo = []
    for dados in listar_dados_banco:
        for key, value in dados.items():
            corpo.append(u'{} : {}'.format(key,value))
    return corpo

def consultar(connection,nome_conexao,tbl):
    arquivo = u'Tabela{}-{}.json'.format(tbl.upper(),nome_conexao.upper())
    listar_dados_banco = conexao(connection,tbl)
    corpo = cabecalho(listar_dados_banco)
    campos = []
    file = open(arquivo, "w", encoding='utf8')
    for dados in corpo:
        if dados.startswith("ID"):
            file.write('--------------------\n')
        file.write(json.dumps(
            dados, indent=4, sort_keys=True, ensure_ascii=False, default=str)+'\n')
    file.close()
    return

if __name__ == "__main__":
    try:
        nome_conexao = sys.argv[1]
        connection = banco_local_remoto(sys.argv[1])
        consultar(connection,nome_conexao,sys.argv[2])
        # nomeTabelas(connection)
    except:
        os.system("cls")
        print(u'\n{}\n\nNão esqueça de colocar dessa forma: mysql.py <LOCAL ou REMOTO> <TABELA>\n\n{}\n'.format('*'*80,'*'*80))
        sys.exit(0)
        # print(nomeTabelas(connection))