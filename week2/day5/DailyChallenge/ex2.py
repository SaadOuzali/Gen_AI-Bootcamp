import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    __suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    __values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [
            Card(suit, value) for suit in Deck.__suits for value in Deck.__values
        ]

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            print("No more cards to deal!")
            return None
        return self.cards.pop()
