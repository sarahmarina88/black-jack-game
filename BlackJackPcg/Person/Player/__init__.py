from BlackJackPcg.Person import Person

class Player(Person):

    def __init__(self, username):
        super().__init__(username)

    def make_game_decision(self):
        decision_flag = True
        decision_input_count = 0
        while decision_flag and decision_input_count <= 3:
            try:
                choice = int(input("Would you like to take a card? Enter 1 for yes or 0 for no:"))
                if choice == 0:
                    decision_flag = False
                    return False
                elif choice == 1:
                    decision_flag = False
                    return True
                else:
                    print("Please enter only 1 for yes or 0 for no.")
                    decision_input_count += 1
            except ValueError as e:
                print("Please enter decision to take a card as an integer (0 for no, 1 for yes)")
                decision_input_count += 1
        if decision_input_count > 3:
            print("Sorry you put in too many invalid inputs - ending game!")
            exit(1)

