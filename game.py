import board_helper


def game():  # called from main
    print(open("text/batman-ascii-art.txt", "r").read())
    print(open("text/game-description.txt", "r").read())
    rows = 3
    columns = 5
    board = board_helper.make_board(rows, columns)
    print(board_helper.describe_board(board))
    print(board_helper.build_board_map(board))
    # character = make_character("Player name")
    # achieved_goal = False
    # while not achieved_goal:
    #     // Tell the user where they are
    #     describe_current_location(board, character)
    #     direction = get_user_choice( )
    #     valid_move = validate_move(board, character, direction)
    #     if valid_move:
    #         move_character(character)
    #         describe_current_location(board, character)
    #         there_is_a_challenge = check_for_challenges()
    #         if there_is_a_challenge:
    #             execute_challenge_protocol(character)
    #             if character_has_leveled():
    #                 execute_glow_up_protocol()
    #         achieved_goal = check_if_goal_attained(board, character)
    #     else:
    # // Tell the user they can’t go in that direction
    # // Print end of game stuff like congratulations or sorry you died


def main():
    game()


if __name__ == "__main__":
    main()
