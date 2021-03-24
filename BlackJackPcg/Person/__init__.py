from abc import abstractmethod, ABC


class Person(ABC):
    def __init__(self, username):
        self.username = username
        self.hand = []

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def get_points_of_hand(self):
        pass

    def add_card_to_hand(self, list_of_cards):
        pass

    def show_hand(self):
        for card in self.hand:
            card.show()

    @abstractmethod
    def make_game_decision(self):
        pass  # this is abstractmethod as different implementation for the player and the dealer
