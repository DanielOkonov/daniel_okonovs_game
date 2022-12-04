import board_helper
import character_helper
import riddle_helper
import fight_helper
import arch_rival_fight_helper


def show_choices():
    """
    Print available commands.
    """

    choices = " Valid choices:"
    choices += "\n quit - Q"
    choices += "\n help - H"
    choices += "\n map - M"
    choices += "\n status - T"
    choices += "\n step north - N"
    choices += "\n step east - E"
    choices += "\n step south - S"
    choices += "\n step west - W"
    print(choices)


def game():  # called from main
    """
    Run the game.
    """
    print(open("text/batman-ascii-art.txt", "r").read())
    print(open("text/game-description.txt", "r").read())
    rows = 5
    columns = 5
    board = board_helper.make_board(rows, columns)
    print(board_helper.describe_board(board))
    player_name = input("Enter your player name: ")
    character = character_helper.make_character(player_name)
    print(board_helper.build_board_map(board, character['position'], character['map_symbol']))
    print(character_helper.describe_character(character))
    show_choices()
    # main game circle
    while True:
        user_choice = input("Enter your choice or 'H' for help: ").upper()
        if user_choice == "Q":
            user_choice = input("Are you sure you want to quit? Your progress won't be saved. (Y, N): ").upper()
            if user_choice == 'Y':
                break
            continue
        if user_choice == "H":
            show_choices()
            continue
        if user_choice == "M":
            print(board_helper.build_board_map(board, character['position'], character['map_symbol']))
            print(board_helper.describe_board(board))
            continue
        if user_choice == "T":
            print(character_helper.describe_character(character))
            continue
        if user_choice in ["N", "E", "S", "W"]:
            move_result = board_helper.try_move(board, character['position'], user_choice)
            if not move_result[0]:
                print(move_result[1])
                continue
            new_position = move_result[1]
            character['position'] = new_position
            print(character_helper.describe_character(character))

            challenge = board_helper.get_challenge(board, new_position)
            if challenge is None:
                continue
            challenge_type = challenge['type']
            if challenge_type == 'riddle':
                acquired_points = riddle_helper.execute_challenge(challenge)
                level_changed_message = character_helper.add_points(character, acquired_points)
                if level_changed_message is not None:
                    print(level_changed_message)
                continue
            if challenge_type == 'fight':
                acquired_points = fight_helper.execute_challenge(challenge)
                level_changed_message = character_helper.add_points(character, acquired_points)
                if level_changed_message is not None:
                    print(level_changed_message)
                continue
            if challenge_type == 'arc_rival_fight':
                if arch_rival_fight_helper.execute_fight(challenge, character['points']):
                    print(f'🎉🎉🎉 Congrats {player_name}!!! You won the final challenge and the game! 🎉🎉🎉')
                else:
                    print(f'😢 Condolences {player_name}, you lost the final challenge and the game. 😢')
                break
            raise Exception("Unknown challenge type: " + challenge_type)

        print("not valid choice: " + user_choice)

    # achieved_goal = False
    # while not achieved_goal:
    #             if character_has_leveled():
    #                 execute_glow_up_protocol()
    #         achieved_goal = check_if_goal_attained(board, character)
    # // Print end of game stuff like congratulations or sorry you died


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
