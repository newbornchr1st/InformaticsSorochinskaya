array = input("Вводите элементы через пробел:").split()
sum = 0

for i in array:
    sum = sum + int(i)

sr_arifm = sum // len(array)

print(sr_arifm)