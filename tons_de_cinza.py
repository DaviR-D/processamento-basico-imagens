from PIL import Image

img = Image.open("imagem.jpg")
imagem_cinza = Image.new('L', img.size)

for x in range(img.width):
    for y in range(img.height):
        r, g, b = img.getpixel((x, y))
        gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)
        imagem_cinza.putpixel((x, y), gray_value)

imagem_cinza.show()

