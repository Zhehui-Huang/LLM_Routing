import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
            5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
            10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
            15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
        }
        self.tour = [0, 4, 1, 8, 16, 17, 5, 19, 6, 2, 10, 3, 18, 14, 11, 9, 12, 7, 13, 15, 0]
        self.reported_cost = 349.1974047195548

    def test_unique_cities(self):
        unique_cities = set(self.tour[:-1])  # exclude final return to the depot
        self.assertEqual(len(unique_cities), 20)

    def test_route_starts_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_travel_cost(self):
        calculated_cost = sum(self.calculate_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5)

    def test_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.reported_cost, float)
        self.assertTrue(all(isinstance(city, int) for city in self.tour))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    # Determine if the solution is CORRECT based on test results:
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")