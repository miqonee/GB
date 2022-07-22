a = input("Введите значение - ").split()
b = 1
for i in range(0, len(a)):
    if b <= (len(a)+1):
        if len(a[i]) <= 10:
            print(f"Слово {b}", a[i])
            b = b + 1
        else:
            print(f"Слово {b}", (a[i][0:10]))
            b = b + 1




