#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import datetime

login = 'seuemail@email.com'
password = 'suasenha'

# self.url = "https://site.verocard.com.br/apex/f?p=105:105"
# self.caixa_nro = 'P105_CARTAO'  #id
# self.caixa_captcha = 'P105_VALIDACAO_RECAPTCHA'  #id
# self.botao = 'P105_SUBMIT'  #id

def initiateSelenium():
    try:
        #Pega caminho do script , pra acessar o chromedriver
        dirpath = os.getcwd()
        #Option pra evitar alguns erros, talvez possa ser removida
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        #Inicia driver
        # driver = webdriver.Chrome(executable_path=r"%s/chromedriver.exe" % dirpath, chrome_options=chrome_options)
        driver = webdriver.Chrome()
        return driver
    except Exception as e:
        print('Error on initiateSelenium(): %s' % str(e))
        raise

def go():
    try:
        driver = initiateSelenium()
        #Acessa url de login
        url = "https://site.verocard.com.br/apex/f?p=105:105"
        driver.get(url)
        # driver.get('https://pt.expertoption.com/login')
        #Encontra campos login/pw via xpath
        # user_input = driver.find_element_by_xpath("//input[@name='email']")
        # pw_input = driver.find_element_by_xpath("//input[@name='password']")
        nro_cartao = '6064450790280350'
        idinput1 = '//*[@id="P105_CARTAO"]'
        idcaptcha = '//*[@id="recaptcha-anchor"]/div[1]'
        idbotao = '//*[@id="B560900111699388687"]'
        nro = driver.find_element_by_xpath(idinput1)
        botao = driver.find_element_by_xpath(idbotao)
        # find element by xpath(xpath).click()
        captcha = driver.find_element_by_xpath(idcaptcha).click()
        #Preenche campos
        nro.send_keys(nro_cartao)
        # captcha.send_keys(password)
        # botao.click()
        # user_input.send_keys(login)
        # pw_input.send_keys(password)
        #Encontra form via xpath e clica no botao login
        form = driver.find_element_by_class_name('form-holder')
        btn = form.find_element_by_xpath(".//button[@class='button fill full small']")
        btn.click()
        #Aguarda o load da proxima pagina (max 30 segundos), onde o amount-input aparece
        WebDriverWait(driver, 30).until(
         EC.visibility_of_element_located((By.CLASS_NAME, "amount-input"))
        )

        #Roda indefinidamente
        while True:
            inputs = driver.find_elements_by_class_name('amount-input')
            print('Price at: %s is %s' % (datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),inputs[1].text))
            print('Saving to DB (chamar funcao de save no banco)')
            time.sleep(1)
    except Exception as e:
        print('Error on go(): %s' % str(e))

go()