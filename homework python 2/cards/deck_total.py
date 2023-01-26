import random
from typing import Self

# Начнем с создания карты
# ♥ ♦ ♣ ♠
VALUES = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
SUITS = {'Spades': 0.1, 'Clubs': 0.2, 'Diamonds': 0.3, 'Hearts': 0.4}
SUITS_UNI = {
        'Spades': '[black]♠[/]',
        'Clubs': '[black]♣[/]',
        'Diamonds': '[red]♦[/]',
        'Hearts': '[red]♥[/]'
}


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты
        self.point = SUITS[suit] + VALUES[value]

    def __str__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __eq__(self, other_card: Self):
        if type(other_card) == Card:
            return self.suit == other_card.suit
        else:
            raise TypeError('В колоде есть что-то не похожее на карты')

    def __gt__(self, other_card: Self):
        if type(other_card) == Card:
            return self.point > other_card.point
        else:
            raise TypeError('В колоде есть что-то не похожее на карты')

    def __lt__(self, other_card: Self):
        if type(other_card) == Card:
            return self.point < other_card.point
        else:
            raise TypeError('В колоде есть что-то не похожее на карты')


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]
        self.cards.sort()

    def __str__(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        return f'deck[{len(self.cards)}]: ' + \
               ', '.join([str(card) for card in self.cards])

    def draw(self, qty):
        # Принцип работы данного метода прописан в 00_task_deck.md
        result = [self.cards.pop(0) for _ in range(qty)]
        return result

    def shuffle(self):
        random.shuffle(self.cards)


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    # Задачи - реализовать нативную работу с объектами:
    # 1. Вывод колоды в терминал:
    print(deck)  # вместо print(deck.show())

    card1, card2 = deck.draw(2)
    # 2. Вывод карты в терминал:
    print(card1)  # вместо print(card1.to_str())
    print(card2)
    # 3. Сравнение карт:
    if card1 > card2:
        print(f"{card1} больше {card2}")
    if card1 < card2:
        print(f"{card1} меньше {card2}")

# Это на следующее занятие.
# 4. Итерация по колоде:
# for card in deck:
#     print(card)

# 5. Просмотр карты в колоде по ее индексу:
# __getitem__(self, index):
# print(deck[6])


# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html
