"""
Задача №3
Дана строка. Необходимо посчитать количество вхождений каждого символа.
Пример:
In: Hello, Python1.
Out: 
H: 1
e: 1
h: 1
l: 2
o: 2
,: 1
P: 1
y: 1
t: 1
n: 1
1: 1
 : 1
.: 1 
"""
result = {}

for char in (string := input('Введите строку: ')):
    if char not in result:
        result[char] = string.count(char)

for item in result.items():
    print(*item, sep=':')