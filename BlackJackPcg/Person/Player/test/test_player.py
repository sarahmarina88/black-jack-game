from unittest import TestCase, mock
import io
import contextlib
import unittest.mock

from BlackJackPcg.Card import Card
from BlackJackPcg.Person.Player import Player


class TestPlayer(TestCase):

    def test_player_initiates_with_empty_hand(self):
        p = Player("test_player")
        self.assertTrue(len(p.get_hand()) == 0)

    def test_addition_of_cards_to_hand_gives_expected_number_in_hand(self):
        p = Player("test_player")
        card_list = [Card("S", "10"), Card("H", "J")]
        p.add_card_to_hand(card_list)
        self.assertTrue((len(p.get_hand()) == 2))

    def test_get_points_of_hand_gives_expected_value(self):
        p = Player("test_player")
        card_list = [Card("S", "10"), Card("H", "J")]
        p.add_card_to_hand(card_list)
        score = p.get_points_of_hand()
        p.add_card_to_hand([Card("H", "A")])
        self.assertTrue(score == 20 and p.get_points_of_hand() == 21)

    def test_get_points_with_multiple_aces(self):
        p = Player("test_player")
        card_list = [Card("S", "A"), Card("H", "A")]
        p.add_card_to_hand(card_list)
        score = p.get_points_of_hand()
        p.add_card_to_hand([Card("C", "A")])
        score_two = p.get_points_of_hand()
        p.add_card_to_hand([Card("D", "9")])
        # check all the scores are adjusted as expected on adding aces to hand
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

    #unsure how to do testing with user input
    def test_make_game_decision_gives_true_for_input_1(self):
        p = Player("test_player")
        pass

    def test_make_game_decision_gives_false_for_input_0(self):
        pass

    def test_make_game_decision_gives_error_for_non_integer_input(self):
        pass

    def test_make_game_decision_not_accepting_other_integers(self):
        pass

