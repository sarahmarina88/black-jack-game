import io
import contextlib
from unittest import TestCase

from BlackJackPcg.Deck import Deck
from BlackJackPcg.Card import Card
from BlackJackPcg.Utils import CardUtils

class TestDeck(TestCase):

    def test_deck_creation_gives_correct_number_of_cards(self):
        #arrange
        d = Deck()
        #act
        d.init_deck()
        #assert
        self.assertTrue(len(d.get_deck()) == 52)

    def test_deck_creation_no_duplicates(self):
        #arrange
        d = Deck()
        #act
        d.init_deck()
        for card in d.get_deck():
            if d.get_deck().count(card) != 1:
                self.assertTrue(False)
        #assert - true unless a duplicate found then will fail
        self.assertTrue(True)

    def test_get_deck_function_empty_list_before_deck_init(self):
        d = Deck()
        d.get_deck()
        self.assertTrue(len(d.get_deck()) == 0)

    def test_get_deck_gives_all_valid_cards_after_deck_init(self):
        d = Deck()
        d.init_deck()
        d.get_deck()
        for c in d.get_deck():
            if isinstance(c, Card):
                if c.get_suit() not in CardUtils.get_possible_suits() or c.get_number() not in CardUtils.get_possible_numbers():
                    self.assertTrue(False)
            else:
                self.assertTrue(False) #will fail test directly if there is something not a card
        self.assertTrue(True) #passes provided all are cards and all valid

    def test_print_deck(self):
        # arrange - make deck of cards
        d = Deck()
        d.init_deck()
        with io.StringIO() as buffer:
            # redirect the stdout to the buffer - whatever goes to stdout will go to buffer
            with contextlib.redirect_stdout(buffer):
                # what is printed in this with will be redirected to the buffer; act
                d.print_deck()
                printed_text = buffer.getvalue().strip()
            # assert - getvalue from buffer - check it is the same as the string
            self.assertTrue(printed_text.count("The card is:") == 52)

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
        try:
            d.give_n_cards(-3)
        except ValueError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

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
        d = Deck()
        # for 0 - 5 cards initiate the deck for each card returned from dealing the n cards, check if is in the remaining deck
        for n in range(5):
            d.init_deck()
            for c in d.give_n_cards(n):
                if c in d.get_deck():
                    self.assertTrue(False)
        self.assertTrue(True)
    #only passes if no matter how many cards taken, none of what is in returned list is still in the deck
