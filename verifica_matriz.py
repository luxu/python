#!/usr/bin/python
# -*- coding: utf-8 -*-

def verificamatriz(m):
    if len(m) != 4:
        return 0
    return 1

def multiplica_matriz():
    return x[0] * y[1] * z[2] * w[3]

x=[5,5,6,6]
y=[7,7,8,8]
z=[9,9,1,0]
w=[4,4,3,3]
i=0
if verificamatriz(x):
    i+=1
    if verificamatriz(y):
        i+=1
        if verificamatriz(z):
            i+=1
            if verificamatriz(w):
                i+=1
if i >= 4:
    print(multiplica_matriz())
else:
    print("Não é matriz quadrada!!")
