
import os
import csv
from PIL import Image, ImageFilter
import os.path
def n1():
    #os.mkdir("pictures_new")
    myPath=os.getcwd()
    a=len([f for f in os.listdir(myPath)
         if f.endswith('.jpg') and os.path.isfile(os.path.join(myPath, f))])
    b=[f for f in os.listdir(myPath)
         if f.endswith('.jpg') and os.path.isfile(os.path.join(myPath, f))]
    for i in range(a):
        im=str(b[i])
        with Image.open(im) as img:
            img = img.filter(ImageFilter.CONTOUR)
            img.save('pictures_new/'+im+".jpg")
            img.show()
#n1()

def n2():
    # os.mkdir("pictures_new")
    myPath = os.getcwd()
    r=input("Изображения какого расширения вы хотите обработать?: ")
    if r=='.jpg':
        a = len([f for f in os.listdir(myPath)
                 if f.endswith('.jpg') and os.path.isfile(os.path.join(myPath, f))])
        b = [f for f in os.listdir(myPath)
             if f.endswith('.jpg') and os.path.isfile(os.path.join(myPath, f))]
        for i in range(a):
            im = str(b[i])
            with Image.open(im) as img:
                img = img.filter(ImageFilter.CONTOUR)
                #img.save('pictures_new/' + im + r)
                img.show()
    if r=='.png':
        a = len([f for f in os.listdir(myPath)
                 if f.endswith('.png') and os.path.isfile(os.path.join(myPath, f))])
        b = [f for f in os.listdir(myPath)
             if f.endswith('.png') and os.path.isfile(os.path.join(myPath, f))]
        for i in range(a):
            im = str(b[i])
            with Image.open(im) as img:
                img = img.filter(ImageFilter.CONTOUR)
                #img.save('pictures_new/' + im + r)
                img.show()
#n2()

def n3():
    with open("data.csv") as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        sum=0
        st=1
        print("Нужно купить: ")
        for row in file_reader:
            print(f'    {row[0]} - {row[1]} шт. за  {row[2]} руб.')
            st=int(row[1]) * int(row[2])
            sum+=st
            count += 1
    print("Итоговая сумма: ", sum, " руб." )
n3()

