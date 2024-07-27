import unittest
import math

# Provided city positions indexed accordingly
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

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# The provided tour and expected cost
provided_tour = [0, 12, 2, 9, 13, 18, 15, 5, 1, 17, 4, 3, 10, 8, 6, 14, 7, 11, 16, 19, 0]
provided_total_cost = 458.64455578878136

class TestTSPSolution(unittest.TestCase):
    def test_start_and_end_at_depot(self):
      self.assertEqual(provided_tour[0], 0, "Does not start at depot")
      self.assertEqual(provided_tour[-1], 0, "Does not end at depot")

    def test_visit_all_cities_once(self):
        # Check if all cities, except depot, are visited exactly once
        cities_visited = provided_tour[1:-1]
        unique_cities = set(cities_visited)
        self.assertEqual(len(cities_visited), len(unique_cities), "Some cities are visited more than once")
        self.assertEqual(len(unique_cities), 19, "Not all cities are visited")

    def test_correct_cost_calculation(self):
        # Calculate the total travel cost from the provided tour and compare with the expected cost
        calculated_cost = sum(calculate_distance(provided_tour[i], provided_tour[i+1]) for i in range(len(provided_tour) - 1))
        self.assertAlmostEqual(calculated_cost, provided_total_cost, places=5, msg="Calculated cost does not match the provided cost")
        
unittest_suite = unittest.TestSuite()
unittest_suite.addTest(unittest.makeSuite(TestTSPSolution))
unittest_text_runner = unittest.TextTestRunner().run(unittest_suite)

if unittest_text_runner.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")