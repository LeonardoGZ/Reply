#Importando bibliotecas
import glob
import os
from PIL import Image
from pathlib import Path
from tkinter import filedialog

#declarando variavel do incrementador
i = 0
j = 0
size = 4 * 1024 * 1024  # 4MB
#atribuindo à variaveis as pastas selecionadas
    #path é a pasta onde os arquivos estão
    #path1 é pasta de destino das fotos editadas 
path = filedialog.askdirectory()
path1 = filedialog.askdirectory()

#atribuindo a lista com as fotos da pasta de origem 
imagens = glob.glob(path + '/*.JPG', recursive = True) 
imagenseditadas = glob.glob(path1 + '/*.JPG', recursive = True)

#Laço de repetição 
    
for imagem in imagens:
    #Importação das imagens 
    imagem = Image.open(imagens[i])
    ic = str([i])
   
    print(os.path.getsize(imagens[i]))
    img = imagem.save(path1 + "/imagem.JPG",optimize = True, quality = 100)
    os.rename(path1 + '/imagem.JPG',path1 +  "/imagem %s.JPG"%ic)
    print(os.path.getsize(path1 +  "/imagem %s.JPG"%ic))
    print(size)

    #q=100

    #while os.path.getsize(path1 +  "/imagem %s.JPG"%ic) > size and q > 0:
    #    print(os.path.getsize(path1 +  "/imagem %s.JPG"%ic))
     #   imagem.save(path1 +  "/imagem %s.JPG"%ic, optimize = True, quality = q)
     #   q = q -1
        
    
    #Descrição das dimençôes das imagens
    width, height = imagem.size 
    print(imagem.size)
    #transformando o incrmentador em string
  
    
    #while os.path.getsize(imagens[i]) > size:
    #img.save(path1 +  "/imagem %s.JPG"%ic, optimize=True, quality=85)

    #img = imagem.save(path1 + "/imagem.JPG")
    #os.rename(path1 + '/imagem.JPG',path1 +  "/imagem %s.JPG"%ic)

    # Comprima a imagem para 4MB ou menos
    #while os.path.getsize(path1 +  "/imagem %s.JPG"%ic) > size:
     #   img.save(path1 +  "/imagem %s.JPG"%ic, optimize=True, quality=85)
    #rotacionando a imagem em 180 graus
    img180 = imagem.rotate(180)
    img180 = img180.save(path1 + "/imagem180.JPG")
    #enumerando as imagens editadas 
    os.rename(path1 + '/imagem180.JPG',path1 +  "/imagem180 %s.JPG"%ic)
    
    #q=100

    #while os.path.getsize(path1 +  "/imagem180 %s.JPG"%ic) > size and q > 0:
     #   print(os.path.getsize(path1 +  "/imagem180 %s.JPG"%ic))
      #  imagem.save(path1 +  "/imagem180 %s.JPG"%ic, optimize = True, quality = q)
       # q = q -1
    #rotacionando a imagem em 90 graus
    """img90 = imagem.rotate(90, expand=True)
    img90 = img90.save(path1 +  "/imagem90.jpg")
    #enumerando as imagens editadas 
    os.rename(path1 + '/imagem90.jpg',path1 +  '/imagem90 %s.jpg'%ic)
    #rotacionando a imagem em 270 graus
    img270 = imagem.rotate(270, expand=True)
    img270 = img270.save(path1 + "/imagem270.jpg")
    #enumerando as imagens editadas 
    os.rename(path1 + '/imagem270.jpg',path1 +  '/imagem270 %s.jpg'%ic)
    #espelha a imagem horizontalmente
    hori_flippedIma = imagem.transpose(Image.FLIP_LEFT_RIGHT)
    hori_flippedIma = hori_flippedIma.save(path1 + "/imagem270.jpg")
    #enumerando as imagens editadas
    os.rename(path1 + '/imagem270.jpg',path1 +  '/imagemhori_flipped %s.jpg'%ic)
    #espelha a imagem verticalmente
    Vert_flippedImage = imagem.transpose(Image.FLIP_TOP_BOTTOM)
    Vert_flippedImage = Vert_flippedImage.save(path1 + "/imagem270.jpg")
    #enumerando as imagens editadas
    os.rename(path1 +  '/imagem270.jpg',path1 +  '/imagemVert_flipped %s.jpg'%ic)"""

    
    i = i + 1 

print('modificação concluida')
j = i/6
i = 0
imagenseditadas = glob.glob(path1 + '/*.JPG', recursive = True)

for imageme in imagenseditadas:
    #Importação das imagens 
    imageme = Image.open(imagenseditadas[i])
    ic = str([i])
    

    q=100

    while os.path.getsize(imagenseditadas[i]) > size and q > 0:
        print(os.path.getsize(imagenseditadas[i]))
        imageme.save(imagenseditadas[i], optimize = True, quality = q)
        q = q -1
    
    i = i + 1 
    if i == j 
        i = 0  

    #os.rename(path1 + '/imagem.JPG',path1 +  "/imagem %s.JPG"%ic)

print('Concluido')
#fim do programa

