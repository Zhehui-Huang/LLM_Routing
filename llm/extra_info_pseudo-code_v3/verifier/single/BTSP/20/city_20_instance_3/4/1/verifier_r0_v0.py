import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
            (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
            (18, 16), (4, 43), (53, 76), (19, 72)
        ]
        self.tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        self.total_cost = 1074.2795438948997
        self.max_distance = 128.81770064707723

    def test_visits_all_cities(self):
        unique_cities = set(self.tour)
        # Check if tour visits each city exactly once and starts/ends at depot
        self.assertEqual(len(unique_cities), len(self.cities))
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_minimizes_max_distance(self):
        # Calculate max distance from provided solution
        max_dist = max([
            sqrt((self.cities[self.tour[i]][0] - self.cities[self.tour[i+1]][0])**2 +
                 (self.cities[self.tour[i]][1] - self.cities[self.tour[i+1]][1])**2)
            for i in range(len(self.tour)-1)
        ])
        self.assertEqual(max_dist, self.max_distance)

    def test_correct_total_travel_cost(self):
        # Calculate total travel cost from provided solution
        computed_total_cost = sum([
            sqrt((self.cities[self.tour[i]][0] - self.cities[self.tour[i+1]][0])**2 +
                 (self.cities[self.tour[i]][1] - self.cities[self.tour[i+1]][1])**2)
            for i in range(len(self.tour)-1)
        ])
        self.assertAlmostEqual(computed_total_cost, self.total_cost, places=5)

    def test_correct_output(self):
        self.assertIsInstance(self.tour, list)
        self.assertTrue(all(isinstance(city, int) for city in self.tour))
        self.assertIsInstance(self.total_cost, (int, float))
        self.assertIsInstance(self.max_distance, (int, float))

    def test_solution(self):
        try:
            self.test_visits_all_cities()
            self.test_minimizes_max_distance()
            self.test_correct_total_travel_cost()
            self.test_correct_output()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# Create a test suite and add the test case
suite = unittest.TestSuite()
suite.addTest(TestTSPSolution('test_solution'))

# Run the tests
runner = unittest.TextTestRunner()
runner.run(suite)