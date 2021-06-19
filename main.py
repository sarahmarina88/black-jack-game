from BlackJackPcg.Game import Game
from BlackJackPcg.Person.Player import Player

if __name__ == '__main__':

    list_of_players_names = []
    need_number_players = True

    while need_number_players:
        try:
            num_players = int(input("How many players are playing?"))
            if num_players <= 0:
                print("There has to be at least one player! Enter the number of players as an integer.")
            elif num_players > 4:
                print("Up to four players can be added. Enter the number of players as an integer.")
            else:
                need_number_players = False
        except ValueError as e:
            print("Please enter number of players as an integer!")

    # need to edit so names cannot be blank
    for n in range(num_players):
        if n == 0:
            player_name = input("Enter the first player's username:")
            list_of_players_names.append(player_name)
        else:
            player_name = input("Enter the next player's username:")
            list_of_players_names.append(player_name)
    print("{} players have been added! You will be playing against a dealer called Bot.".format(num_players))

    # way to count how many rounds each player won
    games_won_dict = {}
    for name in list_of_players_names:
        games_won_dict[name] = 0
    games_won_dict["bot"] = 0

    play_game_flag = True
    while play_game_flag:
        # have taken the names of players, make into list of players
        list_of_players = [Player(name) for name in list_of_players_names]
        # play the game with the list of players
        g = Game(list_of_players)
        g.play_game()
        # add the winner to counts of number of games won dictionary
        if g.get_winner() is not None:
            games_won_dict[g.get_winner().get_username()] += 1
        # see if user wants to play again
        new_game_choice_needed = True
        while new_game_choice_needed:
            try:
                new_game_dec = int(input("Would you like to play another game? Enter 1 for yes or 0 for no."))
                if new_game_dec == 0:
                    play_game_flag = False
                    new_game_choice_needed = False
                elif new_game_dec == 1:
                    new_game_choice_needed = False
                else:
                    print("Please enter only 1 for yes or 0 for no.")
            except ValueError as e:
                print("Please enter answer as an integer (0 for no, 1 for yes).")

    print("\nThe overall number of games won by each player were:-")
    for name in games_won_dict:
        print("- {} won {} games".format(name, games_won_dict[name]))

    #say who won overall
