
from PIL import Image
def n12():
    image = Image.open('orig.jpg')
    image.show()
    print("Размер изображения: ",image.size)
    print("Формат изображения: ", image.format)
    print("Цветовая модель изображения: ", image.mode)
    im2 = image.reduce(3)
    im2.save('orig-3.jpg')
    im3 = image.rotate(90)
    im3.save('orig-4.jpg')
    im4 = image.transpose(Image.FLIP_LEFT_RIGHT)
    im4.save('orig-5.jpg')
n12()
import os
from PIL import Image, ImageFilter
import os.path
def n3():
    #os.mkdir("pictures")
    for i in range(1,6):
        im=str(i)+'.jpg'
        with Image.open(im) as img:
            gray_img = img.convert("L")
            gray_img = gray_img.show()
            gray_img.save('pictures/'+str(im))
n3()
def n4():
    k=int(input("Сколько изображений вы хотите обработать?: "))
    for i in range(0,k):
        g=str(i)+'.jpg'
        image_path=input("Введите название изображения, включая .jpg: ")
        watermark_path=input("Введите название водяного знака, включая .png: ")
        im = Image.open(image_path)
        watermark = Image.open(watermark_path)
        watermark1 = watermark.reduce(3)
        im.paste(watermark1, (1,1))
        im.show()
        im.save(str(g))
n4()




