def n1():
    try:
        a = int(input('Введите число для проверки: '))
    except ValueError:
        print('Введено не число!')
    else:
        if a%3 == 0 and a != 0:
            print('Число', a, 'делится на 3')
        elif a == 0:
            print('Введён ноль!')
        else:
            print('Число', a, 'не делится на 3')
def n2():
    try:
        a = int(input('Введите число для проверки: '))
        b= 100/a
    except ZeroDivisionError:
        print('Введен ноль!')
    except ValueError:
        print('Введено не число!')
    else:
        print('Полученный результат: ', b)

def n3():
    d=input('Введите дату в формате дд.мм.гггг: ')
    d=d.split('.')
    if int(d[0])*int(d[1]) == int(d[2][2:4]):
        print("Дата магическая")
    else:
        print("Дата не магическая")

def n4():
    n = input('Введите номер для проверки: ')
    sum1 = 0
    sum2 = 0
    if (len(n) % 2) != 0:
        print('Номер не подходит')
    else:
        ser = int(len(n) / 2)
        for i in range(ser):
            sum1 += int(n[i:i + 1])
        for g in range(ser):
            sum2 += int(n[ser:ser + 1])
            ser += 1
        if sum1 == sum2:
            print('Ваш билет счастливый!')
        else:
            print('Ваш билет не счастливый')


n1(), n2(), n3(), n4()