from BlackJackPcg.Deck import Deck
from BlackJackPcg.Person.Player import Player

if __name__ == '__main__':
    d = Deck()
    p = Player('player')
    d.init_deck()
    #print(len(d.deck))
    #d.print_deck()
    #print()
    d.shuffle_deck()
    #d.print_deck()
    p.add_card_to_hand(d.give_n_cards(3))
    p.show_hand()
