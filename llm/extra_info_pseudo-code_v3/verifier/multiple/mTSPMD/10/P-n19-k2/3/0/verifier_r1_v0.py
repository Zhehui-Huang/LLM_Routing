import unittest
from math import sqrt

# Defining the cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Tours provided in the solution
solution = {
    "Robot 0": [0, 6, 2, 7, 5, 9, 8, 3, 4, 0],
    "Robot 1": [1, 10, 12, 14, 11, 16, 17, 15, 13, 18, 1]
}

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Unit tests to verify the solution
class TestTSPSolution(unittest.TestCase):
    def test_start_end_depot(self):
        self.assertEqual(solution["Robot 0"][0], 0)
        self.assertEqual(solution["Robot 0"][-1], 0)
        self.assertEqual(solution["Robot 1"][0], 1)
        self.assertEqual(solution["Robot 1"][-1], 1)

    def test_visit_all_cities_once(self):
        all_cities_visited = sorted(solution["Robot 0"][1:-1] + solution["Robot 1"][1:-1])
        expected_cities = list(range(2, 19))
        self.assertEqual(all_cities_visited, expected_cities)

    def test_total_travel_cost(self):
        total_cost = 0
        for robot, tour in solution.items():
            for i in range(len(tour) - 1):
                total_cost += calculate_distance(tour[i], tour[i + 1])
        expected_total_cost = 263.82
        self.assertAlmostEqual(total_cost, expected_total_cost, places=2)

# Main function to run the tests
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")