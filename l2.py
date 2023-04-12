def n1():
    password = input('Введите пароль: ')
    is_numeric = False
    is_upper = False
    is_lower = False
    is_spec = False
    for char in password:
        if char.isnumeric():
            is_numeric = True
        elif char.islower():
            is_lower = True
        elif char.isupper():
            is_upper = True
        elif char in "@#%&!":
            is_spec = True
        if len(password) > 6 and is_numeric and is_lower and is_upper and is_spec:
            print('Надежный пароль!')
    else:
        if len(password) < 6:
            print('Пароль слишком короткий')
        if is_numeric == False:
            print('Пароль должен содержать цифры')
        if is_lower == False:
            print('Пароль должен содержать строчные буквы')
        if is_upper == False:
            print('Пароль должен содержать заглавные буквы')
        if is_spec == False:
            print('Пароль должен содержать специальные символы')
n1()

def n2():
    mesto = int(input('Введите номер вашего места: '))
    if mesto in range(37, 54):
        if mesto % 2 == 0:
            print('У вас боковое верхнее место')
        else:
            print('У вас боковое нижнее место')
    if mesto in range(1, 36):
        if mesto % 2 == 0:
            print('У вас верхнее место')
        else:
            print('У вас нижнее место')
n2()

def n3():
    god = int(input('Какой год вы хотите проверить: '))
    if ((god % 4 == 0) and (god % 4 != 0)) or (god % 4 == 0):
        print('Год високосный')
    else:
        print('Год не високосный')
n3()

def n4():
    a = input('Введите цвет: ')
    if (a != "красный") and (a != "синий") and (a != "желтый"):
        print('Ошибка! Введите цвет: красный, синий или желтый')
    b = input('Введите цвет: ')
    if (b != "желтый") and (b != "красный") and (b != "синий"):
        print('Ошибка! Введите цвет: красный, синий или желтый')
    if a == "красный":
        if b == "синий":
            print('Полученный цвет: фиолетовый')
        if b == "желтый":
            print('Полученный цвет: оранжевый')
        if b == "красный":
            print('Полученный цвет: красный')
    if a == "синий":
        if b == "красный":
            print('Полученный цвет: фиолетовый')
        if b == "желтый":
            print('Полученный цвет: зеленый')
        if b == "синий":
            print('Полученный цвет: синий')
    if a == "желтый":
        if b == "красный":
            print('Полученный цвет: оранжевый')
        if b == "желтый":
            print('Полученный цвет: желтый')
        if b == "синий":
            print('Полученный цвет: зеленый')
n4()

def n5():
    N = int(input('Введите количество слов: '))
    f = ''
    for i in range(N):
        s = input('Введите слово: ')
        f += s + ' '
    print('Полученная фраза: ', f)
n5()