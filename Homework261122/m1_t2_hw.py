"""
Задача № 2. 
Введены два натуральных числа.
Округлить в большую сторону результат деления, если числа не делятся нацело.
Про if, math, round ничего не знаем
Что знаем: +, -, *, /, //, %, int, str, bool, float 

Пример 1:
In:
    a = 7
    b = 4
Out:
    result: 2

Пример 2:
In:
    a = 16
    b = 4
Out:
    result: 4
"""
dividend = int(input('Введите делимое: '))
divisor = int(input('Введите делитель: '))
result = dividend / divisor
mod = dividend % divisor
print(f'Результат: {int(result) + (mod != 0)}')
