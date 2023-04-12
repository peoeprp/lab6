from random import randint
def n1():

    number=[]
    for i in range(5):
        number.append(randint(1,10))
    a=int(input("Введите число: "))
    if a in number:
        print("Загаданный список: ",*number)
        print("Поздравляю, Вы угадали число!")
    else:
        print("Загаданный список: ",*number)
        print("Нет такого числа!")
n1()

def n2():
    k=int(input("введите длину списка: "))
    numbers=[]
    kol=0
    for i in range(k):
        numbers.append(randint(1,10))
    i=0
    for j in range(k-1):
        g=numbers[i]
        if g == numbers[j+1]:
            kol +=1
            i +=1
    print("Загаданный список: ",*numbers)
    print("Число повторений: ", kol)
n2()

def n3():
    dn = ("Пн","Вт","Ср","Чт","Пт","Сб","Вс")
    d=int(input("Введите количество выходных: "))
    for i in dn:
        print("Рабочие: ", *dn[:-d])
        print("Выходные: ", *dn[-d:])
        break
n3()

def n4():
    l1=["Иванов","Смирнов","Кузнецов","Попов","Васильев","Петров","Соколов","Михайлов","Ершов","Афанасьев"]
    l2=["Поляков","Моисеев","Соболев","Кошелев","Лебедев","Козлов","Новиков","Журавлев","Фролов","Горбачев"]
    l3=[]
    k=randint(0,8)
    m=randint(0,8)
    for i in range(5):
        l3.append(l1[k])
        k += 1
    for i in range(5):
        l3.append(l2[m])
        m +=1
    print("Список первой группы: ",*l1)
    print("Список второй группы: ",*l2)
    print("Список полученной группы: ",*l3)
    print("Количество человек в команде: ", len(l3))
    l3.sort()
    print("Список группы по алфавиту: ", *l3)
    fam=str(input("Введите фамилию: "))
    if fam in l3:
        print("Этот человек есть в команде")
    else:
        print("Этого человека нет в команде")
n4()