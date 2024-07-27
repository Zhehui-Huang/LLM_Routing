import unittest
from math import sqrt

# The provided cities coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

expected_tour = [0, 5, 1, 17, 4, 3, 10, 8, 6, 14, 16, 19, 11, 7, 18, 13, 15, 2, 9, 12, 0]
expected_cost = 467.24450086107504

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to calculate the total cost of the tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_tour_start_end(self):
        # Requirement 1
        self.assertEqual(expected_tour[0], 0)
        self.assertEqual(expected_tour[-1], 0)

    def test_visit_all_once(self):
        # Requirement 2
        unique_cities = set(expected_tour[1:-1])  # Ignore the depot city in the beginning and end
        self.assertEqual(len(unique_cities), 19)

    def test_tour_cost(self):
        # Requirement 3 & 5
        calculated_cost = calculate_total_cost(expected_tour)
        self.assertAlmostEqual(calculated_cost, expected_cost, places=5)
        
    def test_output_format(self):
        # Requirement 4
        self.assertIsInstance(expected_tour, list)
        self.assertIsInstance(expected_cost, float)

# Run the tests
suite = unittest.TestSuite()
test_loader = unittest.TestLoader()
suite.addTests(test_loader.loadTestsFromTestCase(TestTSPSolution))

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Output based on test results
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")