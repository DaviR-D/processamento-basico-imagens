from PIL import Image

img = Image.open("imagem.jpg")
imagem_girada = Image.new('RGB', (img.height, img.width))

for x in range(img.width):
    for y in range(img.height):
        pixel = img.getpixel((x, y))
        imagem_girada.putpixel((y, x), pixel)

imagem_girada.show()
