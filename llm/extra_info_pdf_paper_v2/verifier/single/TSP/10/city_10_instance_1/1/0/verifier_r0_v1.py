import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 5, 3, 8, 4, 6, 1, 7, 2, 9, 0]
        self.cost = 297.4869430225416
        self.cities = {
            0: (53, 68),
            1: (75, 11),
            2: (91, 95),
            3: (22, 80),
            4: (18, 63),
            5: (54, 91),
            6: (70, 14),
            7: (97, 44),
            8: (17, 69),
            9: (95, 89)
        }

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_all_cities_once(self):
        self.assertEqual(len(set(self.tour[1:-1])), 9)

    def test_correct_euclidean_distance(self):
        total_distance_calculated = 0
        for i in range(len(self.tour) - 1):
            city1, city2 = self.tour[i], self.tour[i + 1]
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            total_distance_calculated += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(self.cost, total_distance_calculated, places=5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Running the test suite
test_result = run_tests()
print(test_result)