import random

from BlackJackPcg.Card import Card
from BlackJackPcg.Utils import CardUtils


class Deck:

    def __init__(self):
        self.deck = []

    def init_deck(self):
        for i_col in CardUtils.get_possible_colors():
            for i_suit in CardUtils.get_possible_suits():
                for i_num in CardUtils.get_possible_numbers():
                    self.deck.append(Card(i_suit, i_col, i_num))

    def get_deck(self):
        return self.deck

    def suffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        for card in self.deck:
            card.show()