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
                #each of the cards added to list of cards in deck
                self.deck.append(Card(i_suit, i_num))

    def get_deck(self):
        return self.deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        for card in self.deck:
            card.show()

    def to_string(self):
        deck_string = ""
        for card in self.deck:
            deck_string = deck_string + card.to_string() + "\n"
        return deck_string

    #takes off one from the list, put into list to return, removes from original list
    def give_n_cards(self, num):
        if not isinstance(num, int):
            raise TypeError
        if (num < 0) or (num > len(self.deck)):
            raise ValueError
        x = 0
        cards_dealt = []
        while x < num:
            cards_dealt.append(self.deck.pop(0))
            x += 1
        return cards_dealt
