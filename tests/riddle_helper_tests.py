from unittest import TestCase
import riddle_helper


class TestRiddleHelper(TestCase):

    def test_correct_challenge_type_created(self):
        challenges = riddle_helper.create_riddles()
        self.assertTrue(len(challenges) > 0)
        self.assertEqual('riddle', challenges[0]['type'])

