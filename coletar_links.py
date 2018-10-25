from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())
allExtLinks = set()
allIntLinks = set()

#Recupera uma lista de todos os links externos encontrados em uma página
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []
	#encontra todos os links que começam com "http" ou "www" que não contêm i URL atual
	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

#Recupera uma lista de todos os links internos encontrados em uma página
def getInternalLinks(bsObj, excludeUrl):
	externalLinks = []
	#encontra todos os links que começam com "http" ou "www" que não contêm a URL atual
	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	return address.replace("http://","").split("/")

#Coleta uma lista de todas as URLs externas encontradas no site
def getAllExternalLinks(siteUrl):
	html = urlopen(siteUrl)
	bsObj = BeautifulSoup(html, "lxml")
	internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
	externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allIntLinks:
			print("About to get link: "+link)
			allIntLinks.add(link)
			getAllExternalLinks(link)

getAllExternalLinks("https://www.luxu.com.br")
