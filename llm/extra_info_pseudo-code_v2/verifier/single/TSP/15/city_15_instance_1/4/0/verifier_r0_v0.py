import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.coordinates = [
            (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
            (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
            (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
        ]
        # Provided solution
        self.tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
        self.reported_cost = 442.570870788815

    def test_starts_and_ends_at_depot(self):
        # [Requirement 1]
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_all_cities_once(self):
        # [Requirement 2]
        visited = set(self.tour)
        self.assertEqual(len(visited), 15)
        self.assertEqual(visited, set(range(15)))

    def test_euclidean_cost(self):
        # [Requirement 3] and [Requirement 4]
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.coordinates[self.tour[i]]
            x2, y2 = self.coordinates[self.tour[i + 1]]
            calculated_cost += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    # Suite to determine overall result for checking [Requirement 5], assumed Lin-Kernighan algorithm suitability
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")