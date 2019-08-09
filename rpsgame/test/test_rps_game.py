"""
##########################
#   RPS GAME  Test Cases #
##########################
Created on May 15, 2019

@author: ksivalin
"""

from rps_game import rps_game as rps_game
from rps_game.rps_game import  USER_CHOICES
from unittest.mock import patch
import unittest
import xmlrunner


class TestRPSGame(unittest.TestCase):
    """A class whose instances are single test
    cases for RPS Game.
    """
    def __init__(self, *args, **kwargs):
        super(TestRPSGame, self).__init__(*args, **kwargs)

    def test_input_validation_pass1(self):
        user_input = ['1','XXX','1','n']
        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(SystemExit) as cm:
                rps_game.RPSGame().input_validation()
            self.assertEqual(cm.exception.code, 0)

    def test_input_validation_pass2(self):
        user_input = ['2','n']
        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(SystemExit) as cm:
                rps_game.RPSGame().input_validation()
            self.assertEqual(cm.exception.code, 0)

    def test_input_validation_fail1(self):
        user_input = ['q']
        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(SystemExit) as cm:
                rps_game.RPSGame().input_validation()
            self.assertEqual(cm.exception.code, -1)

    def test_input_validation_pass3(self):
        user_input=['1','xxx','3','Y','1','mozhi','2', 'n']
        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(SystemExit) as cm:
                rps_game.RPSGame().input_validation()
            self.assertEqual(cm.exception.code, 0)

    def test_input_validation_pass4(self):
        user_input=['2','y','2','n']
        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(SystemExit) as cm:
                rps_game.RPSGame().input_validation()
            self.assertEqual(cm.exception.code, 0)

    def test_input_validation_fail(self):
        user_input=['3']
        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(SystemExit) as cm:
                rps_game.RPSGame().input_validation()
            self.assertEqual(cm.exception.code, -1)

    def test_get_input_pass(self):
        user_input=['x']
        with patch('builtins.input', side_effect=user_input):
            self.assertEqual(rps_game.get_input("Hi.."),'x')

    def test_exit_game(self):
        with self.assertRaises(SystemExit) as cm:
            rps_game.exit_game()
        self.assertEqual(cm.exception.code, -1)

    def test_validate_pass(self):
        with self.assertRaises(SystemExit) as cm:
            rps_game.validate('q',USER_CHOICES)
        self.assertEqual(cm.exception.code, -1)
        self.assertIsNone(rps_game.validate('1',USER_CHOICES))

    def test_validate_fail(self):
        with self.assertRaises(SystemExit) as cm:
            rps_game.validate('W',USER_CHOICES)
        self.assertEqual(cm.exception.code, -1)

    def test_start_game_pass(self):
        user_input=['2','n']
        with patch('builtins.input', side_effect=user_input):
            rps_game.RPSGame().start_game()

    def test_evaluate_result(self):
        self.assertTrue(rps_game.RPSGame().evaluate_result("1","1"))
        self.assertTrue(rps_game.RPSGame().evaluate_result("1","3"))
        self.assertTrue(rps_game.RPSGame().evaluate_result("2","3"))

    def test_countdown(self):
        self.assertIsNone(rps_game.countdown(2))
        self.assertIsNone(rps_game.countdown('1'))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),failfast=False, buffer=False, catchbreak=False)
