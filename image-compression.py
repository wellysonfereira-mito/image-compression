from google.colab import drive
from PIL import Image
from IPython.display import display

drive.mount('/content/drive')
caminho_imagem = "/content/drive/My Drive/maltese-1123016_960_720.jpg"
imagem_original = Image.open(caminho_imagem)
def converter_para_cinza(imagem):
  largura, altura = imagem.size
  imagem_cinza = Image.new("L", (largura, altura))  # Escala de cinza

  for y in range(altura):
      for x in range(largura):
          r, g, b = imagem.getpixel((x, y))
          valor_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
          imagem_cinza.putpixel((x, y), valor_cinza)

  return imagem_cinza

def binarizar_imagem(imagem_cinza, limiar=127):
  largura, altura = imagem_cinza.size
  imagem_binaria = Image.new("1", (largura, altura))  # Binária

  for y in range(altura):
      for x in range(largura):
          valor_cinza = imagem_cinza.getpixel((x, y))
          valor_binario = 1 if valor_cinza > limiar else 0
          imagem_binaria.putpixel((x, y), valor_binario)

  return imagem_binaria



imagem_cinza = converter_para_cinza(imagem_original)

imagem_binaria = binarizar_imagem(imagem_cinza)

print("Imagem Original:")
display(imagem_original)

print("Imagem em Tons de Cinza:")
display(imagem_cinza)

print("Imagem Binarizada:")
display(imagem_binaria)