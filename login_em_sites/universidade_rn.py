# coding: utf-8

from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver


class Universidade:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://sigaa.ufrn.br/sigaa/public/docente/busca_docentes.jsf?aba=p-academico'
        self.caixa_busca = 'form:nome' #name

    def navigate(self):
        self.driver.get(self.url)

    def _get_boxes(self):
        return self.driver.find_elements_by_class_name(self.box)

    def _get_search(self):
        return self.driver.find_element_by_name(self.caixa_busca)

    def get_all_data(self):
        campo_busca = self._get_search()
        campo_busca.send_keys('Raquel Carmona Torres Felix')
        # for box in boxes:
        #     print(self._get_title(box).text)

cc = webdriver.Chrome()
c = Universidade(cc)
c.navigate()
c.get_all_data()
