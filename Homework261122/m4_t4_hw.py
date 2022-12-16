"""
Задача №4.
Написать программу, используя набор букв из модуля string(string.ascii_lowercase).

Вход: размер шахматной доски, от 0 до 20
Выход: вывести на экран эту доску с названиями полей.
Подсказка: Используем вложенные циклы

Пример:
In: 4
Out:
    a4 b4 c4 d4
    a3 b3 c3 d3
    a2 b2 c2 d2
    a1 b1 c1 d1
"""
import string

for i in range((n := int(input('Введите размер шахматной доски: '))), 0, -1):
    for j in range(n):
        print((string.ascii_lowercase[j] + str(i)).rjust(3) , sep='', end=' ')
    print()
    