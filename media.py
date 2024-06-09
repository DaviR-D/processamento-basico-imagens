from PIL import Image

gray_img = Image.open("imagem_cinza.jpg")

imagem_media = Image.new('L', gray_img.size)

for x in range(2,gray_img.width-1):
    for y in range(2,gray_img.height-1):
        gray = gray_img.getpixel((x, y))
        mean_value = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                mean_value += gray_img.getpixel((x + i, y + j))
        mean_value //= 9

        imagem_media.putpixel((x, y), mean_value)

imagem_media.show()
