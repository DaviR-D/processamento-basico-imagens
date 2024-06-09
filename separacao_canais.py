from PIL import Image


img = Image.open("imagem.jpg")
width, height = img.size


vermelho = Image.new("RGB", (width, height))
verde = Image.new("RGB", (width, height))
azul = Image.new("RGB", (width, height))

for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        vermelho.putpixel((x, y), (r, r, r))
        verde.putpixel((x, y), (g, g, g))
        azul.putpixel((x, y), (b, b, b))


vermelho.show()
verde.show()
azul.show()
