from unittest import TestCase, mock

from BlackJackPcg.Person.Player import Player


class TestPlayer(TestCase):

# what is inherited from the class Person is tested in the test_person
# only to test the game decision function

    def test_make_game_decision_gives_true_for_input_1(self):
        p = Player("test_player")
        with mock.patch("builtins.input", return_value=1):
            self.assertTrue(p.make_game_decision())

    def test_make_game_decision_gives_false_for_input_0(self):
        p = Player("test_player")
        with mock.patch("builtins.input", return_value=0):
            self.assertFalse(p.make_game_decision())

    def test_make_game_decision_gives_error_for_invalid_integer_input(self):
        p = Player("test_player")
        #make the input so it will be three
        with mock.patch("builtins.input", return_value=3):
            #this should return a print statement - also mock the print but also cause an exception otherwise loop won't ever break
            #side effect - to happen when the mock is called so as to break the loop
            with mock.patch("builtins.print", side_effect=[Exception("To break the while loop")]) as mocked_print:
                #exception will be reaised as a statement is printed
                with self.assertRaises(Exception) as cm:
                    p.make_game_decision()
                    the_exception_raised = cm.exception
                #check that the print was called and with the expected message; side effect was an exception which was raised - can check exception raised
                mocked_print.assert_called_with("Please enter only 1 for yes or 0 for no.") and self.assertTrue(the_exception_raised == "To break the while loop")

    def test_make_game_decision_gives_value_error_when_string_as_input(self):
        p = Player("test_player")
        # mock to input a string - need to check that a ValueError results

    def test_make_game_decision_prints_message_when_string_as_input(self):
        p = Player("test_player")
        # mock to input a string - should cause a value error and then print message - also mock the print to check is correct
        with mock.patch("builtins.input", return_value = 'one'):
            # mock for the print after value error from str input
            # will continue as a loop - make a side effect of mocking the print is to give an Exception - breaks the while loop
            with mock.patch("builtins.print", side_effect=[Exception("To break the while loop")]) as mocked_print:
                with self.assertRaises(Exception):
                    p.make_game_decision()
            # assert whether the expected print statement was shown
            mocked_print.assert_called_with("Please enter decision to take a card as an integer (0 for no, 1 for yes)")

    def test_function_gives_message_and_keeps_asking_input_until_valid(self):
        p = Player("test_player")
        # mock to input different inputs in sequence - first three should cause print message, last (1) correct so breaks - also mock the print to check is correct
        with mock.patch("builtins.input", side_effect=['one', 3, 3.5, 1]):
            # mock for the printed messages after value error from string input or invalid numbers
            # will continue as a loop as without exception side effect of mocked print - last input of list correct to break loop
            with mock.patch("builtins.print") as mocked_print:
                p.make_game_decision()
            # gave three incorrect inputs before valid input so should have three times printed something
            self.assertTrue(mocked_print.call_count == 3)
