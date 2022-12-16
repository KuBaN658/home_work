"""
Задача №2
Напишите программу, определяющую количество уникальных символов в строке.
Вывести сами символы  и количество.

Например, в строке Hello, World! содержится десять
уникальных символов, а в строке zzz – один.
In: zzz
Out: z, 1

In: Hello, World!
Out: ['H', ...., '!'], 10

!set еще не придумали
"""

string = input('Введите строку: ')
unique = []

for char in string:
    if char not in unique:
        unique.append(char)

print(*unique, ', ', len(unique), sep='')