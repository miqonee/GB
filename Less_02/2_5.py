print("Система 'Рейтинг' приветсвует")
q = ''
my_list = [7, 8, 4, 6, 1]
print(f"Изначальный списко выглядит так {my_list}")
while q !='q':
    q = input('Введите q для выхода из программы, или любой другой символ для продолжения')
    for el in range(len(my_list)):
     if q !='q':
        i = int(input("Введите число"))
        my_list.insert(el + 1, i)
        my_list.sort()
        print(my_list[::-1])
     elif q == "q":
         print("Пока пока")
