import glob
import os
from PIL import Image

i = 0
imagens = glob.glob('Replicação de fotos\Fotos\**\*.jpg', 
                   recursive = True)                  
for imagem in imagens:
    imagem = Image.open(imagens[i])
    width, height = imagem.size
    print(imagem.size)
    ic = str([i])
    img180 = imagem.rotate(180)
    img180 = img180.save("Replicação de fotos\Fotoseditadas\imagem180.jpg")
    os.rename('Replicação de fotos\Fotoseditadas\imagem180.jpg', "Replicação de fotos\Fotoseditadas\imagem180 %s.jpg"%ic)
    img90 = imagem.rotate(90, expand=True)
    img90 = img90.save("Replicação de fotos\Fotoseditadas\imagem90.jpg")
    os.rename('Replicação de fotos\Fotoseditadas\imagem90.jpg', 'Replicação de fotos\Fotoseditadas\imagem90 %s.jpg'%ic)
    img270 = imagem.rotate(270, expand=True)
    img270 = img270.save("Replicação de fotos\Fotoseditadas\imagem270.jpg")
    os.rename('Replicação de fotos\Fotoseditadas\imagem270.jpg', 'Replicação de fotos\Fotoseditadas\imagem270 %s.jpg'%ic)
    hori_flippedIma = imagem.transpose(Image.FLIP_LEFT_RIGHT)
    hori_flippedIma = hori_flippedIma.save("Replicação de fotos\Fotoseditadas\imagem270.jpg")
    os.rename('Replicação de fotos\Fotoseditadas\imagem270.jpg', 'Replicação de fotos\Fotoseditadas\imagemhori_flipped %s.jpg'%ic)
    Vert_flippedImage = imagem.transpose(Image.FLIP_TOP_BOTTOM)
    Vert_flippedImage = Vert_flippedImage.save("Replicação de fotos\Fotoseditadas\imagem270.jpg")
    os.rename('Replicação de fotos\Fotoseditadas\imagem270.jpg', 'Replicação de fotos\Fotoseditadas\imagemVert_flipped %s.jpg'%ic)
    i = i + 1

print('acabou')
