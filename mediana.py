from PIL import Image

gray_img = Image.open("imagem_cinza.jpg")

imagem_mediana = Image.new('L', gray_img.size)

for x in range(2,gray_img.width-1):
    for y in range(2,gray_img.height-1):
        gray = gray_img.getpixel((x, y))

        pixels = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                pixels.append(gray_img.getpixel((x + i, y + j)))
        pixels.sort()
        median_value = pixels[4]

        imagem_mediana.putpixel((x, y), median_value)

imagem_mediana.show()
