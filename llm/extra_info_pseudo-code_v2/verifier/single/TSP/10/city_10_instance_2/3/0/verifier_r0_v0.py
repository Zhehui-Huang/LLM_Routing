import unittest
import math

# The input data:
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# The provided solution:
tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
reported_total_cost = 354.91

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

class TestTSPSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
    
    def test_all_cities_visited_once(self):
        unique_cities = set(tour)
        self.assertEqual(len(unique_cities), len(cities))  # Includes depot city, visited twice
        
    def test_correct_calculation_of_tour_cost(self):
        calculated_cost = calculate_total_tour_cost(tour)
        self.assertAlmostEqual(calculated_cost, reported_total_cost, places=2)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()