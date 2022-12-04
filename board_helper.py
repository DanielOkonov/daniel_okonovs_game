import itertools
import random

import riddle_helper
import fight_helper
import arch_rival_fight_helper


# import collections
# collections.Callable = collections.abc.Callable

def make_board(rows, columns):
    """
    Create a game board.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: both parameters must be given positive integers
    :postcondition: creates a 2-D list which represents a board
    :return: a two-dimensional list which represents a board
    """
    board = [[None for x in range(columns)] for x in range(rows)]

    riddles = riddle_helper.create_riddles()
    fights = fight_helper.create_fights()
    all_challenges = []
    for riddle in riddles:
        all_challenges.append(riddle)
    for fight in fights:
        all_challenges.append(fight)

    # starting from 1 cause at cell 0 there is a hero
    # ending one short cause at last cell there is an arc-rival
    random_cells_for_challenges = random.sample(range(1, rows * columns - 1), len(all_challenges))

    cell_id = 0
    challenge_id = 0
    for rowId in range(rows):
        for column in range(columns):
            if cell_id in random_cells_for_challenges:
                board[rowId][column] = all_challenges[challenge_id]
                challenge_id += 1
            cell_id += 1

    board[rows - 1][columns - 1] = arch_rival_fight_helper.create_arch_rival_fight()

    return board


def get_all_cells(board):
    """
    Return all cells of board as a regular list

    :param board: 2-D list
    :precondition: board must be 2-D list
    :postcondtion: represents the 2-D list as a regular list
    :return: all cells of board as a regular list

    >>> get_all_cells([[None, None], [None, None]])
    [None, None, None, None]
    """
    return [cell for row in board for cell in row]


def describe_board(board):
    """
    Describe the board for the user.

    :param board: a 2-D list
    :precondition: board is a 2-D list of positive numbers representing the rows and columns
    :postcondition: describes how the board looks
    :return: a string that describes what the board looks like
    """
    filled_cells = [c for c in get_all_cells(board) if c is not None]
    grouped_challenges = [(k, len(list(g))) for k, g in itertools.groupby(filled_cells, lambda c: c['type'])]
    remaining_challenges_string = ', '.join("{} - {}".format(g[0], g[1]) for g in grouped_challenges)

    description = f'Gotham City has {len(board)} Avenues and {len(board[0])} Streets.'
    description += '\nRemaining challenges: '
    description += remaining_challenges_string

    return description


def build_board_map(board, character_position, character_symbol):
    """
    Create the visual map that the user will see.

    :param board: a 2-D list of challenges
    :param character_position: a tuple made up of a row and column
    :param character_symbol: the emoji representing the position of the character
    :precondition: parameters must have described expected values
    :postcondition: a map of the board is printed
    :return: a string representation of a map
    """
    chars_per_cell = 7
    row_separator = '\n' + '-' * len(board[0]) * chars_per_cell + '\n'
    board_map = ''
    board_map += row_separator

    for row in range(len(board)):
        for column in range(len(board[0])):
            board_map += '|  '
            a_thing = board[row][column]
            if a_thing is not None:
                board_map += a_thing['map_symbol']
            elif character_position[0] == row and character_position[1] == column:
                board_map += character_symbol
            else:
                board_map += '🏿'
            board_map += '  '
        board_map += '|'
        board_map += row_separator

    return board_map


def try_move(board, character_position, user_choice):
    """
    Determine new board position based off of player movement.

    :param board: a 2-D list
    :param character_position: a tuple made up of a row and column
    :param user_choice: a letter representing in which direction the character should move
    :precondition: parameters must have described expected values
    :postcondition: character will move to a new position within the map
    :return: a boolean
    """
    message_format = "You are on the {direction}ern border of the Gotham city, cannot go further {direction}"
    if user_choice == 'N':
        if character_position[0] == 0:
            return False, message_format.format(direction='north')
        return True, (character_position[0] - 1, character_position[1])
    if user_choice == 'E':
        if character_position[1] == len(board[0]) - 1:
            return False, message_format.format(direction='east')
        return True, (character_position[0], character_position[1] + 1)
    if user_choice == 'S':
        if character_position[0] == len(board) - 1:
            return False, message_format.format(direction='south')
        return True, (character_position[0] + 1, character_position[1])
    if user_choice == 'W':
        if character_position[1] == 0:
            return False, message_format.format(direction='west')
        return True, (character_position[0], character_position[1] - 1)
    raise Exception("Unknown user choice: " + user_choice)


def get_challenge(board, position):
    """
    Read challenge in current cell on board.

    :param board: a 2-D list
    :param position: the player's current position on the map
    :precondition: parameters must have described expected values
    :postcondition: reads a challenge if there is one at the player's current position
    :return: a challenge if there is one at the position
    """
    challenge = board[position[0]][position[1]]
    board[position[0]][position[1]] = None
    return challenge
