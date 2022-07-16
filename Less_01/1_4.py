all = int(input("Введите ваше число - "))
last_max = all % 10
all = all // 10

while all > 0:
    if all % 10 > last_max:
        last_max = all % 10
    all = all // 10
print("Самая большая цифра в числе - ", last_max)

# в решении задания очень помог дебаг, спасибо!
