import random

from BlackJackPcg.Card import Card
from BlackJackPcg.Utils import CardUtils


class Deck:

    def __init__(self):
        self.deck = []

    def init_deck(self):
        #go through the possible suits (4) and for each get the possible numbers then mark as red or blue for colour depending on the suit - colour not actually needed
        for i_suit in CardUtils.get_possible_suits():
            for i_num in CardUtils.get_possible_numbers():
                if i_suit == 'S' or i_suit == 'C':
                    i_col = 'B'
                else:
                    i_col = 'R'
                #each of the cards added to list of cards in deck
                self.deck.append(Card(i_suit, i_col, i_num))

    def get_deck(self):
        return self.deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        for card in self.deck:
            card.show()

    def give_cards(self, num):
        pass
    #takes the num card/s off deck, return list of cards dealt