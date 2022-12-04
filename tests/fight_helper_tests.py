from unittest import TestCase
import fight_helper


class TestFightHelper(TestCase):

    def test_correct_challenge_type_created(self):
        challenges = fight_helper.create_fights()
        self.assertTrue(len(challenges) > 0)
        self.assertEqual('fight', challenges[0]['type'])

