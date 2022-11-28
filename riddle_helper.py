def create_riddles():
    riddle_type = 'riddle'
    riddle_map_symbol = 'R'
    riddles = [
        {'type': riddle_type,
         'map_symbol': riddle_map_symbol,
         'name': 'arch_rival_name',
         'points_acquired': 5,
         'descr': 'What is the name of Batman\'s arch rival?',
         'attempts': 3,
         'answer': 'Joker'},
        {'type': riddle_type,
         'map_symbol': riddle_map_symbol,
         'name': 'transport_name',
         'points_acquired': 4,
         'descr': 'What is the name of Batman\'s most known mean of transportation?',
         'attempts': 3,
         'answer': 'batmobile'},
        {'type': riddle_type,
         'map_symbol': riddle_map_symbol,
         'name': 'sidekick_name',
         'points_acquired': 3,
         'descr': 'What is the name of Batman\'s sidekick?',
         'attempts': 2,
         'answer': 'Robin'}]

    return riddles
