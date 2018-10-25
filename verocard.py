from selenium import webdriver
from bs4 import BeautifulSoup
import requests


class Verocard:
    def __init__(self, driver):
        self.driver = driver
        # self.url = "http://www.verocard.com.br/"
        self.url = "https://site.verocard.com.br/apex/f?p=105:105"
        self.caixa_nro = 'P105_CARTAO'  #id
        self.caixa_captcha = 'P105_VALIDACAO_RECAPTCHA'  #id
        self.botao = 'P105_SUBMIT'  #id
        # self.page = requests.get(url)
        # self.soup = BeautifulSoup(page.content, 'html.parser')

    def navigate(self):
        self.driver.get(self.url)

    def search(self, numero=0):
        self.driver.find_element_by_id(self.caixa_nro).send_keys(numero)

        self.driver.find_element_by_id(self.caixa_captcha).send_keys(numero)

        # self.driver.find_element_by_name().click()
        self.driver.find_element_by_id(self.botao).click()


# url = "https://site.verocard.com.br/apex/f?p=105:105"

cc = webdriver.Chrome()
c = Verocard(cc)
c.navigate()
c.search(6064450790280350)
# c.get_all_data()

# tab1 = soup.find(id='tab-1').get_text()
# day.css(".title::attr(data-dia)").extract_first()
# tab1 = soup.find(id='tab-1')
# tab1a = tab1[0]
# for x in tab1:
# print(x)

#         caixas = soup.find(class_="small-12 large-8 left sticky2Equalizer")
#         tit = caixas.find(class_="left top10 bold font12 txt-darkgray medium-8 show-for-medium-up").text.split()
#         tituloPrevisao = tit[2]+tit[6]+tit[7]
#         qt = caixas.find(class_="left text-center small-12 top5 normal font12 txt-black").text.split()
#         qtdadeChuva = qt[0]+qt[1]

#         caixa = caixas.find(class_="columns top10 small-12 medium-6")
#         maxima = caixa.find(id="tempMax0").text
#         minima = caixa.find(id="tempMin0").text

#         if (dia == "https://www.climatempo.com.br/previsao-do-tempo/cidade/524/presidenteprudente-sp"):
#                 lista = {
#                         "tituloPrevisaoHoje" : tituloPrevisao,
#                         "minimaHoje" : minima,
#                         "maximaHoje" : maxima,
#                         "qtdadeChuvaHoje" : qtdadeChuva
#                 }
#         else:
#                 lista = {
#                         "tituloPrevisaoAmanha" : tituloPrevisao,
#                         "minimaAmanha" : minima,
#                         "maximaAmanha" : maxima,
#                         "qtdadeChuvaAmanha" : qtdadeChuva
#                 }
#         return lista
# listaHoje = {}
# listaAmanha = {}
# hoje = "https://www.climatempo.com.br/previsao-do-tempo/cidade/524/presidenteprudente-sp"
# listaHoje = montar(hoje)

# amanha = "https://www.climatempo.com.br/previsao-do-tempo/amanha/cidade/524/presidenteprudente-sp"
# listaAmanha = montar(amanha)

# listas = {}
# listas.update(listaHoje)
# listas.update(listaAmanha)

# print(listas)
# for key,value in listas.items():
#         # print(key,'=>',value)
#         print(key,'=>',value.split())

# def escape_html(data):
#     return cgi.escape(data).encode(
#         'ascii', 'xmlcharrefreplace').decode('utf-8')

# # Salvando arquivo html do resultado
# import cgi

# fobj = open('climatempo.html', 'w')
# fobj.write(
#         '<html>\n' +
#         '<table style="border: 1px solid black;width: 850px;">\n' +
#         '  <thead style="border: 1px solid black;background-color: antiquewhite;width: 400px;">\n' +
#         '    <tr>\n<th>' +
#         '</th>\n      <th>'.join(
#         escape_html('PREVISÃO, MÍNIMA, MÁXIMA, CHUVA').split(',')
#         ) +
#         '    </th>\n</tr>\n' +
#         '  </thead>\n'+
#         '  <tbody style="border: 1px solid black;background-color: aliceblue;">\n'+
#         '    <tr style="text-align: center;">\n'
# )
# for key,value in listaHoje.items():
#         fobj.write('<td>{}</td>\n'.format(escape_html(value)))
# fobj.write('  </tr>\n    <tr style="text-align: center;">\n')
# for key,value in listaAmanha.items():
#         fobj.write('<td>{}</td>\n'.format(escape_html(value)))
# fobj.write(
#         '</tbody>\n' +
#         '</table>\n' +
#         '</html>\n'
# )
# fobj.close()

# import webbrowser
# new = 2
# url = "file://C:/Users/LucianoMartins/Desktop/python/climatempo.html"
# webbrowser.open(url,new=new)
