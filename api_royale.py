from requests import get
import json
import os

# 'https://docs.royaleapi.com/#/endpoints/endpoints'

headers = {
    'auth': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjEzOSwiaWRlbiI6IjQwNTE0NDg3ODczODA0Njk4NyIsIm1kIjp7fSwidHMiOjE1NDQ1NzI4MDE1NzB9.XlbcBZYapP3NhluHUAtJJMcTvvWfJJu7eP9qfZXdWaI",
    }


tag_do_cla = "9JOUG" # farrapos
tag_do_cla = "9Y92GY80" # Disneylandia
nome_do_cla = "Disneylandia"

# remove o arquivo ANTES de salvá-lo dnv
if os.path.isfile("../%s.txt" % nome_do_cla):
    os.remove("../%s.txt" % nome_do_cla)


# url = "https://api.royaleapi.com/clan/%s" % tag_do_cla
# url = "https://api.royaleapi.com/clan/%s/warlog" % tag_do_cla
# url = "https://api.royaleapi.com/clan/%s/history" % tag_do_cla/
# url = "https://api.royaleapi.com/clan/%s/tracking" % tag_do_cla
# url = "https://api.royaleapi.com/top/clans/br"
url = "https://api.royaleapi.com/top/players/br"
# url = "https://api.royaleapi.com/endpoints"
# url = "https://api.royaleapi.com/popular/players?"
# url = "https://api.royaleapi.com/popular/clans?"
# url = "https://api.royaleapi.com/clan/search?name=%s" % nome_do_cla

reponse = get(url, headers=headers)

if reponse:

	dict_salvar = json.dumps(reponse.json(), indent=4, ensure_ascii=False)

	try:
	    # file = open("%s.txt" % nome_do_cla, "w", encoding='utf8')
	    file = open("players_br.txt", "w", encoding='utf8')
	    file.write(dict_salvar)
	    file.close()
	except Exception as erro:
	    print("Ocorreu um erro ao carregar o arquivo.")
	    print("O erro é: {}".format(erro))

else:
	print("Deu ruim!")
	# print(response)


