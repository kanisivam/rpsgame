"""
##########################
#   RPS GAME   #
##########################
Created on May 15, 2019

@author: ksivalin
"""
import random
import sys
import time
OPTIONS = {"1": "Rock", "2": "Paper", "3": "Scissors"}
USER_CHOICES = ['1', '2', 'q', 'y', 'n']
COMPUTER = 'Computer'
SELECT_PLAY_MODE = """\nPlease Select Play Mode:
1 - Player vs Computer
2 - Computer Vs Computer
q - quit"""
INVALID_CHOICE = "Oops! You have selected invalid choice : {0}.." \
                 "Try again to pick choices from :{1}"
CHANGE_PLAY_MODE = """\nDo you want to change play mode ?
y - Yes
n - No """
INSTRUCTIONS = """Winning Rules of the Rock paper scissor game as follows: 
Rock vs paper->paper wins 
Rock vs scissor->Rock wins 
paper vs scissor->scissor wins"""
COMP_PLAYER1 = "Computer 1"
COMP_PLAYER2 = "Computer 2"


class RPSGame:
    """Rock Paper Scissiors Game.
    This is an Interactive Script to take input from user to
     play Rock Paper Scissor Game.
    Get Play Mode Selection input from user (Player vs computer / Computer1 vs Computer2).
    Changing play mode option should be given to the user.
    Once Play mode is selected by user, for eg: Player vs Computer,
    take input from user and let consider random choice/move
     as computer choice
    and apply Rock Paper Scissors Game rule to find out winner.
    computer choice = generate random number
    user choice = Get input from user;
    outcome = Apply rule/logic to evaluate winner
    (compchoice, userchoice) and display the winner.

    """
    def __init__(self):
        """Initialize an instance..
        """
        self.player1 = ''
        self.player2 = COMPUTER
        self.player_name = 'Player'

    def input_validation(self):
        """
        Get input from user such as play mode and name of player
        and validate user selected choice with the list of
        choices defined.
        """
        print("Hello!! Welcome to Play 'Rock...Scissor...Paper ...!! Game'")
        print("-----------------------------------------------------------")
        print(INSTRUCTIONS)
        while True:
            user = get_input(SELECT_PLAY_MODE)
            validate(user, USER_CHOICES[0:3])
            if user == '1':
                name = get_input("\nEnter Player Name : ")
                self.player1 = name if name else 'Player'
            else:
                self.player1, self.player2 = COMP_PLAYER1, COMP_PLAYER2
            self.start_game()
            user_input = get_input(CHANGE_PLAY_MODE)
            validate(user_input, USER_CHOICES[2:])
            if user_input.lower() == 'y':
                continue
            print("\nThanks for playing")
            sys.exit(0)

    def start_game(self):
        """
        start game between user selected player and computer or computer vs computer.
        and evaluate the results.
        """
        print("\nBe Ready!! Game will be Started between '{0}' vs '{1}' in few seconds ".format(self.player1, self.player2), end='', flush=True)
        countdown(5)
        print("\n")
        if self.player1 != COMP_PLAYER1:
            print("Choose Move \n 1. Rock \n 2. paper \n 3. scissor \n")
            p1_choice = get_input("Hey {0} ,Choose Your Move: ".format(self.player1)).lower()
        else:
            p1_choice = random.choice(list(OPTIONS.keys()))
        validate(p1_choice, OPTIONS.keys())
        p2_choice = random.choice(list(OPTIONS.keys()))
        if self.player1 != COMP_PLAYER1:
            print("Now its {0} turn.......".format(self.player2))
        print('"{0}" Move is :  {1}'.format(self.player1, OPTIONS[p1_choice]))
        print('"{0}" Move is :  {1}'.format(self.player2, OPTIONS[p2_choice]))
        print(self.evaluate_result(p1_choice, p2_choice))

    def evaluate_result(self, p1_choice, p2_choice):
        """
        Evaluate results..
        :param p1_choice: player1 move <str>
        :param p2_choice: player2 move <str>
        :return:
        """
        if p2_choice == p1_choice:
            msg = '<**** Oh! its a tie between {0} and {1} ****> <**** {2} tie {3} ****> '.format(self.player1, self.player2, OPTIONS.get(p1_choice), OPTIONS.get(p2_choice))
        elif (p1_choice, p2_choice) in (("1", "3"), ("2", "1"), ("3", "2")):
            msg = "<**** {0} wins ****><**** {1} wins ****>".format(OPTIONS.get(p1_choice), self.player1)
        else:
            msg = "<**** {0} wins ****><**** {1} wins ****>".format(OPTIONS.get(p2_choice), self.player2)
        return msg


def validate(user, choices):
    """
    validate user entered value and the list of allowed OPTIONS
    :param user: user selected choice <str>
    :param choices: available choices defined <list>
    """
    if user.lower() == 'q':
        exit_game()
    if user.lower() not in choices:
        print(INVALID_CHOICE.format(user, choices))
        sys.exit(-1)


def get_input(message):
    """
    get input from user for the given message
    :param message: <str>
    :return: user selected val
    """
    val = input(message).strip()
    return val


def exit_game():
    """
    exit the game.
    :return: system exit -1
    """
    print("Quit the Game..")
    sys.exit(-1)


def countdown(num):
    """
    count down - intentionally adding an delay
    :param num:delay in seconds <int>
    """
    if not isinstance(num, int):
        return
    for x in range(num, 0, -1):
        print('{}  '.format(x), end="", flush=True)
        time.sleep(1)


if __name__ == '__main__':
    rps_game = RPSGame()
    rps_game.input_validation()
