import unittest
import math

# Function to calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Test class for the TSP solution
class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of cities as (x, y)
        self.cities = [
            (3, 26),   # Depot city 0
            (85, 72), (67, 0), (50, 99), (61, 89),
            (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
            (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
            (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
        ]

        # Given tour
        self.tour = [0, 8, 6, 17, 5, 1, 4, 3, 10, 2, 9, 15, 13, 18, 7, 11, 19, 16, 14, 12, 0]
        self.expected_total_cost = 573.20
        self.expected_max_distance = 95.46

    def test_unique_visit(self):
        visited = set(self.tour[:-1])  # Ignore the last city since it's the depot's duplicate for return
        expected = set(range(20))
        self.assertEqual(visited, expected)

    def test_return_to_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_calculate_total_cost(self):
        total_cost = sum(calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
                         for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=2)

    def test_max_distance(self):
        max_distance = max(calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
                           for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(max_distance, self.expected_max_distance, places=2)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    run_tests()