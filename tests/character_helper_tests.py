from unittest import TestCase
import character_helper


class TestCharacterHelper(TestCase):

    def test_make_character_correct_name(self):
        character = character_helper.make_character('test_name')
        self.assertIsNotNone(character)
        self.assertTrue('test_name' in character['name'])

    def test_describe_character_correct_name(self):
        character = character_helper.make_character('test_name')
        description = character_helper.describe_character(character)
        self.assertTrue('You are test_name' in description)

    def test_add_points_added_correct(self):
        character = character_helper.make_character('test_name')
        character['points'] = 0
        character_helper.add_points(character, 10)
        self.assertEqual(10, character['points'])

    def test_get_level_correct_level_returned(self):
        self.assertEqual(1, character_helper.get_level(40))
        self.assertEqual(2, character_helper.get_level(60))
        self.assertEqual(3, character_helper.get_level(90))
        self.assertEqual(4, character_helper.get_level(110))
