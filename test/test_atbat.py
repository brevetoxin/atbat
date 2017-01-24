import unittest
import atbat

class Log5Test(unittest.TestCase):
    def test_bad_batter_probability(self):
        self.assertRaises(ValueError, atbat.log5,-1,0.3,0.4)
    def test_bad_pitcher_probability(self):
        self.assertRaises(ValueError, atbat.log5,0.3,-1,0.4)
    def test_bad_league_probability(self):
        self.assertRaises(ValueError, atbat.log5,0.3,0.4,-1)
    def test_zero_batter(self):
        self.assertEqual(atbat.log5(0, 0.175, 0.222), 0)
    def test_zero_pitcher(self):
        self.assertEqual(atbat.log5(0.333, 0, 0.222), 0)
    def test_zero_league(self):
        self.assertRaises(ValueError, atbat.log5,0.333, 0.175, 0)
    def test_appropriate_calculations(self):
        self.assertEqual(round(atbat.log5(0.333, 0.175, 0.222), 10), 0.2706759443)

class moreyZTest(unittest.TestCase):
    def test_bad_batter_probability(self):
        self.assertRaises(ValueError, atbat.moreyZ,-1,0.3,0.4)
    def test_bad_pitcher_probability(self):
        self.assertRaises(ValueError, atbat.moreyZ,0.3,-1,0.4)
    def test_bad_league_probability(self):
        self.assertRaises(ValueError, atbat.moreyZ,0.3,0.4,-1)
    def test_zero_batter(self):
        self.assertEqual(round(atbat.moreyZ(0, 0.175, 0.222), 11), 0.03178827586)
    def test_zero_pitcher(self):
        self.assertEqual(round(atbat.moreyZ(0.333, 0, 0.222), 10), 0.1435111473)
    def test_zero_league(self):
        self.assertRaises(ValueError, atbat.moreyZ,0.333, 0.175, 0)
    def test_appropriate_calculations(self):
        self.assertEqual(round(atbat.moreyZ(0.333, 0.175, 0.222), 10), 0.267254834)


if __name__ == '__main__':
    unittest.main()
