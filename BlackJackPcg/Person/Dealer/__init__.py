from BlackJackPcg.Person import Person


class Dealer(Person):
    def __init__(self, username):
        super().__init__(username)
        self.username = 'bot'
        self.hand = []  # start with empty list - will hold the cards the player has

    def make_game_decision(self):
        pass
    #check score of hand - if less than 17 take a card otherwise stop?

    def show_hand_during_player_turn(self):
        self.hand[0].show()