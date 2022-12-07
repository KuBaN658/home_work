"""
Задача №3
Дано слово из символов(латинские буквы + цифры), других нет.
Нужно вывести новой строкой только цифры, если они есть или
написать, что их нет.
Пример:
In: 'antuh1ouou21au3'
Out: 1213

In: 'sauhsauhasnhuasnhu'
Out: 'no digits'

Подсказки, что использовать:
while, индексация для элементов строки, str.isdigit()
"""
word = input('Введите символы: ')
i = 0
result = ''
while i < len(word):
    if word[i].isdigit():
        result += word[i]
    i += 1
if result:
    print(result)
else:
    print('no digits')