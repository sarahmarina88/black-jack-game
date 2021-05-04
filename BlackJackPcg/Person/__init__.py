from abc import abstractmethod, ABC


class Person(ABC):
    def __init__(self, username):
        self.username = username
        self.hand = []

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def get_hand(self):
        return self.hand

    def get_points_of_hand(self):
        points_before_aces = 0
        ace_count = 0
        for card in self.hand:
            if card.get_number() in ["J", "Q", "K"]:
                points_before_aces += 10
            elif card.get_number() != "A":
                points_before_aces += (int(card.get_number()))
            else:
                ace_count += 1
        if ace_count == 0:
            return points_before_aces
        else:
            points = (points_before_aces + (ace_count * 11))
            if points <= 21:
                return points
            else:
                for i in range(ace_count):
                    points = points - 10
                    if points <= 21:
                        return points

    def add_card_to_hand(self, list_of_cards):
        for card in list_of_cards:
            self.hand.append(card)

    def show_hand(self):
        for card in self.hand:
            card.show()

    @abstractmethod
    def make_game_decision(self):
        pass  # this is abstractmethod as different implementation for the player and the dealer
