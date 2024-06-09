 
from PIL import Image

gray_img = Image.open("imagem_cinza.jpg")

width, height = gray_img.size

imagem_binaria = Image.new('1', (width, height))

threshold = 100

for x in range(width):
    for y in range(height):
        gray_value = gray_img.getpixel((x, y))

        bin_value = 1 if gray_value >= threshold else 0
        imagem_binaria.putpixel((x, y), bin_value)

imagem_binaria.show()
