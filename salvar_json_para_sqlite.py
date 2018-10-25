# -*- coding: utf-8 -*-

import sqlite3
import json
from pprint import pprint

def ler_json():
    with open('tabelas.json', encoding="utf-8") as f:    
        datas = json.load(f)

    criar_banco()
    for data in datas:
        for d in datas:
            insert_data(d)
        break

def criar_banco():
    # definindo um cursor
    cursor = conn.cursor()

    # criando a tabela (schema)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tabelas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            rodada INTEGER,
            horario     VARCHAR(255) NOT NULL,
            jogo     VARCHAR(255) NOT NULL,
            timedacasa INTEGER,
            timedefora INTEGER,
            createdAt DATETIME,
            updatedAt DATETIME
    );
    """)

    print('Tabela criada com sucesso.')

def insert_data(dados):
    cursor = conn.cursor()

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO tabelas (rodada, horario, jogo, timedacasa, timedefora, createdAt)
    VALUES (?,?,?,?,?,?)
    """, (int(dados['rodada'][6:]), dados['horario'], dados['jogo'], dados['timeDaCasa'], dados['timeDeFora'], '2018-04-28'))

    # gravando no bd
    conn.commit()

    print('Dados inseridos com sucesso.')

# conectando...
nome_banco = 'br2018.db'
conn = sqlite3.connect(nome_banco)
# criar_banco(conn)
dados = ler_json()
conn.close()
