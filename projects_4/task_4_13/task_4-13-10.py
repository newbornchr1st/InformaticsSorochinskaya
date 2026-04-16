array = input("Вводите элементы через пробел: ").split()
sum = 0

for i in range(1, len(array), 2):
    sum = sum + int(array[i])

print(sum)