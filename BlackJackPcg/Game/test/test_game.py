from unittest import TestCase
from BlackJackPcg.Game import Game
from BlackJackPcg.Person.Player import Player


class TestGame(TestCase):

    def test_game_initiates_with_deck_of_cards(self):
        g = Game()
        self.assertTrue(len(g.deck.get_deck()) == 52)

    def test_initiates_without_players(self):
        g = Game()
        self.assertTrue(len(g.get_list_of_players()) == 0)

    def test_initiates_with_dealer_called_bot(self):
        g = Game()
        self.assertTrue(g.dealer.get_username() == 'bot')

    def test_initiates_without_winner_decided(self):
        g = Game()
        self.assertTrue(g.get_winner() is None)

    def test_add_player_adds_players_to_list(self):
        g = Game()
        p_one = Player("testplayer1")
        p_two = Player("testplayer2")
        g.add_player_to_game(p_one)
        num_players = len(g.get_list_of_players())
        player_name = g.get_list_of_players()[0].get_username()
        g.add_player_to_game(p_two)
        if num_players == 1 and player_name =='testplayer1':
            self.assertTrue((len(g.get_list_of_players())==2) and (g.get_list_of_players()[1].get_username() == 'testplayer2'))
        else:
            self.assertTrue(False)

    # tests for the play_game() function
    def test_play_game_each_player_and_dealer_get_2_cards(self):
        pass

    def test_play_game_moves_onto_next_player_then_to_dealer(self):
        pass

    def test_exits_if_too_many_incorrect_input(self):
        pass