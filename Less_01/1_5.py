rev = float(input("Введите вашу прибыль - "))
cos = float(input("Введите ваши издержки - "))
res = rev - cos
if rev > 0:
    print(f"Прибыль составила {res}")
    ren = (100 * (res / cos))
    print(f'Рентабильность составила {ren:.2}% ')
    per = int(input("Сколько сотрудников в вашей компании?"))
    print(f"Прибыль на сотрудника состовляет {res / per:2}")
elif res < 0:
    print(f"Увы ваша прибыль составляет {-res:2}")
else:
    print("Идеальный баланс")
