import Card
import random


class Deck:
    ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    suites = ["Heart", "Spades", "Clubs", "Clovers"]

    def __init__(self):
        self.cards = []

        for suite in self.suites:
            for rank in self.ranks:
                self.cards.append(Card.Card(rank, suite))

    def shuffle(self):
        random.shuffle(self.cards)

    def get_cards(self):
        return self.cards

    def remove_card(self):
        return self.cards.pop(0)
