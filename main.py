from BlackJackPcg.Deck import Deck


class Player:
    pass


if __name__ == '__main__':
    d = Deck()
    d.init_deck()
    d.print_deck()
    print()
    d.suffle_deck()
    d.print_deck()
    print()
