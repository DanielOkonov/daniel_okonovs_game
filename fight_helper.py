import datetime


def create_fights():
    """
    Create fight scenarios that will fill up map.

    :return: a list of dictionaries with different fight scenarios.
    """
    fight_type = 'fight'
    fights = [
        {'type': fight_type,
         'map_symbol': '🎭',
         'name': 'two_face',
         'points_acquired': 20,
         'points_lost': 10,
         'tasks': [('strike', 3, 1,
                    'You knock out one of Twoface\'s teeth and he yells in agony!',
                    'You swung and missed! Twoface knees you in the stomach.'),
                   ('duck', 4, 2,
                    'Twoface missed a hit on you and lost his balance!',
                    'You did not duck fast enough! Twoface uppercuts you and knocks you off your feet.')],
         'num_of_tasks_to_win': 1,
         'descr': 'Two face has captured both of Jim Gordon\'s children and is holding them hostage!'
                  'You must fight Two Face in order to save Jim\'s children!'},
        {'type': fight_type,
         'map_symbol': '👊',
         'name': 'street_thugs',
         'points_acquired': 25,
         'points_lost': 15,
         'tasks': [('hit', 3, 1,
                    'You knocked 4 of the thugs!',
                    'You missed a hit on one of the thugs! He pushes you off and laughs.'),
                   ('block', 2, 1,
                    'You blocked a bat swing from a thug.',
                    'You miss a block and get hit with a bat! Your vision goes blurry as you fall to '
                    'your knees.')],
         'num_of_tasks_to_win': 2,
         'descr': 'A group of thugs are harassing and attempting to rob a family in an alley way, there\'s'
                  'five of them and three of them are armed with baseball bats. This family needs your help!'},
        {'type': fight_type,
         'map_symbol': '👊',
         'name': 'bane',
         'points_acquired': 25,
         'points_lost': 15,
         'tasks': [('hit', 3, 1,
                    'You strike a fatal blow and mess up the tubing in Bane\'s mask!',
                    'Bane dodges the strike, punches you in the face and breaks your nose!'),
                   ('block', 2, 1,
                    'Bane throws a terrifyingly quick right hook that you efficiently block!',
                    'You don\'t block Bane\'s kick in time and take a bad hit to the head.')],
         'num_of_tasks_to_win': 2,
         'descr': 'Bane has broken into a bank and is holding everyone hostage! Bane is threatening to kill'
                  'everyone unless he is given all of the money. Defeat Bane and save the people!'}]

    return fights


def execute_challenge(fight):
    """
    Print fight description and results.

    :param fight: one of the fights from the create_fights function
    :precondition: fight passed must have all attributes
    :postcondition: prints description of fight and results
    :return: points lost if fight lost, points gained if fight won
    """
    symbol = fight['map_symbol'] + ' '
    print(symbol + 'You engage in fight with: ' + fight['name'])
    print(symbol + fight['descr'])
    tasks_to_win = fight['num_of_tasks_to_win']
    print(symbol +
          "You will have to succeed in {to_win} fight tasks out of {total}"
          .format(to_win=tasks_to_win, total=len(fight['tasks'])))
    num_of_succeeded = 0
    task_num = 0
    for task in fight['tasks']:
        task_num += 1
        if execute_time_lapse_task(task, task_num, symbol):
            num_of_succeeded += 1

    print(symbol + "You succeeded in {num_of_succeeded} out of {total} tasks"
          .format(num_of_succeeded=num_of_succeeded, total=len(fight['tasks'])))
    if num_of_succeeded < tasks_to_win:
        print(symbol + "You lost the fight, lost {points} points".format(points=fight['points_lost']))
        return -fight['points_lost']
    print(symbol + "You won the fight, acquired {points} points".format(points=fight['points_acquired']))
    return fight['points_acquired']


def execute_time_lapse_task(task, task_num, symbol):
    """
    Determine if task was accomplished in given time frame.

    :param task: a fight task from one of the fights
    :param task_num: number of the task based on the index of the task in the tuple
    :param symbol: map symbol of the fight
    :precondition: must contain all fight attributes mentioned in the parameters
    :postcondition: determines whether task was accomplished in given time frame or not
    :return: a boolean, True for win or False for lost
    """
    task_prefix = 'task_' + str(task_num) + ': '
    task_verb = task[0]
    period = task[1]
    tolerance = task[2]
    task_succeeded_message = task[3]
    task_failed_message = task[4]
    print(symbol + task_prefix + "--------")
    print(symbol + task_prefix +
          "You have to {task_verb} 2 times {period} seconds apart with {tolerance} seconds precision"
          .format(task_verb=task_verb, period=period, tolerance=tolerance))
    input(symbol + task_prefix + "Hit Enter for the first {task_verb}".format(task_verb=task_verb))
    time_1 = datetime.datetime.now()
    input(symbol + task_prefix + "Hit Enter for the second {task_verb} in {period} seconds"
          .format(task_verb=task_verb, period=period))
    time_2 = datetime.datetime.now()
    elapsed = (time_2 - time_1).total_seconds()
    print(symbol + task_prefix + "You {task_verb} {elapsed} seconds apart"
          .format(task_verb=task_verb, elapsed=elapsed))
    delta = abs(elapsed - period)
    if delta < tolerance:
        print(f'{symbol + task_prefix}You succeeded in the task {str(task_num)}. {task_succeeded_message}')
        return True

    print(f'{symbol + task_prefix}You failed in the task {str(task_num)}. {task_failed_message}')
    return False
