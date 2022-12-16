"""
Задача №5
Написать программу, которая расшифрует строку,
используя набор букв из модуля string(string.ascii_lowercase),
Каждая символ - это две цифры.
Отчет с 00 -> 'a', 01 -> 'b' и до 25 -> 'z', 26 - это пробел, он не входит в набор букв
Вход: строка из цифр. Выход: Текст.
Проверка работы программы выполняется через вторую строку.

* реализовать и расшифровку и зашифровку
"""
import string as st

code = '070411111426152419071413'
alfa = st.ascii_lowercase + ' '

for i in range(0, len(code), 2):
    print(alfa[int(code[i:i + 2])], end='')
print()

string = input('Введите строку: ').lower()

for i in string:
    index = alfa.find(i)
    if index == -1:
        print(f' {i} - не кодируемый символ!', end=' ')
    else:
        print(str(index).rjust(2, '0'), end='')
