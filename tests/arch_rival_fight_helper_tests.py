from unittest import TestCase
import arch_rival_fight_helper


class TestArchRivalFightHelper(TestCase):

    def test_arc_rival_fight_created(self):
        fight = arch_rival_fight_helper.create_arch_rival_fight()
        self.assertIsNotNone(fight)
        self.assertEqual('arc_rival_fight', fight['type'])

    def test_correct_num_of_tasks_calculated(self):
        self.assertEqual(11, arch_rival_fight_helper.calc_num_of_tasks(20))
        self.assertEqual(7, arch_rival_fight_helper.calc_num_of_tasks(60))
        self.assertEqual(5, arch_rival_fight_helper.calc_num_of_tasks(80))
        self.assertEqual(3, arch_rival_fight_helper.calc_num_of_tasks(110))

