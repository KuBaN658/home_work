# from deck_total import Card, Deck

"""
Cоздадим имитацию ходов в “Дурака без козырей”:

1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 10 карт
3. Второй игрок берет сверху 10 карт.
4. Игрок-1 ходит:
    4.1. игрок-1 выкладывает самую маленькую карту по "старшенству"
    4.2. игрок-2 пытается бить карту, если у него есть такая же масть, но значением больше.
    4.3. Если игрок-2 не может побить карту, то он проигрывает/забирает себе(см. пункт 7)
    4.4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Если Игрок-2 отбился, то Игрок-1 и Игрок-2 меняются местами. Игрок-2 ходит, Игрок-1 отбивается.
6. Выведите в консоль максимально наглядную визуализацию данных ходов (библиотека rich)
7* Реализовать возможность добрать карты из колоды после того, как один из игроков отбился/взял в руку
"""
from rich.table import Table
from rich.console import Console
from deck_total import Deck


def print_deck(dck: Deck) -> None:
    """
    осуществляет красивый вывод колоды
    :return: None
    """
    table = Table(width=58)
    table.add_column("Колода",
                     style="black",
                     justify="center")
    table.add_row(str(dck))
    console.print(table)


style = "white on green"
console = Console(width=58, style=style)

dck = Deck()
dck.shuffle()
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print_deck(dck)  # вместо print(deck.show())

# 3. Сравнение карт:
card1, card2 = dck.draw(2)
result = ''
if card1 > card2:
    result = "[bold]\u003e[/]"
if card1 < card2:
    result = "[bold]\u003c[/]"

table = Table(title="Сравнение карт",
              width=58
              )

table.add_column("Моя карта",
                 style="black",
                 justify="center")

table.add_column("Результат",
                 style="white",
                 justify="center")

table.add_column("Карта оппонента",
                 justify="center",
                 style="black")

table.add_row(str(card1), result, str(card2))


console.print(table)
print_deck(dck)