import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

resul = pd.read_csv(
	"consulta_cand_2018_SP.csv",
	encoding='cp1251',
	sep=';',
	header=0
)

def isCity(city):
    if 'prudente'.upper() in city:
        return True
    else:
        return False

columns = resul.columns

candidatos_prudente = resul[
		resul['NM_MUNICIPIO_NASCIMENTO'] == 'PRESIDENTE PRUDENTE'
	]
['NM_CANDIDATO']

idade_minima = resul[resul['DT_NASCIMENTO']==resul['DT_NASCIMENTO'].min()]

x = sum(resul['NM_MUNICIPIO_NASCIMENTO'].apply(lambda x: isCity(x)))

# for x in columns:
# 	# print(x)
# 	if x.startswith('C'):
# 		print(x)

qt_menor_candidatos_por_municipio =	resul['NM_MUNICIPIO_NASCIMENTO'].value_counts() > 1
def maior_que_um(x):
	if x == 'AGOGADOS DO INGAZEIRA':
		return x
	return ''

contMaisDeUm = 0
contMenosDeUm = 0
for x in resul['NM_MUNICIPIO_NASCIMENTO'].value_counts() < 2:
	if x:
		contMenosDeUm+=1
	else:
		contMaisDeUm+=1

nome_dep_estadual = resul[
(resul['DS_CARGO'] != 'DEPUTADO ESTADUAL') & (resul['NM_URNA_CANDIDATO'] == 'DR. TALMIR')
]['NM_MUNICIPIO_NASCIMENTO']

nro_dep_estadual = resul[
(resul['DS_CARGO'] != 'DEPUTADO ESTADUAL') & (resul['NM_URNA_CANDIDATO'] == 'DR. TALMIR')
]['NR_CANDIDATO']

for nome,nro in zip(nome_dep_estadual,nro_dep_estadual):
	print(nome, nro)

# print(
# resul[resul['NM_CANDIDATO'] == 'MILTON CARLOS DE MELLO']['NR_CANDIDATO']
# )

# resul[resul['NM_MUNICIPIO_NASCIMENTO'] == 'PRESIDENTE PRUDENTE']['NM_CANDIDATO']

# print (
# 	resul[
# 	(resul['NM_MUNICIPIO_NASCIMENTO'] == 'SAO PAULO') & (resul['NM_MUNICIPIO_NASCIMENTO'].value_counts() < 2)
# 	]
# )