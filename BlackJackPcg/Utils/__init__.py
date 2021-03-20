class CardUtils:

    @staticmethod
    def get_possible_suits():
        return ["S", "C", "H", "D"]

    @staticmethod
    def get_possible_colors():
        return ["R", "B"]

    @staticmethod
    def get_possible_numbers():
        possible_numbers = ["{}".format(x) for x in range(2, 11)]
        possible_numbers.extend(["J", "Q", "K", "A"])
        return possible_numbers
