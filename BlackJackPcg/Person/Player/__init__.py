from abc import ABC

from BlackJackPcg.Person import Person


class Player(Person, ABC):

    def __init__(self, username):
        super().__init__(username)
        self.username = username
        self.hand = []  # start with empty list - will hold the cards the player has


    def make_game_decision(self):
        pass
