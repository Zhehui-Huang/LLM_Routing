import unittest
from math import sqrt

# Predefined city positions as global constants
CITIES = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestSolution(unittest.TestCase):
    def test_tsp_solution(self):
        tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        expected_total_distance = 337.8447016788252
        expected_max_distance = 60.67124524847005

        # Check Requirement 1: Start and end at depot city 0
        self.assertEqual(tour[0], 0, "Tour should start at city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at city 0")

        # Check Requirement 2: Each city must be visited exactly once apart from depot
        self.assertCountEqual(tour[:-1], list(range(len(CITIES))), "Each city must be visited exactly once")

        # Check if calculated total distance is correctly estimated
        total_travel_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(total_travel_distance, expected_total_distance, places=5, msg="Total travel cost is incorrect.")

        # Check Requirement 3: Check if max distance between any consecutive cities is within expected
        max_distances = [distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)]
        self.assertAlmostEqual(max(max_distances), expected_max_distance, places=5, msg="Maximum distance between consecutive cities is incorrect.")

# Executing the tests
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)