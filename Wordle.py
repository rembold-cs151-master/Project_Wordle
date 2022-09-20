########################################
# Name:
# Collaborators (if any):
# Estimated time spent (hr):
########################################

from WordleGraphics import WordleGWindow
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
import random

def wordle():
    """ The main function to play the Wordle game. """

    def enter_action():
        """ What should happen when the RETURN or ENTER key is pressed. """
        gw.show_message("You need to implement this method")


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
