"""
Задача № 1. 
Получить реверсную запись трехзначного числа
Пример: 
вход: 346, выход: 643
вход: 100, выход: 001
вход: 340, выход: 043
"""
num = input('Введите трехзначное число: ')
if len(num) == 3:
    num = int(num)
    hundreds = num // 100
    tens = num % 100 // 10
    units = num % 10
    print(units, tens, hundreds, sep='')
elif len(num) == 0:
    print('Данные отсутствуют')
else:
    print(f'Вы ввели {len(num)}-значное число')

