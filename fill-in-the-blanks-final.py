from random import shuffle
import sys
import time
from time import sleep

# A list of blank spaces to be passed in to the play_game function.
blank_space = ["__1__", "__2__", "__3__", "__4__"]

# The following three strings are seperate quizes to pass into the play_game function
easy = ("Python is a __1__ language that allows computer scientists to build software programs. "
        "Guido von Rossum created Python in December __2__ in Amsterdam. The most basic __3__ in Python "
        "is __4__, often used by beginners to tell Python to display 'Hello World' on the screen. ")
medium = ("A string object is __1__, i.e. it cannot be modified after it has been created. "
          "An important concept in Python and other programming languages is the __2__, used to store a value. "
          "To assign a value to a variable use the __3__ operator. A more versatile and mutable data "
          "type in Python is __4__, containing items separated by commas and within square brackets. ")
hard =  ("In Python, the most common flow control statement is __1__ which lets you branch based on a condition. "
         "Looping commands like __2__ execute statements a given number of times, or __3__ repeats "
         "statements as long as a condition remains True. Loop statements may have an __4__ clause "
         "that is executed when the loop terminates through exhaustion of the list (with for) "
         "or when the condition becomes false (with while). ")

# A list of answers for each of the three quizes
easy_answers = ['programming', '1989', 'command', 'print']
medium_answers = [ 'immutable', 'variable', 'equals', 'list']
hard_answers = ['if', 'for', 'while', 'else']

def play_game(string, answers):
    """
    The play_game function prompts the user for raw_input to complete a quiz
    : param string: user selects quiz
    : param answers: user fills in the blank with raw_input
    """
    for answer in answers:
        user_input = raw_input("What should fill in the blank" + blank_space[answers.index(answer)])
        while user_input != answer:
            user_input = raw_input("Incorrect, try again: ")
        string = string.replace(blank_space[answers.index(answer)], user_input)
        print string
    print "You finished the level!"
        
def select_difficulty():
    """
    The select_difficulty function prompts the user to choose a quiz level and 
    the calls the play_game function with the corresponding parameters
    """
    while True:
        difficulty = raw_input("Choose a difficulty for the quiz: Type EASY, MEDIUM or HARD to continue.  ")
        if difficulty.upper() == "EASY":
            print "Please read the following paragraph, then fill in the blanks when prompted. "
            print easy
            play_game(easy, easy_answers)
        elif difficulty.upper() == "MEDIUM":
            print "Please read the following paragraph, then fill in the blanks when prompted. "
            print medium
            play_game(medium, medium_answers)
        elif difficulty.upper() == "HARD":
            print "Please read the following paragraph, then fill in the blanks when prompted. "
            print hard
            play_game(hard, hard_answers)

select_difficulty()


'''
Used multiple web sources outside Udacity including:
https://review.udacity.com/#!/reviews/95377
https://teamtreehouse.com/community/fill-in-the-blank-python-basic
http://stackoverflow.com/questions/34642044/fill-in-blanks-game
http://stackoverflow.com/questions/34596868/validating-user-input-in-a-fill-in-the-blanks-program-using-python
'''
