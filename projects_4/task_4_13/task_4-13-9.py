array = input("Вводите элементы через пробел:").split()
sum = 0

for i in array:
    if int(i) % 2 == 1:
        sum = sum + int(i)

print(sum)