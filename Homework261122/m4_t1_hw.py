"""
Задача №1.
Программа получает на вход последовательность целых чисел N(от 2 до 10).

Вам нужно определить вид последовательности:
 - возрастающая
 - убывающая
 - случайная
 - постоянная

В качестве ответа следуют выдать прописными латинскими буквами тип последовательности:
1. ASCENDING (строго возрастающая)
2. WEAKLY ASCENDING (нестрого возрастающая, то есть неубывающая)
3. DESCENDING (строго убывающая)
4. WEAKLY DESCENDING (нестрого убывающая, то есть невозрастающая)
5. CONSTANT (постоянная)
7. RANDOM (случайная)

Примеры входных и выходных данных:
In: 9 4 2 -1  Out: DESCENDING
In: 3 8 8 11  Out: WEAKLY ASCENDING
In: 2 -1 7    Out: RANDOM
In: 5 5 5 5   Out: CONSTANT
"""
import random as rnd

negative_positive = [-1, 1]
n = [rnd.randint(2, 10) * rnd.choice(negative_positive)
     for i in range(rnd.randint(2, 5))]
print(n)

keys = ['ASCENDING', 'DESCENDING', 'CONSTANT',
        'WEAKLY ASCENDING', 'WEAKLY DESCENDING', 'RANDOM']
val = [True] * 6

for i in range(len(n) - 1):
    next = n[i + 1]
    if n[i] < next:
        val[1] = val[4] = val[2] = False
    elif n[i] == next:
        val[0] = val[1] = False
    else:
        val[0] = val[3] = val[2] = False
        
print(keys[val.index(True)])
