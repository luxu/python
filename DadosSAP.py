# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv('c:/Users/luxu/Desktop/SAP.csv')
df.columns
df.head()
lista = df['NOME'].apply(lambda x: x.split(',')[0])
df.to_csv('c:/Users/luxu/Desktop/nomes.csv',sep=';')
lista_nv = []
for x in lista[:2000]:
    novo = x.split(';')
    if 'seg' in novo[2].lower():
        print(novo)
        lista_nv.append(novo)
len(lista_nv)
lista_nv[0][2]
