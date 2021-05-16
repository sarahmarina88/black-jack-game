import io
import contextlib

from BlackJackPcg.Card import Card
from BlackJackPcg.Utils import CardUtils
from unittest import TestCase


class TestCard(TestCase):

    def test_card_for_suit(self):
        flag = False
        try:
            Card("asd", CardUtils.get_possible_numbers()[0]) #here we want to have suit wrong (to make sure get exception) rest right
        except RuntimeError:
            flag = True #if there is something wrong in the card suit the flag will become true
        if flag:
            self.assertTrue(True) #is always true - this is true if there is exception
        else:
            self.assertTrue(False)

    def test_card_for_number(self):
        flag = False
        try:
            Card(CardUtils.get_possible_suits()[0], "uiu")#here we want to have num wrong (to make sure get exception) rest right
        except RuntimeError:
            flag = True #if there is something wrong i the card num the flag will become true
        if flag:
            self.assertTrue(True) #is always true - this is true if there is exception
        else:
            self.assertTrue(False)

    def test_card_creation(self):
        flag = True
        try:
            Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_numbers()[0]) #here we want to have suit wrong (to make sure get exception) rest right
        except RuntimeError:
            flag = False #if we do get error test has failed (not passed as all should be ok)
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_get_suit_function(self):
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_numbers()[0])
        suit = c.get_suit()
        self.assertTrue(suit in CardUtils.get_possible_suits())

    def test_get_number_function(self):
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_numbers()[0])
        number = c.get_number()
        self.assertTrue(number in CardUtils.get_possible_numbers())

    def test_show_card(self):
        #arrange - make the card
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_numbers()[0])
        with io.StringIO() as buffer:
            #redirect the stdout to the buffer - whatever goes to stdout will go to buffer
            with contextlib.redirect_stdout(buffer):
                #what is printed in this with will be redirected to the buffer; act
                c.show()
            #assert - getvalue from buffer - check it is the same as the string
            self.assertTrue(buffer.getvalue().strip() == c.to_string())

    def test_get_card_value(self):
        list_of_values = []
        for n in CardUtils.get_possible_numbers():
            # for each possibly number in one suit, add the value of card to list
            list_of_values.append(Card("D",n).get_card_value())
        # checks the list of values is as expected for suit
        self.assertTrue(list_of_values == [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
