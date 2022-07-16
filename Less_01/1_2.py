time_sec = int(input("ВВедите время в секундах (1 час = 3600 секунд) - "))

time_min = (time_sec % 3600) // 60
time_h = (time_sec / 60) // 60
time_sec_ = (time_sec % 60)
print(f'{time_h:02}:{time_min:02}:{time_sec_:02}')
