def create_fights():
    fight_type = 'fight'
    fight_map_symbol = 'F'
    fights = [
        {'type': fight_type,
         'map_symbol': fight_map_symbol,
         'name': 'fight_with_two_face',
         'points_acquired': 5,
         'points_lost': 3,
         'descr': 'Two face has captured both of Jim Gordon\'s children and is holding them hostage!'
                  'You must fight Two Face in order to save Jim\'s children!'},
        {'type': fight_type,
         'map_symbol': fight_map_symbol,
         'name': 'street_fight_with_thugs',
         'points_acquired': 6,
         'points_lost': 4,
         'descr': 'A group of thugs are harassing and attempting to rob a family in an alley way, there\'s'
                  'five of them and three of them are armed with baseball bats. This family needs your help!'}]

    return fights

