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
        self.winner = None

    def set_winner(self, winner):
        self.winner = winner

    def get_winner(self):
        return self.winner

    def get_list_of_players(self):
        return self.list_of_players

    def add_player_to_game(self, player):
        self.list_of_players.append(player)

    # function to deal cards then give each player and dealer a turn to make decision on taking cards; compare points; unfinished
    def play_game(self):
        self.deck.shuffle_deck()
        # give each player two cards and two to dealer
        for player in self.get_list_of_players():
            player.add_card_to_hand(self.deck.give_n_cards(2))
        self.dealer.add_card_to_hand(self.deck.give_n_cards(2))
        # the dealer shows one card
        print("The cards have been dealt - the dealer will show their first card...\n")
        self.dealer.show_hand_during_player_turn()
        print("\n")
        # go through each player in player list - show hand then give option if want new card - show hand again
        score_dict = {}
        for player in self.get_list_of_players():
            bust_flag = False
            twenty_one_flag = False
            print("It is {}'s turn.\nShowing their initial hand of cards...\n".format(player.get_username()))
            player.show_hand()
            if player.get_points_of_hand() == 21:
                twenty_one_flag = True
            else:
                while player.make_game_decision():
                    player.add_card_to_hand(self.deck.give_n_cards(1))
                    print("You took another card!")
                    player.get_hand()[-1].show()
                    # if points get to equal or exceed 21 will move onto next players turn
                    if player.get_points_of_hand() > 21:
                        bust_flag = True
                        break
                    if player.get_points_of_hand() == 21:
                        twenty_one_flag = True
                        break
            if bust_flag:
                print("Points of {}'s hand is {}. Score over 21 so moving onto next player's turn.\n".format(player.get_username(), player.get_points_of_hand()))
            elif twenty_one_flag:
                print("{} has 21! Moving onto next player's turn.\n".format(player.get_username()))
            else:
                print("{} chose to stand with score {} - moving onto next player's turn.\n".format(player.get_username(), player.get_points_of_hand()))
            # put each player and their final score in a dictionary
            score_dict[player] = player.get_points_of_hand()

        # after all players in list have had turn move onto dealer
        print("All players have played. Now it is the dealer's turn. Showing both cards in their initial hand:")
        self.dealer.show_hand()
        # continues to add cards to hand until score exceeds 17 then shows hand
        if min(score_dict.values()) > 21:
            self.set_winner(self.dealer)
            print("The dealer won as all players had scores over 21.\n")
        else:
            while self.dealer.make_game_decision():
                print("Dealer's score was less than 17 - dealer taking one more card")
                self.dealer.add_card_to_hand(self.deck.give_n_cards(1))
                self.dealer.get_hand()[-1].show()
            # put dealer's score in dictionary also to allow comparing for winners
            score_dict[self.dealer] = self.dealer.get_points_of_hand()
            print("Showing the dealer's final hand with score {}.".format(self.dealer.get_points_of_hand()))
            self.dealer.show_hand()
            print("\n")

            # compare scores of player(s) to dealer: anyone with 21 win/joint win; if all less than 21 highest wins; if players all over 21 dealer win
            winner_list = []
            if self.dealer.get_points_of_hand() == 21:
                winner_list.append(self.dealer)
            elif self.dealer.get_points_of_hand() > 21:
                del score_dict[self.dealer]

            for player in self.list_of_players:
                if player.get_points_of_hand() == 21:
                    winner_list.append(player)
                elif player.get_points_of_hand() > 21:
                    #loser_list.append(player)
                    del score_dict[player]

            if len(winner_list) == 1:
                self.winner = winner_list[0]
                print("There is one winner! {} has 21 and has won!\n".format(winner_list[0].get_username()))
            elif len(winner_list) >= 2:
                self.winner = None
                print("Draw! The players with 21 are: {}!\n".format(' and '.join(x.get_username() for x in winner_list)))
            #if no one got 21 find highest score of those who did not exceed 21 - these are winner
            elif len(winner_list) == 0:
                top_score = max(score_dict.values())
                for player in score_dict:
                    if score_dict[player] == top_score:
                        winner_list.append(player)
                if len(winner_list) == 1:
                    self.winner = winner_list[0]
                    print("The winner is {} with a score of {}".format(winner_list[0].get_username(),top_score))
                if len(winner_list) > 1:
                    self.winner = None
                    print("The game was a draw between {}.".format(' and '.join([x.get_username() for x in winner_list])))
