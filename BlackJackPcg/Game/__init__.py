from BlackJackPcg.Deck import Deck


class Game:

    def __init__(self, list_of_players, dealer):
        self.deck = Deck()
        self.list_of_players = []
        self.dealer = dealer

    def initialise_deck(self):
        self.deck.init_deck()

    def shuffle_deck(self):
        self.deck.shuffle_deck()

    def give_first_hand_of_cards(self):
        pass
    # two cards from the deck and give to the player, give two to the dealer - removed from deck card list

    def add_player(self, player):
        pass
    #to add player to the list of players - unsure if needed?

    def determine_winner(self):
        pass
    #to state who has won the game from the scores