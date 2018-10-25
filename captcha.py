from PIL import Image
#Imagem a ser quebrada, neste ponto você poderia usar urlib, httplib ou curl para carregar esta imagem.
img = Image.open('hodo.jpg')
#convertemos para o padrão RGB
img = img.convert("RGBA")
#damos bind da imagem para a variável pixdata
pixdata = img.load()

# Limpando a sujeira do background, se a cor for != black, então transformamos em branco.
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y] != (0, 0, 0, 255):
            pixdata[x, y] = (255, 255, 255, 255)

#Salvamos a nova imagem com fundo branco
img.save("input-black.jpg", "jpg")

#   Aumentamos as dimensões da imagem (requerido pelo OCR)
im_orig = Image.open('input-black.gif')
big = im_orig.resize((116, 56), Image.NEAREST)

#Salvamos a imagem com tamanho maior
ext = ".tif"
big.save("input-NEAREST" + ext)

#   Yeah! Fazemos OCR da imagem usando o Pytesser
from pytesser import *
image = Image.open('input-NEAREST.tif')
#simplesmente imprimimos a imagem em formato de string OCRizado
print(image_to_string(image))
