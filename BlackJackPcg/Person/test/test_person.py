from unittest import TestCase
import io
import contextlib

from BlackJackPcg.Card import Card
from BlackJackPcg.Person import Person


class TestPerson(TestCase):
    #rewritten to put the tempobj class outside of the individual tests - can have once instead of repeating
#args allows diff variables to be given -
    def __init__(self, *args, **kwargs):
        super(TestPerson, self).__init__(*args, **kwargs)

        class TempObj(Person):
            def __int__(self, username):
                super().__init__()
            #have to have the abstract method

            def make_game_decision(self):
                raise NotImplementedError("It is an abstract test")
        # make instance of the temporary object then can do tests on this

        self.p = TempObj("test_person")

    def test_person_initiates_with_empty_hand(self):
       self.assertTrue(len(self.p.get_hand()) == 0)

    def test_addition_of_cards_to_hand_gives_expected_number_in_hand(self):
        card_list = [Card("S", "10"), Card("H", "J")]
        self.p.add_card_to_hand(card_list)
        self.assertTrue((len(self.p.get_hand()) == 2))

    def test_get_points_of_hand_gives_expected_value(self):
        card_list = [Card("S", "10"), Card("H", "J")]
        self.p.add_card_to_hand(card_list)
        score = self.p.get_points_of_hand()
        self.p.add_card_to_hand([Card("H", "A")])
        self.assertTrue(score == 20 and self.p.get_points_of_hand() == 21)

    def test_get_points_with_multiple_aces(self):
        card_list = [Card("S", "A"), Card("H", "A")]
        self.p.add_card_to_hand(card_list)
        score = self.p.get_points_of_hand()
        self.p.add_card_to_hand([Card("C", "A")])
        score_two = self.p.get_points_of_hand()
        self.p.add_card_to_hand([Card("D", "9")])
        #check all the scores are adjusted as expected on adding aces to hand
        self.assertTrue(score == 12 and score_two == 13 and self.p.get_points_of_hand() == 12)

    def test_show_hand_gives_expected_string(self):
        card_list = [Card("S", "10"), Card("H", "J")]
        self.p.add_card_to_hand(card_list)
        with io.StringIO() as buffer:
            # redirect the stdout to the buffer - whatever goes to stdout will go to buffer
            with contextlib.redirect_stdout(buffer):
                # what is printed in this with will be redirected to the buffer; act
                self.p.show_hand()
                printed_text = buffer.getvalue()
            # assert - getvalue from buffer - check it contains expected phrase twice
            self.assertTrue(printed_text.count("The card is:") == 2)
