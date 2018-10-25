import os

def lerSql(s):
    with open(s, encoding="utf8") as _file:
        text = _file.read()
    return text

def lerSql2(s):
    with open(s, encoding="utf8") as f:
        linhas = f.readlines()[41:]
    return linhas

def criarCabecalho(tabela):
	cabecalho = list()
	nro_linha = 1
	for l in tabela.split('\n'):
		if 'INSERT INTO' in l:
			nrolinha=nro_linha
			cabecalho = l.split('`')
			# print(cabecalho)
		nro_linha += 1
	cabecalho1=cabecalho[3].split('CT_')[1]
	cabecalho2=cabecalho[5].split('CT_')[1]
	cabecalho3=cabecalho[7].split('CT_')[1]
	cabecalho4=cabecalho[9].split('CT_')[1]
	tabela = dict(cabecalho1=cabecalho1,
		cabecalho2=cabecalho2,
		cabecalho3=cabecalho3,
		cabecalho4=cabecalho4,
		nrolinha=nrolinha
	)
	return tabela

def criarCorpo(dicionario, tabela):
	lista2 = list()
	lista3 = list()

	for l in tabela:
		# print(l.split('\n')[0])
		lista2.append(l.split('\n')[0])
	for l in lista2:
		lista3.append(l.split(','))
		# print(l.split(','))
	for l in lista3:
		nome_da_cidade = l[1].strip()
		codigo_do_estado = l[2]
		print(nome_da_cidade, codigo_do_estado)
		dicionario = dict(
			nome_da_cidade=nome_da_cidade,
			codigo_do_estado=codigo_do_estado
		)
	return dicionario

# arquivo = "cidadess.sql"
arquivo = "city.sql"
tabela = lerSql(arquivo)
tabela2 = lerSql2(arquivo)
dicionario = dict()
dicionario = criarCabecalho(tabela)
dicionario = criarCorpo(dicionario, tabela2)
for index,value in dicionario.items():
	print(value)
