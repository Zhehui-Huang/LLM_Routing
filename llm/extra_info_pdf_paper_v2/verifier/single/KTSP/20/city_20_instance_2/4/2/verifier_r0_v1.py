import unittest
import math

# Define the cities with coordinates, including the depot
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

# The given tour and its total cost
tour = [0, 12, 14, 16, 11, 7, 18, 15, 13, 19, 0]
given_total_cost = 190.66  # From the problem statement

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def calculate_total_tour_cost(tour):
    return round(sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)), 2)

class TourTest(unittest.TestCase):
    def test_tour_validity(self):
        # Starting and ending at the depot city
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Test that exactly 10 cities are visited
        self.assertEqual(len(set(tour)), 10)

        # Check travel cost calculation
        calculated_cost = calculate_total_tour_cost(tour)
        self.assertAlmostEqual(calculated_cost, given_total_cost, places=2)

# Running the test
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TourTest))

runner = unittest.TextTestRunner()
result = runner.run(suite)

if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")