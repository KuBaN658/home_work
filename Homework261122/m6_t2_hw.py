'''
Задача №1
Вход:
Пользователь должен ввести 'правильный' пароль, состоящий из:
цифр, букв латинского алфавита(строчные и прописные) и
специальных символов  special = '_!@#$%^&'.
Всего 4 набора различных символов.
В пароле обязательно должен быть хотя бы один символ из каждого набора.
Длина пароля от 8(мин) до 15(макс) символов включительно.
Максимальное количество попыток ввода неправильного пароля - 5.
Каждый раз выводим номер попытки.
Желательно выводить пояснение, почему пароль не принят и что нужно исправить.

* Добавить проверку, что в пароле только символы из 4-х наборов.

Как вариант:
check_password('some string') -> tuple[bool, str]
(True, reasons)
(False, reasons)


Оформить решения в виде модуля

import string as st
st.digits
st.ascii_lowercase
st.ascii_uppercase
special = '_!@#$%^&'

Выход:
пароль подходит / не подходит

Пример:
пароль подходит -> o58anuahaunH!
пароль подходит -> aaaAAA111!!!
пароль не подходит -> saucacAusacu8
'''
import string as st


def get_pass() -> None:
    """
    Получает пароль пользователя, проверяет его и выводит результат проверки.
    :return: None
    """
    count = 5
    while count:
        password = input('Введите пароль(от 8 до 15 символов): ')
        mistakes = {digit_check_pass(password), special_check_pass(password),
                    low_check_pass(password), up_check_pass(password),
                    forbidden_char_check(password), check_length_pass(password)}
        mistakes.discard('')
        if mistakes:
            print(*mistakes, sep='\n')
            count -= 1
            print_try(count)
        else:
            print(f'Пароль подходит: {password}')
            break
    else:
        print('Вы ввели неподходящий пароль пять раз')


def digit_check_pass(password) -> str:
    """
    Проверяет пароль на наличие цифр
    :param password: проверяемый пароль
    :return: возвращает ответ если цифр нет
    """
    for i in password:
        if i in st.digits:
            return ''
    return 'Пароль должен содержать хотя бы одну цифру'


def special_check_pass(password) -> str:
    """
    Проверяет наличие спец символов
    :param password: проверяемый пароль
    :return: возвращает ответ если спец символов нет
    """
    special = '_!@#$%^&'
    for i in password:
        if i in special:
            return ''
    return 'Пароль должен содержать хотя бы один спец символ'


def low_check_pass(password) -> str:
    """
    Проверяет наличие символов в нижнем регистре
    :param password: проверяемый пароль
    :return: возвращает ответ если символов в нижнем регистре нет
    """
    for i in password:
        if i in st.ascii_lowercase:
            return ''
    return 'Пароль должен содержать хотя бы один строчный символ'


def up_check_pass(password) -> str:
    """
    Проверяет наличие символов в верхнем регистре
    :param password: проверяемый пароль
    :return: возвращает ответ если символов в верхнем регистре нет
    """
    for i in password:
        if i in st.ascii_uppercase:
            return ''
    return 'Пароль должен содержать хотя бы один прописной символ'


def forbidden_char_check(password) -> str:
    """
    Проверяет пароль на наличие недопустимых символов
    :param password: проверяемый пароль
    :return: возвращает ответ если пароль содержит недопустимые символы
    """
    char = set(st.digits) | set('_!@#$%^&') | \
        set(st.ascii_lowercase) | set(st.ascii_uppercase)
    for i in password:
        if i not in char:
            return 'Пароль содержит недопустимые символы'
    return ''


def check_length_pass(password) -> str:
    """
    Проверяет длину пароля
    :param password: проверяемый пароль
    :return: возвращает ответ если пароль недопустимой длины
    """
    if len(password) > 15 or len(password) < 8:
        return 'Длина пароля должна быть от 8 до 15 символов'
    return ''


def print_try(counter) -> None:
    """
    Выводит количество оставшихся попыток с правильным оконыанием
    :param counter: количество оставшихся попыток
    :return: None
    """
    if counter == 1:
        print('У вас осталась 1 попытка')
    elif counter:
        print(f'У вас осталось {counter} попытки')


if __name__ == '__main__':
    get_pass()
    