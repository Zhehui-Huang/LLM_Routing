import math
import unittest

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestGTSPSolution(unittest.TestCase):
    def setUp(self):
        self.depot = (35, 40)
        self.cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
                       (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
                       (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]
        self.groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]
        self.proposed_tour = [0, 8, 13, 1, 14, 5, 12, 10, 0]
        self.proposed_cost = 225.43

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.proposed_tour[0], 0)
        self.assertEqual(self.proposed_tour[-1], 0)

    def test_visit_one_from_each_group(self):
        visited = set(self.proposed_tour[1:-1])  # exclude depot
        for group in self.groups:
            self.assertTrue(any(city in group for city in visited))

    def test_euclidean_distance_calculation(self):
        calculated_cost = 0
        for i in range(len(self.proposed_tour) - 1):
            city1 = self.proposed_tour[i]
            city2 = self.proposed_tour[i + 1]
            calculated_cost += calculate_euclidean_distance(*self.cities[city1], *self.cities[city2])
        self.assertAlmostEqual(calculated_cost, self.proposed_cost, places=2)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestGTSPSolution))
    runner = unittest.TextTestRunner()

    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")