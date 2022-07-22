a = int(input('Введите число месяца'))
b = ['Зима', 'Весна', 'Лето', 'Осень']
if a > 0 and a <= 12:
    if a == 1 or a == 12 or a == 2:
        print(b[0])
    elif a == 3 or a == 4 or a == 5:
        print(b[1])
    elif a == 6 or a == 7 or a == 8:
        print(b[2])
    else:
        print(b[3])
else:
    print("Нет такого месяца")
