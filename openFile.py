from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import sys
import os
# import pyautogui
import threading

sys.path.append(os.getcwd())

arquivoConf = os.path.join(os.getcwd(), sys.argv[1])

with open(arquivoConf) as json_data_file:
    config = json.load(json_data_file)

# E:/geckodriver.exe
# WebDriver driver = new FirefoxDriver()

firefox_profile = webdriver.FirefoxProfile(config['from_nameFirefox'])
browser = webdriver.Firefox(firefox_profile)

num_of_tabs = 10


def restartTabs():

    num_current_tabs = len(browser.window_handles)

    # Fechar todas - 1 abas, deixando uma aberta para não fechar o navegador.
    for i in range(1, num_current_tabs):
        browser.window_handles[i]
        browser.close()
        time.sleep(2)

    # Script para abrir as páginas.
    for total_new_tabs in range(1, num_of_tabs):
        browser.execute_script("window.open('','_blank');")

        # Foca na última aba aberta
        browser.switch_to_window(browser.window_handles[-1])
        time.sleep(2)

    # Fecha a aba remanescente das anteriormente fechadas.
    browser.windows_handles[0].close()

    startTimer()


def startTimer():
    t = threading.Timer(30.0, restartTabs)
    t.start()


restartTabs()
