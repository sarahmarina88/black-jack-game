from unittest import TestCase
import io
import contextlib

from BlackJackPcg.Card import Card
from BlackJackPcg.Person.Dealer import Dealer

class TestDeck(TestCase):

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
