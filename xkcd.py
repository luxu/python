#! python
# downloadXkcd.py - Faz download de todas as tirinhas de XKCD

import requests, os, bs4

url = 'http://xkcd.com' # url inicial
os.makedirs('xkcd', exist_ok=True) # armazena as tirinhas em ./xkcd
while not url.endswith('#'):

    # TODO: Faz download da página
    print('Download page {}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # TODO: Encontra o URL da imagem da tirinha
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        comiUrl = 'http:' + comicElem[0].get('src')
        # Faz download da imagem.
        print('Download image {}...'.format(comiUrl))
        res = requests.get(comiUrl)
        res.raise_for_status()

    # TODO: Salva a imagem em ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comiUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # TODO: Obtém o url do botão PREV
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
