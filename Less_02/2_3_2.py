a = int(input('Введите число месяца'))
b = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if a > 0 and a <= 12:
    if a == 1 or a == 12 or a == 2:
        print(b.get(1))
    elif a == 3 or a == 4 or a == 5:
        print(b.get(2))
    elif a == 6 or a == 7 or a == 8:
        print(b.get(3))
    else:
        print(b.get(4))
else:
    print("Нет такого месяца")
