from unittest import TestCase
import io
import contextlib

from BlackJackPcg.Card import Card
from BlackJackPcg.Person.Dealer import Dealer

class TestDealer(TestCase):

    def test_dealer_showing_cards_in_player_turn_only_shows_one(self):
        d = Dealer("test_dealer")
        card_list = [Card("S", "10"), Card("H", "J")]
        d.add_card_to_hand(card_list)
        with io.StringIO() as buffer:
            # redirect the stdout to the buffer - whatever goes to stdout will go to buffer
            with contextlib.redirect_stdout(buffer):
                # what is printed in this with will be redirected to the buffer; act
                d.show_hand_during_player_turn()
                printed_text = buffer.getvalue()
            # assert - getvalue from buffer - check it only tells once the card is
            self.assertTrue(printed_text.count("The card is:") == 1)

    def test_dealer_showing_cards_shows_all(self):
        d = Dealer("test_dealer")
        card_list = [Card("S", "10"), Card("H", "J")]
        d.add_card_to_hand(card_list)
        with io.StringIO() as buffer:
            # redirect the stdout to the buffer - whatever goes to stdout will go to buffer
            with contextlib.redirect_stdout(buffer):
                # what is printed in this with will be redirected to the buffer; act
                d.show_hand()
                printed_text = buffer.getvalue()
            # assert - getvalue from buffer - check it only tells once the card is
            self.assertTrue(printed_text.count("The card is:") == 2)

    def test_game_decision_when_points_over_17(self):
        d = Dealer("test_dealer")
        # test dealer - give hand with high points
        card_list = [Card("S", "10"), Card("H", "J")]
        d.add_card_to_hand(card_list)
        # check that the function will return false to not take another card
        self.assertFalse(d.make_game_decision())

    def test_game_decision_when_points_are_17(self):
        d = Dealer("test_dealer")
        card_list = [Card("S", "10"), Card("H", "7")]
        d.add_card_to_hand(card_list)
        self.assertFalse(d.make_game_decision())

    def test_game_decision_when_points_under_17(self):
        d = Dealer("test_dealer")
        card_list = [Card("S", "2"), Card("H", "7")]
        d.add_card_to_hand(card_list)
        self.assertTrue(d.make_game_decision())