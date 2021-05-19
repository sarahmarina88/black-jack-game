from BlackJackPcg.Deck import Deck
from BlackJackPcg.Person.Dealer import Dealer


class Game:

    def __init__(self, list_of_players=None):
        self.deck = Deck()
        self.deck.init_deck()
        self.list_of_players = list_of_players
        if self.list_of_players is None:
            self.list_of_players = []
        self.dealer = Dealer("bot")

    def get_list_of_players(self):
        return self.list_of_players

    def add_player_to_game(self, player):
        self.list_of_players.append(player)

    # function to deal cards then give each player and dealer a turn to make decision on taking cards; compare points; unfinished
    def play_game(self):
        bust_flag = False
        twenty_one_flag = False
        # shuffle cards before dealing
        self.deck.shuffle_deck()
        # give each player two cards and two to dealer
        for self.player in self.get_list_of_players():
            self.player.add_card_to_hand(self.deck.give_n_cards(2))
        self.dealer.add_card_to_hand(self.deck.give_n_cards(2))
        # the dealer shows one card
        print("The dealer will show their first card")
        self.dealer.show_hand_during_player_turn()
        # go through each player in player list - show hand then give option if want new card - show hand again
        for player in self.get_list_of_players():
            print("It is the turn of the player {}. Showing initial hand of cards.".format(player.get_username()))
            player.show_hand()
            if player.get_points_of_hand() == 21:
                twenty_one_flag = True
            else:
                while player.make_game_decision():
                    player.add_card_to_hand(self.deck.give_n_cards(1))
                    print("Showing hand of cards:")
                    player.show_hand()
                    # if points get to equal or exceed 21 will move onto next players turn
                    if player.get_points_of_hand() > 21:
                        bust_flag = True
                        break
                    if player.get_points_of_hand() == 21:
                        twenty_one_flag = True
                        break
            if bust_flag:
                print("Points of {}'s hand is {}. Over 21 so moving onto next player's turn.".format(player.get_username(), player.get_points_of_hand()))
            elif twenty_one_flag:
                print("{} has 21! Moving onto next player.".format(player.get_username))
            else:
                print("{} has chosen to stand with score {} - moving onto next player's turn.".format(player.get_username(), player.get_points_of_hand()))
        # move onto dealer turn - show hand then decision made depending score
        print("All players have played. Now it is the dealer's turn. Showing both cards in their initial hand:")
        self.dealer.show_hand()
        # continues to add cards to hand until score exceeds 17 then shows hand
        while self.dealer.make_game_decision():
            self.dealer.add_card_to_hand(self.deck.give_n_cards(1))
        print("Showing the dealer's final hand with score {}.".format(self.dealer.get_points_of_hand()))
        self.dealer.show_hand()

        # next have to compare scores of player(s) to dealer
        # if anyone has 21 will win/joint win; if all less than 21 highest wins; if players over 21 dealer win

