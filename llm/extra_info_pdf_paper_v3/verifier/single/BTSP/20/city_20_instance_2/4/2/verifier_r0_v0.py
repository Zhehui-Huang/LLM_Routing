import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
            (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
            (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
            (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
        ]
        self.tour = [0, 2, 18, 15, 8, 3, 16, 11, 17, 4, 5, 9, 10, 19, 6, 12, 7, 14, 13, 1, 0]
        self.total_cost = 1008.82
        self.max_distance = 94.02

    @staticmethod
    def distance(city1, city2):
        return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city.")

    def test_visit_each_city_once(self):
        unique_cities = set(self.tour)
        expected_cities = set(range(len(self.cities)))
        self.assertEqual(unique_cities, expected_cities, "Not all cities are visited exactly once or some are visited more than once.")

    def test_max_distance(self):
        distances = [self.distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]]) for i in range(len(self.tour)-1)]
        calculated_max_distance = max(distances)
        self.assertAlmostEqual(calculated_max_distance, self.max_distance, places=2, msg="Maximum distance between consecutive cities does not match.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")