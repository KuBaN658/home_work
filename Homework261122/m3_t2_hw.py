"""
Задача №4
Дана строка из двух слов. Поменяйте эти слова местами.
Пример:
In: 'Hello Python'
Out: 'Python Hello'

Используем str.index(), срезы.
! Списки еще не придумали !
"""

string = input('Введите строку из двух слов: ')
if ' ' in string:
    i = string.index(' ')

print(f'{string[i:]} {string[:i]}')
