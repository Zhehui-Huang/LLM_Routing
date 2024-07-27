import unittest
from math import sqrt

# Coordinates for each city indexed by city number
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance between cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Proposed solution tour and cost
proposed_tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
proposed_total_cost = 410.03585920085146

class TestTSPSolution(unittest.TestCase):
    def test_tour_validity(self):
        # Test starts and ends at the depot (city 0) and all cities are visited exactly once
        self.assertEqual(proposed_tour[0], 0, "Tour should start at city 0")
        self.assertEqual(proposed_tour[-1], 0, "Tour should end at city 0")
        cities_visited_once = all(proposed_tour.count(city) == 1 for city in set(proposed_tour) - {0})
        self.assertTrue(cities_visited_once, "Each city must be visited exactly once")

    def test_travel_cost(self):
        # Check if the calculated travel cost approximately equals the proposed_total_cost
        calculated_cost = sum(calculate_distance(proposed_tour[i], proposed_tour[i+1]) for i in range(len(proposed_tour) - 1))
        self.assertAlmostEqual(calculated_cost, proposed_total_cost, places=5, msg="Calculated travel cost does not match the expected cost")

if __name__ == "__main__":
    # Load test suite
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_tour_validity'))
    suite.addTest(TestTSPSolution('test_travel_cost'))

    # Execute tests
    runner = unittest.TextTestRunner()
    test_results = runner.run(suite)

    # Checking results
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")