sta = float(input("Стартовый результат"))
fin = float(input("Финальный результат"))
day = 1
while sta < fin:
    sta = sta + sta * 0.1
    day = day + 1
    print(f"Результат {sta:0.3} КМ через {day} дня")
else:
    print("Невероятно")
