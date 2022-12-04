import math
import datetime
from random import randrange


def create_arch_rival_fight():
    fight_type = 'arc_rival_fight'
    fight_map_symbol = '🤡'
    return {'type': fight_type,
            'map_symbol': fight_map_symbol,
            'word_timer_tasks': [
                ('hit', 3, 8),
                ('strike', 2, 8),
                ('batman', 2, 7),
                ('hostage', 2, 9)
            ]
            }


def execute_fight(fight, character_points):
    symbol = fight['map_symbol'] + ' '
    print(f"{symbol}You came to final challenge having {character_points} points.")
    num_of_tasks = calc_num_of_tasks(character_points)
    print(f"{symbol}Based on your level you will be challenged with {num_of_tasks} tasks.")
    print(f"{symbol}You need to succeed in at least {num_of_tasks - 1} tasks to win the fight and the game.")
    tasks = fight['word_timer_tasks']

    failed_once = False
    for task_num in range(num_of_tasks):
        random_task_id = randrange(len(tasks))
        if not execute_word_timer_tasks(tasks[random_task_id], task_num + 1, symbol):
            if failed_once:
                return False
            failed_once = True

    return True


def execute_word_timer_tasks(word_timer_task, task_num, symbol):
    word = word_timer_task[0]
    num_of_times = word_timer_task[1]
    seconds_limit = word_timer_task[2]
    task_prefix = symbol + 'task_' + str(task_num) + ': '
    print(f"{task_prefix} ------")
    print(f"{task_prefix}You will have to type a word multiple times separated by space.")
    input(f"{task_prefix}Hit enter to see the word and number of times to type it.")
    time_1 = datetime.datetime.now()
    string_from_user = \
        input(f"{task_prefix}Type word '{word}' {num_of_times} times in less than {seconds_limit} seconds: ")
    time_2 = datetime.datetime.now()
    elapsed = (time_2 - time_1).total_seconds()
    expected_string = ((word + ' ') * num_of_times).rstrip()
    if string_from_user != expected_string:
        print(f"{task_prefix}You failed: string is not as expected.")
        print(f"{task_prefix}Expected: '{expected_string}', actually printed: '{string_from_user}'.")
        return False
    if elapsed > seconds_limit:
        print(f"{task_prefix}You failed: took longer than the limit of {seconds_limit} seconds: actually {elapsed}.")
        return False

    print(f"{task_prefix}You succeeded!")
    return True


def calc_num_of_tasks(points):
    num_of_tasks = 3
    if points >= 100:
        return num_of_tasks
    if points < 0:
        return num_of_tasks + 10

    return num_of_tasks + math.floor((100 - points) / 10)
