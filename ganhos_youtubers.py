#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# url = 'https://socialblade.com/youtube/channel/UCBUPPrMmr9TIhEo849cQm-w'
url = 'https://socialblade.com/'
nome_do_youtuber = 'andarilho'

browser = webdriver.Chrome()
browser.get(url)

# browser.find_element_by_name('txt_logindce')
caixaProcurar = browser.find_element_by_xpath('//*[@id="homepage-meta-search-input"]')
btnProcurar = browser.find_element_by_xpath('//*[@id="homepage-meta-search-button"]')
caixaProcurar.send_keys(nome_do_youtuber)
btnProcurar.send_keys(Keys.ENTER)
# sleep(2)
browser.implicitly_wait(2) # seconds
browser.findElement(By.xpath("//a[@href='/youtube/channel']")).click();
# link = browser.find_element_by_xpath('/html/body/div[10]/div[1]/a').click()
# print(link)

def youtuber_selecionado(url_do_youtuber):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	avatar = soup.find("img", {"id": "YouTubeUserTopInfoAvatar"})
	info = soup.find("div", {"id": "YouTubeUserTopInfoBlockTop"})
	for x in info:
		print(x)
		print('-'*50)

# data = popup.find("h3")

# YouTubeUserTopInfoAvatar #id img
# div id="YouTubeUserTopInfoBlockTop"
