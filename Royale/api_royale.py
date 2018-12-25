import pandas as pd
import datetime
import json
import pandas as pd
from requests import get

headers = {
    'auth': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjEzOSwiaWRlbiI6IjQwNTE0NDg3ODczODA0Njk4NyIsIm1kIjp7fSwidHMiOjE1NDQ1NzI4MDE1NzB9.XlbcBZYapP3NhluHUAtJJMcTvvWfJJu7eP9qfZXdWaI",
}

inicio = datetime.datetime.now()
df = pd.read_csv('contries.csv')
tabela = []
for country in range(100,105):
	pais = df.loc[country, ['key','name']]
	url = u"https://api.royaleapi.com/top/players/%s" % pais['key']
	reponse = get(url, headers=headers)
	for r in reponse.json():
		item = {}
		try:
			item['name_pais'] = pais['name']
			item['name'] = r['name']
			item['tag'] = r['tag']
			item['rank'] = r['rank']
			item['expLevel'] = r['expLevel']
			item['trophies'] = r['trophies']
			if 'clan' in r:
				item['name_clan'] = r['clan']['name']
				item['tag_clan'] = r['clan']['tag']
			else:
				item['name_clan'] = None
				item['tag_clan'] = None
			item['name_arena'] = r['arena']['name']
			tabela.append(item)
			print(tabela)
		except Exception as e:
			continue

fim = datetime.datetime.now()
dict_salvar = json.dumps(tabela, indent=4, ensure_ascii=False)
try:
    file = open(u"players.json", "w", encoding='utf8')
    file.write(dict_salvar)
    file.close()
except Exception as erro:
    print("Ocorreu um erro ao carregar o arquivo.")
    print("O erro é: {}".format(erro))

# passar de json para csv

file_name = u'players.csv'
df = pd.read_json('players.json')
df.to_csv(file_name, encoding='utf-8', index=False)
print(fim - inicio)
