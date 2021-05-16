from unittest import TestCase
import io
import contextlib

from BlackJackPcg.Card import Card
from BlackJackPcg.Person import Person
from BlackJackPcg.Person.Player import Player

class TestPerson(TestCase):

# these tests are currently not working - give TypeError: Can't instantiate abstract class Person with abstract methods make_game_decision
# testing functions in player tests
    def test_person_initiates_with_empty_hand(self):
        p = Person("test_person")
        self.assertTrue(len(p.get_hand()) == 0)

    def test_addition_of_cards_to_hand_gives_expected_number_in_hand(self):
        p = Person("test_person")
        card_list = [Card("S", "10"), Card("H", "J")]
        p.add_card_to_hand(card_list)
        self.assertTrue((len(p.get_hand()) == 2))

    def test_get_points_of_hand_gives_expected_value(self):
        p = Person("test_person")
        card_list = [Card("S", "10"), Card("H", "J")]
        p.add_card_to_hand(card_list)
        score = p.get_points_of_hand()
        p.add_card_to_hand([Card("H", "A")])
        self.assertTrue(score == 20 and p.get_points_of_hand() == 21)

    def test_get_points_with_multiple_aces(self):
        p = Person("test_person")
        card_list = [Card("S", "A"), Card("H", "A")]
        p.add_card_to_hand(card_list)
        score = p.get_points_of_hand()
        p.add_card_to_hand([Card("C", "A")])
        score_two = p.get_points_of_hand()
        p.add_card_to_hand([Card("D", "9")])
        #check all the scores are adjusted as expected on adding aces to hand
        self.assertTrue(score == 12 and score_two == 13 and p.get_points_of_hand() == 12)

    def test_show_hand_gives_expected_string(self):
        p = Player("test_player")
        card_list = [Card("S", "10"), Card("H", "J")]
        p.add_card_to_hand(card_list)
        with io.StringIO() as buffer:
            # redirect the stdout to the buffer - whatever goes to stdout will go to buffer
            with contextlib.redirect_stdout(buffer):
                # what is printed in this with will be redirected to the buffer; act
                p.show_hand()
                printed_text = buffer.getvalue()
            # assert - getvalue from buffer - check it contains expected phrase twice
            self.assertTrue(printed_text.count("The card is:") == 2)
