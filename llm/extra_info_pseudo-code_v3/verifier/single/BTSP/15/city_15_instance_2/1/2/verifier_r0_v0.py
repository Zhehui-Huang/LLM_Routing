import unittest
from math import sqrt

# Provided cities data
cities = {
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

# Solution provided
solution_tour = [0, 6, 1, 14, 8, 11, 2, 12, 4, 3, 5, 10, 9, 13, 7, 0]
reported_total_cost = 344.64
reported_max_distance = 58.05

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTSPSolution(unittest.TestCase):
    def test_starts_and_ends_at_depot(self):
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_visits_each_city_exactly_once(self):
        # Each city except the depot should appear exactly once
        tour_cities = sorted(solution_tour[1:-1])
        expected_cities = list(range(1, 15))
        self.assertListEqual(tour_cities, expected_cities)

    def test_output_tour_format(self):
        self.assertEqual(solution_tour[0], solution_tour[-1]) # Starts and ends at depot
        self.assertGreaterEqual(len(solution_tour), 2) # At least two elements (start and end at the depot)

    def test_output_total_travel_cost(self):
        calculated_cost = sum(calculate_distance(solution_tour[i], solution_tour[i + 1]) for i in range(len(solution_tour) - 1))
        self.assertAlmostEqual(calculated_cost, reported_total_cost, places=2)

    def test_output_max_distance(self):
        calculated_max_distance = max(calculate_distance(solution_tour[i], solution_tour[i + 1]) for i in range(len(solution_tour) - 1))
        self.assertAlmostEqual(calculated_max_distance, reported_max_distance, places=2)

# Running the test
if __name__ == '__main__':
    test_case = TestTSPSolution()
    
    # Running testsuite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # The final result
    print("CORRECT" if result.wasSuccessful() else "FAIL")