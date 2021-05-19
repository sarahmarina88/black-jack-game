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
        points_before_ace = 0
        ace_count = 0
        for card in self.hand:
            if card.get_card_value() == 11:
                ace_count += 1
            else:
                points_before_ace += card.get_card_value()
        # if all aces as 11 gives 21 or less return this
        if points_before_ace + (11 * ace_count) <= 21:
            return points_before_ace + (11 * ace_count)
        # check one ace as 11 and the rest as 1 (2 or more aces as 11 -over 21) - if 21 or less return this
        elif points_before_ace + 11 + ace_count - 1 <= 21:
            return points_before_ace + 11 + ace_count - 1
        # otherwise make all aces as 1
        else:
            return points_before_ace + ace_count

    def add_card_to_hand(self, list_of_cards):
        self.hand.extend(list_of_cards)

    def show_hand(self):
        for card in self.hand:
            card.show()

    @abstractmethod
    def make_game_decision(self):
        pass

