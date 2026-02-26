import textwrap

FIO = input('Введите имя исследователя: ')
data_ = input('Введите дату: ')
experiment_name = input('Введите название эксперимента: ')
sum_ = input('Введите вывод: ')
W = 50

with open('journal.txt', 'w', encoding='utf-8') as jr:
    jr.write(f'''
+{'-'*W}+
|{'Электронный лабораторный журнал':^{W}}|
+{'-'*W}+
| {'ФИО исследователя : ' + FIO:<{W-1}}|
| {'Дата              : ' + data_:<{W-1}}|
| {'Эксперимент       : ' + experiment_name:<{W-1}}|
+--------------------------------------------------+
| {'Вывод:':<{W-1}}|
''')
    
    
    for line in textwrap.wrap(sum_, W-2):
        jr.write(f'| {line:<{W-2}} |\n')

    jr.write(f'+{'-'*W}+')