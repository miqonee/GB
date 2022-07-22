print("Система 'Рейтинг' приветсвует")
q = ''
my_list = [7, 8, 4, 6, 1]
print(f"Изначальный списко выглядит так {my_list}")
while q !='q':
    q = input('Введите q для выхода из программы, или любой другой символ для продолжения')
    if q !='q':
        i = int(input("Введите число"))
        my_list.append(i)
        my_list.sort()
        print(my_list[::-1])
    elif q == "q":
        print("Пока пока")