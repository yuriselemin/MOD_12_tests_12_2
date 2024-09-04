from MOD_12_tests_12_2 import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Usain', 10)
        self.andrey = Runner('Andrey', 9)
        self.nick = Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            finishers = list(result.values())
            finisher_names = {i + 1: str(finisher) for i, finisher in enumerate(finishers)}
            print(finisher_names)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        self.all_results[1] = tournament.start()
        self.assertTrue(list(self.all_results[1].values())[-1] == 'Nick')

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        self.all_results[2] = tournament.start()
        self.assertTrue(list(self.all_results[2].values())[-1] == 'Nick')

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        self.all_results[3] = tournament.start()
        self.assertTrue(list(self.all_results[3].values())[-1] == 'Nick')

if __name__ == '__main__':
    unittest.main()