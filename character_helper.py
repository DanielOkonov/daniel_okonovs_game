
# import collections
# collections.Callable = collections.abc.Callable
def make_character(character_name):
    """
    Create the playable character.

    :param character_name: the user's inputted name
    :precondition: character_name must be a string
    :postcondition: creates a character with given info
    :return: a dictionary with the character's info
    """
    return {'type': 'player',
            'map_symbol': '🦇',
            'name': character_name + ' as Batman',
            'points': 50,
            'position': (0, 0)}


def describe_character(character):
    """
    Describe character status with strings.

    :param character: the player's chosen name as a string
    :precondition: character must be a string
    :postcondition: describes character's status
    :return: a description of the character's status using strings
    """

    description = f"You are {character['name']}"
    description += "\nYou are currently at the corner of Avenue {row}".format(row=character['position'][0] + 1)
    description += " and Street {column}".format(column=character['position'][1] + 1)
    description += "\nYou have {points} points, are at level {level}" \
        .format(points=character['points'], level=get_level(character['points']))

    return description


def add_points(character, points):
    """
    Display whether player leveled up or leveled down or neither and increment or decrement total points.

    :param character: the player's chosen name as a string
    :param points: an integer
    :precondition: character must be a string and points must be a positive integer
    :postcondtion: displays player's level status and calculated new total points
    :return: player's level status
    """

    cur_level = get_level(character['points'])
    character['points'] += points
    new_level = get_level(character['points'])
    if new_level > cur_level:
        return "Congrats! You leveled up. New level: {level}".format(level=new_level)
    if new_level < cur_level:
        return "You leveled down. New level: {level}".format(level=new_level)

    return None


def get_level(points):
    """
    Determine the player's current level.

    :param points: player's total amount of points as an integer
    :precondition: must be a positive integer
    :return: player's current level as an integer

    >>> print(get_level(60))
    2
    """
    if points <= 50:
        return 1
    if points <= 70:
        return 2
    if points <= 100:
        return 3
    return 4
