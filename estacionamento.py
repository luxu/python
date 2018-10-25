#!/usr/bin/env python3
# -*- coding: utf-8 -*-

horarios = []
vagas_guardadas = []
vagas = {
    '1': [0],
    '2': [0],
    '3': [0],
    '4': [0],
    '5': [0],
    '6': [0],
    '7': [0],
    '8': [0],
    '9': [0],
    '10':[0]
}

'''Função que lê a planilha de controle e retorna ela 
formato de arquivo'''
def lerArquivo():
    s = 'entrada.txt'
    with open(s) as _file:
	    text = _file.readlines()
    return text

texto = lerArquivo()

'''Função que salva no dicionário VAGAS que contêm no primeiro elemento
o número da vaga e como segundo elemento uma lista onde vou somando o 
qto aquela vaga arrecadou durante o dia'''
def nro_da_vaga(vagas, vaga, preco, veiculo):
    '''Passo a vaga no indice e vou somando o que já está salvo
    como valor ex. vagas['1':10]'''
    # print(
    #     'Na vaga {} entrou um {} - R$ {} reais'.format(vaga[0], veiculo, preco)
    # )
    vagas['{}'.format(vaga[0])][0] += preco

'''Intera no arquivo e separa em horas joga numa lista'''
for t in range(12):
    # print('Hora{}: {}'.format(t+1, texto[t]))
    horarios.append(texto[t])
    '''Intera na lista de horas e separa numa lista de vagas'''
    # for h in range(12):
    for h in horarios:
        # print('Vaga {}: {}'.format(h, h))
        # print(h)
        vagas_guardadas.append(h)
    horarios = []

'''Primeiro leio vaga por vaga'''
for v in vagas_guardadas:
    '''Depois pego os horários que NÃO estão zerados'''
    if not v.startswith("0"):
        for j in v.split():
            '''Como aqui os dados estão assim 21-3, 
            separo ele em 2 partes ['21','3']'''
            j = j.split('-')
            '''Na segunda posição fica o veículo'''
            if j[1] == '1':
                '''Chamo a função e passo dicionário de vagas, 
                lista das vagas, preço da hora e o veículo'''
                nro_da_vaga(vagas,j, 3, 'moto')
            if j[1] == '2':
                '''Chamo a função e passo dicionário de vagas, 
                lista das vagas, preço da hora e o veículo'''
                nro_da_vaga(vagas,j, 5, 'carro')
            if j[1] == '3':
                '''Chamo a função e passo dicionário de vagas, 
                lista das vagas, preço da hora e o veículo'''
                nro_da_vaga(vagas,j, 10, 'caminhão')

'''No fim mostro os valores arrecadados daquele dia'''
soma = 0
print("Vaga          Valor arrecadado")
for key, value in vagas.items():
    print(u'  {}            R$ {} reais'.format(key,value[0]))
    soma+=value[0]
print(u'{} \nTotal de:   R$ {} reais'.format('-'*40,soma))
'''
Escreva um programa que gerencia um estacionamento de veículos. 
O estacionamento possui 10 amplas vagas em que podem ser estacionados um de três tipos de veículos identificados por códigos:
1 – moto, 2 – carro, 3 – caminhão. 
Para cada tipo de veículo é cobrado um valor de hora diferente, 
- motos pagam 3 reais por hora, 
- carros pagam 5 
- caminhões pagam 10. 

O estacionamento funciona 12 horas por dia e ao final de cada dia de trabalho o programa deve 
emitir um relatório que mostra qual o
- valor arrecadado por vaga  
- total arrecadado naquele dia

Sendo assim, escreva um programa que lê a partir de um arquivo de hora em hora se houve alterações e quais as alterações. 
Ao final das 12 horas, exiba o relatório de lucro por vagas e por último, o valor total arrecadado naquele dia. 
A entrada do programa se dará por um arquivo com 12 linhas, cada uma representa as alterações que ocorreram em cada hora do dia. 
Uma linha apenas com o caractere 0 (“zero”) indica que não houve nenhuma alteração nas vagas. 
As linhas que representam mudanças seguem o formato de pares X-Y, onde X é a vaga alterada e Y é a alteração.
As alterações são representadas por quatro códigos, 
1 representa a entrada de uma moto na vaga X
2 representa a entrada de um carro, 
3 de um caminhão 
4 indica que o veículo na vaga X a deixou. 
Por exemplo, a linha:

1-2 2-4 3-1 6-3 9-4 10-1

Representa que na vaga 1 entrou um carro, a vaga 2 foi liberada, na vaga 3 entrou uma moto, na vaga 6 entrou um caminhão, 
a vaga 9 foi liberada e na vaga 10 entrou uma moto. 
As demais vagas permanecem como estavam na hora anterior. 
Obs.: não é necessário remover um veículo de uma vaga para inserir outro.
Não são aceitos pagamentos parciais, ou seja, se o carro ficou 10 minutos na vaga será cobrada uma hora inteira. 
Após a leitura das alterações das 12 horas deverá ser exibido o valor arrecadado para cada vaga no formato vaga – arrecadação, por exemplo: 

Vaga     Valor arrecadado
10                200 
 9                 178
 5                 160
 6                 155
 7                 130
 1                 120
 2                 115
 3                  90
 4                  80
 8                  56

Além disso, ao final, deverá ser exibido o valor total arrecadado no dia: 1.284

Para o arquivo de entrada: 

1-3 2-1 3-1 4-1 5-1 6-1 7-1 8-1 9-1 10-1 
1-2 2-2 3-2 4-2 5-2 6-2 7-2 8-2 9-2 10-2
0
0
4-3 2-1 3-3 1-1 
0 
0
1-0 2-0 3-0 4-0 5-0 6-0 7-0 8-0 9-0 10-0
0 
9-2 8-1 5-1 7-2
0 
1-1 2-1 3-1 4-1 5-1 6-1 7-1 8-1 9-1 10-1

A saída fica assim:
3-51
4-51
9-46
5-42
8-42
1-37
6-36
7-36
10-36
2-30
417
'''
