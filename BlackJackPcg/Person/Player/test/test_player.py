import contextlib
import io
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
        with mock.patch("builtins.input", side_effect=[3,1]):
            #this should return a print statement - redirect to buffer
            # #side effect - two different inputs, second will break loop
            with io.StringIO() as buffer:
                with contextlib.redirect_stdout(buffer):
                    p.make_game_decision()
                    printed_text = buffer.getvalue()
                    self.assertTrue(printed_text.count("Please enter only 1 for yes or 0 for no.") ==1)

    def test_make_game_decision_gives_expected_message_when_string_as_input(self):
        # don't have to test for both error and message - the error is only way to get the message
        # by giving list of inputs can break the loop - also checking can keep inputting till correct
        p = Player("test_player")
        # mock to input a string - need to check that a ValueError results
        with mock.patch("builtins.input", side_effect=['one', 'two', 1]):
            with io.StringIO() as buffer:
                # redirect the stdout to the buffer - whatever goes to stdout will go to buffer
                with contextlib.redirect_stdout(buffer):
                    p.make_game_decision()
                    printed_text = buffer.getvalue()
                    #check that the printed text contains the intended message two times - as final value input is 1 will return true
                    self.assertTrue(printed_text.count("Please enter decision to take a card as an integer (0 for no, 1 for yes)") == 2)

    def test_function_gives_message_and_keeps_asking_input_until_valid(self):
        p = Player("test_player")
        # mock to input different inputs in sequence - first three should cause print message, last (1) correct so breaks - also mock the print to check is correct
        with mock.patch("builtins.input", side_effect=['one', 3, 3.5, 1]):
            with io.StringIO() as buffer:
                with contextlib.redirect_stdout(buffer):
                    p.make_game_decision()
                    printed_text = buffer.getvalue()
                    self.assertTrue(printed_text.count("Please enter") == 3)


