import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (54, 87),
            1: (21, 84),
            2: (69, 84),
            3: (53, 40),
            4: (54, 42),
            5: (36, 30),
            6: (52, 82),
            7: (93, 44),
            8: (21, 78),
            9: (68, 14),
            10: (51, 28),
            11: (44, 79),
            12: (56, 58),
            13: (72, 43),
            14: (6, 99)
        }
        self.tour = [0, 2, 7, 13, 4, 5, 10, 9, 3, 12, 11, 14, 1, 8, 6, 0]
        self.reported_cost = 339.03

    def test_visit_all_cities_once(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), len(self.cities), "Some cities are visited more than once or missed.")

    def test_start_end_depot(self):
        self.assertEqual(self.tour[0], self.tour[-1], "The tour does not start and end at the depot city.")

    def test_total_cost_calculation(self):
        def euclidean_distance(city1, city2):
            x1, y1 = city1
            x2, y2 = city2
            return sqrt((x2 - x1)**2 + (y2 - y1)**2)

        total_cost = 0
        for i in range(len(self.tour) - 1):
            city1, city2 = self.tour[i], self.tour[i+1]
            total_cost += euclidean_distance(self.cities[city1], self.cities[city2])
        
        # Allow a small margin for floating point arithmetic issues
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2, msg="Calculated cost does not match the reported cost.")

    def test_total_cities_count(self):
        self.assertEqual(len(self.cities), 15, "The total count of cities including the depot should be 15.")

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")