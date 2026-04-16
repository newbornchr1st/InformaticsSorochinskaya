array = input("Вводите элементы через пробел: ").split()
count = 0
sum = 0

for i in range(0, len(array), 2):
    sum = sum + int(array[i])
    count = count + 1

sr_arifm = sum // count
print(sr_arifm)