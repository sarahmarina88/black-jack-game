from BlackJackPcg.Person import Person


class Dealer(Person):
    def __init__(self, username):
        super().__init__(username)

    def make_game_decision(self):
        if self.get_points_of_hand() >= 17:
            return False
        if self.get_points_of_hand() < 17:
            return True

    def show_hand_during_player_turn(self):
        self.hand[0].show()
