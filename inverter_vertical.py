from PIL import Image

img = Image.open("imagem.jpg")
imagem_invertida = Image.new('RGB', img.size)

for x, x1 in zip(range(img.width), range(img.width)):
    for y, y1 in zip(range(img.height), range(img.height -1, -1, -1)):
        pixel = img.getpixel((x, y))
        imagem_invertida.putpixel((x1, y1), pixel)

imagem_invertida.show()
