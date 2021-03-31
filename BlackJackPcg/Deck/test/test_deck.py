import io
import contextlib
from unittest import TestCase

from BlackJackPcg.Deck import Deck
from BlackJackPcg.Card import Card
from BlackJackPcg.Utils import CardUtils

class TestDeck(TestCase):

    def test_deck_creation_givs_correct_number_of_cards(self):
        #arrange
        d = Deck()
        #act
        d.init_deck()
        #assert
        self.assertTrue(len(d.get_deck()) == 52)

    def test_deck_creation_no_duplicates(self):
        #arrange
        d = Deck()
        num_duplicates = 0
        #act
        d.init_deck()
        for card in d.get_deck():
            if d.get_deck().count(card) != 1:
                num_duplicates += 1
        #assert
        self.assertTrue(num_duplicates == 0)

    def test_shuffle_function_does_shuffle_the_deck(self):
        d = Deck()
        d.init_deck()
        card_list = []
        for card in d.get_deck():
            card_list.append("{}{}".format(card.get_number(), card.get_suit()))
        d.shuffle_deck()
        new_card_list = []
        for card in d.get_deck():
            new_card_list.append("{}{}".format(card.get_number(), card.get_suit()))
        #check the shuffled card list and the initial card list are not the same
        self.assertTrue((card_list != new_card_list) and (len(card_list) == len(new_card_list)))

    def test_how_many_cards_unmoved_after_shuffling(self):
        d = Deck()
        d.init_deck()
        card_list = []
        for card in d.get_deck():
            card_list.append("{}{}".format(card.get_number(), card.get_suit()))
        d.shuffle_deck()
        new_card_list = []
        for card in d.get_deck():
            new_card_list.append("{}{}".format(card.get_number(), card.get_suit()))
        pairs_still_together = 0
        for i in range(len(card_list) - 1):
            if [card_list[i], card_list[i + 1]] in new_card_list:
                pairs_still_together += 1
        self.assertTrue(pairs_still_together < 5)

    def test_get_deck_function_returns_deck(self):
        d = Deck()
        deck_returned = d.get_deck()
        self.assertTrue(deck_returned == d.deck)

    def test_get_deck_function_empty_list_before_deck_init(self):
        d = Deck()
        d.get_deck()
        self.assertTrue(len(d.get_deck()) == 0)

    def test_get_deck_gives_all_valid_cards_after_deck_init(self):
        d = Deck()
        d.init_deck()
        d.get_deck()
        valid_card_count = 0
        for c in d.get_deck():
            if isinstance(c, Card):
                if c.get_suit() in CardUtils.get_possible_suits() and c. get_number() in CardUtils.get_possible_numbers():
                    valid_card_count += 1
        self.assertTrue(valid_card_count == 52)

    def test_print_deck(self):
        # arrange - make deck of cards
        d = Deck()
        d.init_deck()
        with io.StringIO() as buffer:
            # redirect the stdout to the buffer - whatever goes to stdout will go to buffer
            with contextlib.redirect_stdout(buffer):
                # what is printed in this with will be redirected to the buffer; act
                d.print_deck()
            # assert - getvalue from buffer - check it is the same as the string
            self.assertTrue(buffer.getvalue().strip() == d.to_string().strip())

    def test_giving_cards_function_gives_correct_num_of_cards(self):
        d = Deck()
        d.init_deck()
        num_cards_dealt = 0
        for c in d.give_n_cards(2):
            if isinstance(c, Card):
                num_cards_dealt += 1
        #passes if the number of cards dealt is as expected and the length of the remaining reduced by expected number
        self.assertTrue((num_cards_dealt == 2) and (len(d.get_deck()) == 50))

    def test_asking_neg_num_cards_gives_error(self):
        d = Deck()
        d.init_deck()
        flag = False
        try:
            d.give_n_cards(-3)
        except ValueError:
            flag = True
        self.assertTrue(flag) #test only passes if flag is true - only if error raised for negative number

    def test_asking_more_cards_than_deck_has_gives_error(self):
        d = Deck()
        d.init_deck()
        flag = False
        try:
            d.give_n_cards(len(d.get_deck()) + 5)
        except ValueError:
            flag = True
        self.assertTrue(flag) #test only passes if flag is true - only if error raised for negative number

    def test_asking_non_integer_number_of_cards_gives_error(self):
        d = Deck()
        d.init_deck()
        flag = False
        try:
            d.give_n_cards("three")
        except TypeError:
            flag = True
        self.assertTrue(flag)

    def test_cards_dealt_are_no_longer_in_the_deck(self):
    #check the cards in the dealt cards are not still in the deck - check for taking up to five cards (?)
        d = Deck()
        cards_still_in_deck_after_they_have_been_dealt = 0
        # for 0 - 5 cards initiate the deck for each card returned from dealing the n cards, check if is in the remaining deck
        for n in range(5):
            d.init_deck()
            for c in d.give_n_cards(n):
                if c in d.get_deck():
                    cards_still_in_deck_after_they_have_been_dealt += 1
        self.assertTrue(cards_still_in_deck_after_they_have_been_dealt == 0)
    #only passes if no matter how many cards taken, none of what is in returned list is still in the deck
