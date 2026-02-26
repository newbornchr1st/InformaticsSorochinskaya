name = input("Введите имя оператора:")
pressure = input("Введите текущее значение датчика давления:")

with open("sensor_log.txt", "w", encoding="utf-8") as sensor:
     sensor.write(f"ОПЕРАТОР\t\tЗНАЧЕНИЕ\n{name}\t\t{pressure}\n")
print("Данные успешно сохранены в sensor_log.txt")