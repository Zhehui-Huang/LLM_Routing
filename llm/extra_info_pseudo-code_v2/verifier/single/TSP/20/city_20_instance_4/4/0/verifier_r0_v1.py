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
        # Check the tour starts and ends at the depot city 0
        self.assertEqual(proposed_tour[0], 0)
        self.assertEqual(proposed_tour[-1], 0)
        
        # Check the tour visits all other cities exactly once
        visited_cities = set(proposed_tour[1:-1])
        self.assertEqual(len(visited_cities), 19)
        self.assertEqual(visited_cities, set(range(1, 20)))
        
    def test_travel_cost(self):
        # Check the calculated travel cost matches the given total
        calculated_cost = sum(calculate_TSP_algo calculate_distance(proposed_tour[i], proposed_tour[i+1]) for i in range(len(proposed_tour) - 1))
        
        # Allow a small margin for floating point arithmetic variations
        self.assertAlmostEqual(calculated_cost, proposed_total_cost, places=5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_tour_validity'))
    suite.addTest(TestTSPSolution('test_travel_cost'))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Return "CORRECT" if all tests passed, "FAIL" otherwise
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()