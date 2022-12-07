"""
Задача №5
Строка из нескольких слов, не более 10.
Определите, сколько букв содержит самое длинное слово в строке.
Пример:
In: Как дела в учебе
Out: 5
"""
string = input('Введите несколько слов: ')
string = string.lstrip()
string = string.rstrip()
start_i = 0
stop_i = 0
longest = 0
while True:
    stop_i = string.find(' ', start_i)
    if stop_i == -1:
        break
    length = stop_i - start_i
    if longest < length:
        longest = length
    start_i = stop_i + 1
if longest < len(string) - start_i:
    longest = len(string) - start_i

    
print(longest)