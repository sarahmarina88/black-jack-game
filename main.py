from BlackJackPcg.Deck import Deck


if __name__ == '__main__':
    d = Deck()
    d.init_deck()
    d.print_deck()
    print()
    d.shuffle_deck()
    d.print_deck()

