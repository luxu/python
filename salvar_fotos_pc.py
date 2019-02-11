from requests import get
from bs4 import BeautifulSoup as bs
from shutil import copyfileobj
import os

html = get('http://www.afterfest.com.br/mr-moo-4a-edicao/')
soup = bs(html.content, 'html.parser')

def download_file(name, url, pasta):
    os.makedirs(pasta, exist_ok=True) # armazena as na pasta
    xpto = get(url, stream=True)
    # with open(name, 'wb') as f:
    #     copyfileobj(xpto.raw, f)
    with open(u'{}/{}'.format(pasta,name), 'wb') as f:
        copyfileobj(xpto.raw, f)
    # imageFile = open(os.path.join(diretorio, xpto), 'wb')
    # for chunk in res.iter_content(100000):
    #     imageFile.write(chunk)
    # imageFile.close()

images = [i.a['href'] for i in soup.findAll('div', class_="thumbnail-image")]

for image in images[2:10]:
    _image = image.split('/')
    name = image.split('/')[-1]
    pasta = u'_'.join([_image[4],_image[5],_image[6]])
    print(name)
    print(pasta)
    # download_file('{}.jpg'.format(image[0]), image, pasta)
    download_file(name, image, pasta)
print(len(images))
