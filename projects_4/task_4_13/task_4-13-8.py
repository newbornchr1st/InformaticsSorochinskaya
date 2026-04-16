array = input("Вводите элементы через пробел:").split()
count = 0

for i in array:
    if int(i) > 0:
        count = count + 1

print(count)