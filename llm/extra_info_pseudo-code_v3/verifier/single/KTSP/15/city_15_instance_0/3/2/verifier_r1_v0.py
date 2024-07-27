import unittest
from math import sqrt

# Define the cities' coordinates
cities = {
    0: (9, 93),
    12: (3, 21),
    11: (11, 40),
    8: (19, 76)
}

# Given solution and its total travel cost
solution_tour = [0, 12, 11, 8, 0]
reported_cost = 149.46635635332964

def calculate_euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_tour_start_and_end_at_depot(self):
        """ Test that the tour starts and ends at the depot city """
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_tour_length_includes_exactly_four_cities(self):
        """ Test the tour includes exactly 4 cities, depot included """
        self.assertEqual(len(solution_tour), 5)  # Includes return to depot

    def test_tour_cost_minimization(self):
        """ Test the total travel cost is calculated correctly and is near the reported cost """
        calculated_cost = calculate_total_travel_cost(solution_tour)
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5)

    def test_output_format(self):
        """ Test output format is correct, starting and ending with depot city """
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)
        self.assertIsInstance(reported_cost, float)

# Note: Requirement about the use of GVNS cannot be precisely tested without the algorithm code provided.

if __name__ == '__main__':
    # Run the tests
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    # Check overall test results
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")