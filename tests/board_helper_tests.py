from unittest import TestCase
import board_helper


class TestBoardHelper(TestCase):

    def test_correct_board_created(self):
        test_num_of_rows = 6
        test_num_of_columns = 7

        board = board_helper.make_board(test_num_of_rows, test_num_of_columns)
        self.assertEqual(test_num_of_rows, len(board))
        self.assertEqual(test_num_of_columns, len(board[0]))

    def test_get_all_cells_returns_expected(self):
        self.assertEqual([11, 12, 21, 22], board_helper.get_all_cells([[11, 12], [21, 22]]))

    def test_describe_board_contains_expected_string(self):
        description = board_helper.describe_board(board_helper.make_board(7, 8))
        expected_string = "Gotham City has 7 Avenues and 8 Streets."
        self.assertTrue(expected_string in description)

    def test_can_move_within_limits(self):
        test_num_of_rows = 10
        test_num_of_columns = 10

        board = board_helper.make_board(test_num_of_rows, test_num_of_columns)
        move_result = board_helper.try_move(board, (0, 0), "S")
        self.assertTrue(move_result[0])

    def test_cannot_move_beyond_limits(self):
        test_num_of_rows = 10
        test_num_of_columns = 10

        board = board_helper.make_board(test_num_of_rows, test_num_of_columns)
        move_result = board_helper.try_move(board, (9, 9), "S")
        self.assertFalse(move_result[0])

    def test_get_challenge_returned_expected_and_removed(self):
        board = [[None, 'test_challenge'], [None, None]]
        challenge = board_helper.get_challenge(board, (0, 1))
        self.assertEqual('test_challenge', challenge)
        self.assertIsNone(board[0][1])
