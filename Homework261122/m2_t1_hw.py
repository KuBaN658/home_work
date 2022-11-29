"""
Задача №4. Посчитать размер вклада на депозите за несколько лет.

Вход:
размер начального вклада (от 100 до 1_000_000 рублей)(float),
годовой процент начисления(от 1 до 20)(float) с ежегодной капитализацией,
количество лет по вкладу(от 1 до 100)(int).

Выход:
Проверить введеные данные и посчитать итоговую сумму на счету.
Если данные неверные, то вывести сообщение об этом.
! Циклы еще не придумали
"""
deposit_amount = float(input('Введите размер вклада(от 100 до 1 000 000): '))
if 100 <= deposit_amount <= 10**6:
    percent = float(input('Введите процентную ставку(от 1.0 до 20.0): '))
    if 1 <= percent <= 20:
        deposit_term = int(input('Введите срок вклада(от 1 до 100): '))
        if 1 <= deposit_term <= 100:
            deposit_amount *= (1 + (percent / 100)) ** deposit_term
            print(f'На вашем вкладе: {deposit_amount:.2f}')
        elif deposit_term < 1:
            print('Минимальный срок вклада 1 год')
        else:
            print('Максимальный срок вклада 100 лет')
    elif percent < 1:
        print('Минимальная процентная ставка 1 %')
    else:
        print('Максимальная процентная 20 %')
elif deposit_amount < 100:
    print('Минимальный размер вклада 100 рублей')
else:
    print('Максимальный размер вклада 1 000 000 рублей')