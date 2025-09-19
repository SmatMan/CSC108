"""CSC108H1: Fall 2025 -- Assignment 1: Mystery Message Functions

Instructions (READ THIS FIRST!)
===============================

Make sure that the files a1_checker.py, a1_pyta.json, checker_generic.py
and mystery_message_game.py are in the same folder as this file
(mm_functions.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students 
taking the CSC108H1 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2025 CSC108H1 Teaching Team
"""

# points earned on each occurrence of a correctly guessed consonant
CONSONANT_POINTS = 1

# cost of buying a vowel, does not depend on the number of occurrences
VOWEL_COST = 1

# points earned on each occurrence of hidden consonants at the time of
# solving the puzzle
CONSONANT_BONUS = 2

# players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# menu options
CONSONANT = 'C'  # guess a consonant
VOWEL = 'V'      # buy a vowel
SOLVE = 'S'      # try to solve the puzzle
QUIT = 'Q'       # quit the game

# symbol used for hidden characters
HIDDEN = '^'

# Game types
HUMAN = 'P1'             # one player, human
HUMAN_HUMAN = 'PVP'      # two players, human+human (player vs player)
HUMAN_COMPUTER = 'PVE'   # two players, human+computer (player vs environment)

# computer difficulty levels
EASY = 'E'  # computer plays the "easy" strategy
HARD = 'H'  # computer plays the "hard" strategy

# all consonants and all vowels
ALL_CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALL_VOWELS = 'aeiou'

# the order in which a computer player, hard difficulty level, will
# guess consonants
PRIORITY_CONSONANTS = 'tnrslhdcmpfygbwvkqxjz'


# We provide this function as an example.
# This function is already complete. You must not modify it.
def is_win(view: str, message: str) -> bool:
    """Return True if and only if message and view are a winning
    combination. That is, if and only if message and view are the same.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('a^^le', 'apple')
    False
    >>> is_win('app', 'apple')
    False
    """

    return message == view


# We provide this function as an example of using a function as a helper.
# This function is already complete. You must not modify it.
def is_game_over(view: str, message: str, move: str) -> bool:
    """Return True if and only if message and view are a winning
    combination or move is QUIT.

    >>> is_game_over('a^^le', 'apple', VOWEL)
    False
    >>> is_game_over('a^^le', 'apple', 'Q')
    True
    >>> is_game_over('apple', 'apple', 'S')
    True
    """

    return move == QUIT or is_win(view, message)


# Helper function for computer_chooses_solve
# This function is already complete. You must not modify it.
def half_revealed(view: str) -> bool:
    """Return True if and only if at least half of the alphabetic
    characters in view are revealed.

    >>> half_revealed('')
    True
    >>> half_revealed('x')
    True
    >>> half_revealed('^')
    False
    >>> half_revealed('a^,^c!')
    True
    >>> half_revealed('a^b^^e ^c^d^^d')
    False
    """

    num_hidden = view.count(HIDDEN)
    num_alphabetic = 0
    for char in view:
        if char.isalpha():
            num_alphabetic = num_alphabetic + 1
    return num_alphabetic >= num_hidden


# Implement the required functions below.
#
# We have provided the complete docstring (but not the body!) for the first
# function you are to write.  Write a function body for the function
# is_human.
#
# The header and docstring of is_human is an example of where and how to use
# constants in the docstring. We use the default values of constants in
# the docstring examples, but must use the constants in the function body.

def is_human(current_player: str, game_type: str) -> bool:
    """Return True if and only if current_player represents a human in a
    game of type game_type.
    current_player is PLAYER_ONE or PLAYER_TWO.
    game_type is HUMAN, HUMAN_HUMAN, or HUMAN_COMPUTER.

    In a HUMAN game or a HUMAN_HUMAN game, a player is always
    human. In a HUMAN_COMPUTER game, PLAYER_ONE is human and
    PLAYER_TWO is computer.

    >>> is_human('Player One', 'P1')
    True
    >>> is_human('Player One', 'PVP')
    True
    >>> is_human('Player Two', 'PVP')
    True
    >>> is_human('Player One', 'PVE')
    True
    >>> is_human('Player Two', 'PVE')
    False
    """

    if game_type != HUMAN_COMPUTER:
        return True
    elif current_player == PLAYER_ONE:
        return True
    else:
        return False



# Now define the other functions described in the handout.
# Follow the Function Design Recipe to produce complete functions for
# is_one_player_game, current_player_score, is_bonus_letter, 
# get_updated_char_view, calculate_score, next_player, is_fully_hidden,
# computer_chooses_solve, and remove_at_index.
def is_one_player_game(game_type: str) -> bool:
    """Return True if and only if game_type represents a single person (HUMAN)
    
    >>> is_one_player_game('PVE')
    False
    >>> is_one_player_game('P1')
    True
    >>> is_one_player_game('PVP')
    False
    """
    
    return game_type == HUMAN

# def is_player():

def current_player_score(p1_score: int, p2_score: int, current_player: str) -> int:
    """Return the score of the current player, represented by parameter current_player
    
    >>> current_player_score(5, 6, "Player One")
    5
    >>> current_player_score(5, 6, "Player Two")
    6
    """
    
    if current_player == PLAYER_ONE:
        return p1_score
    else:
        return p2_score
    
def is_bonus_letter(view: str, guessed_letter: str, message: str) -> bool:
    """Returns True if and only if parameter guessed_letter is a bonus letter 
    (bonus letter meaning a hidden consonant)
    
    >>> is_bonus_letter("^ell^", "h", "hello")
    True
    >>> is_bonus_letter("hell^", "h", "hello")
    False
    >>> is_bonus_letter("hell^", "o", "hello")
    False
    """
    
    if guessed_letter not in ALL_CONSONANTS:
        return False # return false if guessed letter isnt a consonant(is vowel)
    
    if guessed_letter in message and guessed_letter not in view:
        return True # true if g_l is in hidden msg but not in view
    
    return False # this shld only happen if g_l is not in msg or is shown

def get_updated_char_view(view: str, message: str, char_index: int, guess:str) -> str:
    """Return either updated character if parameter guess is at message[char_index],
    else return original character
    
    len(message) - 1 > char_index > 0; 
    
    >>> get_updated_char_view("h^^^o", "hello", 1, "e")
    "e"
    >>> get_updated_char_view("h^^^o", "hello", 3, "e")
    "^"
    >>> get_updated_char_view("h^^^o", "hello", 3, "l")
    "l"
    """
    
    og_character = view[char_index]
    potential_character = message[char_index]
    
    if og_character == HIDDEN:
        if potential_character == guess:
            return potential_character
    return og_character

def calculate_score(curr_score: int, num_revealed: int, move: str) -> int:
    """Return player's updated score based on whether move is 
    
    
    """
    
    
        