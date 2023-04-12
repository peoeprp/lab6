from PIL import Image, ImageDraw, ImageFont
def n1():
    im=Image.open('otkr1.jpg')
    im.show()
    im=im.crop((100, 75, 450, 350))
    im.show()
    im.save("new_otkr1.jpg")
n1()

def n2():
    print("Данному коду доступны праздники: 8 марта, 23 февраля, 1 апреля, Новый год")
    sp={"8 марта": "8mart.jpg", "23 февраля" : "23fev.jpg", "1 апреля": "1prl.jpg","Новый год": "ng.jpg"}
    pr=input("Выберите праздник из списка: ")
    im=sp[pr]
    image = Image.open(im)
    image.show()
n2()

def n3():
    im=Image.open("dr.jpg")
    name=input("Введите имя того, кого хотите поздравить: ")
    text = str(name) + ", Поздравляю!"
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype("gogol_regular.otf", size=65)
    draw_text.text(
        (1000, 100),
        text, font=font,
        fill=('#1C0606')
    )
    im.show()
    im.save("drnew.jpg")
n3()
