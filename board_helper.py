import random

import riddle_helper
import fight_helper


def make_board(rows, columns):
    board = []
    for row in range(rows):
        board.append([None] * columns)

    riddles = riddle_helper.create_riddles()
    fights = fight_helper.create_fights()
    all_challenges = []
    for riddle in riddles:
        all_challenges.append(riddle)
    for fight in fights:
        all_challenges.append(fight)

    # starting from 1 cause at cell 0 there is a hero
    random_cells_for_challenges = random.sample(range(1, rows * columns), len(all_challenges))

    cell_id = 0
    challenge_id = 0
    for row in range(rows):
        for column in range(columns):
            if cell_id in random_cells_for_challenges:
                board[row][column] = all_challenges[challenge_id]
                challenge_id += 1
            cell_id += 1

    return board


def describe_board(board):
    return f'Gotham City has {len(board)} Avenues and {len(board[0])} Streets.'


def build_board_map(board):
    chars_per_cell = 6
    row_separator = '\n' + '-' * len(board[0]) * chars_per_cell + '\n'
    map = ''
    map += row_separator

    for row in range(len(board)):
        for column in range(len(board[0])):
            map += '|  '
            a_thing = board[row][column]
            if a_thing is not None:
                map += a_thing['map_symbol']
            else:
                map += '.'
            map += '  '
        map += '|'
        map += row_separator

    return map
