def n1():
    print('Создание строки с известным количеством слов')
    N = int(input('Введите количество слов: '))
    f = ''
    for i in range(N):
        s = input('Введите слово: ')
        f += s + ' '
    print('Полученная фраза: ', f)

def n2():
    print('Создание строки с неизвестным количеством слов')
    ss = ''
    while (w := str(input('Введите слово: '))) != "stop":
        ss += w + ' '
    print('Полученная фраза: ', ss)

def n3():
    print('Проверка на вхождение в слово буквы Ф')
    while (s := str(input('Введите слово: '))) != 'stop':
        if 'ф' in s or 'Ф' in s:
            print('Ого! Это редкое слово!')
        else:
            print('ЭХ, это не очень редкое слово!:(')

def n4():
    print('Игра "Калькулятор"')
    from random import randint
    on = 0
    op = 0
    while on < 3:
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        print(f"{n1} + {n2} = ", end="")
        otv = input()
        if not otv.isdigit() and otv != "stop":
            print("Некорректный ввод, повторите попытку!")
            otv = input()
            if (n1 + n2) != int(otv):
                print("Ответ неверный:(")
                on += 1
            if (n1 + n2) == int(otv):
                print("Правильно!")
                op += 1
            if on >= 3:
                print("Игра окончена. Правильных ответов: ", op)
        elif otv == "stop":
            print("Игра завершена.")
        else:
            if (n1 + n2) != int(otv):
                print("Ответ неверный:(")
                on += 1
            if (n1 + n2) == int(otv):
                print("Правильно!")
                op += 1
            if on >= 3:
                print("Игра окончена. Правильных ответов: ", op)

n1(), n2(), n3(), n4()