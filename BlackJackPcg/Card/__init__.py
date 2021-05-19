from BlackJackPcg.Utils import CardUtils


class Card:

    def __init__(self, suit, number):
        if number not in CardUtils.get_possible_numbers():
            raise RuntimeError("the number passed to the card is not valid")

        if suit not in CardUtils.get_possible_suits():
            raise RuntimeError("the suit passed to the card is not valid")

        self.suit = suit
        self.number = number

    def get_number(self):
        return self.number

    def get_suit(self):
        return self.suit

    def show(self):
        print(self.to_string())

    def to_string(self):
        return "The card is: {}{}".format(self.number, self.suit)

    def get_card_value(self):
        if self.get_number() in ["J","Q","K"]:
            return 10
        elif self.get_number() == "A":
            return 11
        else:
            return int(self.get_number())
