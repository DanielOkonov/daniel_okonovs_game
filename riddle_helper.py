def create_riddles():
    """
    Create riddle scenarios that will fill up map.

    :return: a list of dictionaries with different riddles
    """

    riddle_type = 'riddle'
    riddle_map_symbol = '？'
    riddles = [
        {'type': riddle_type,
         'map_symbol': riddle_map_symbol,
         'name': 'riddle_1',
         'points_acquired': 15,
         'question': 'What is always on its way here, but never arrives?',
         'choices': {1: 'Death', 2: 'Love', 3: 'Tomorrow'},
         'answer': 3},
        {'type': riddle_type,
         'map_symbol': riddle_map_symbol,
         'name': 'riddle_2',
         'points_acquired': 20,
         'question': 'If you are justice, please do not lie. What is the price for your blind eye?',
         'choices': {1: 'A joke', 2: 'A bribe'},
         'answer': 2},
        {'type': riddle_type,
         'map_symbol': riddle_map_symbol,
         'name': 'riddle_3',
         'points_acquired': 25,
         'question': 'What does a liar do when he\'s dead?',
         'choices': {1: 'He lies still', 2: 'Nothing', 3: 'He rots'},
         'answer': 1}]

    return riddles


def execute_challenge(riddle):
    """
    Print riddle and result.

    :param riddle: one of the riddles from the create_riddles function
    :precondition: riddle passed must have all attributes
    :postcondition: prints the riddle and result of chosen answer
    :return: points lost if incorrect riddle answer, points gained if correct riddle answer
    """

    symbol = riddle['map_symbol'] + ' '
    print(symbol + 'riddle: ' + riddle['name'])
    print(symbol + riddle['question'])
    print(symbol + 'choices:')
    for key, value in riddle['choices'].items():
        print(f'{symbol}  {key} - {value}')
    choice = input(symbol + "Enter your choice: ")
    if int(choice) == riddle['answer']:
        print(symbol + 'Congrats! The answer is correct')
        print(symbol + 'You acquired {points} points'.format(points=riddle['points_acquired']))
        return riddle['points_acquired']

    print(symbol + 'Answer is not correct')
    return 0
