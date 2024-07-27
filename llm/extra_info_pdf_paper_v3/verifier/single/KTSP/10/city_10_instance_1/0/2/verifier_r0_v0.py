import unittest
from math import sqrt

# Given tour and total cost from the solution
provided_tour = [0, 3, 4, 5, 8, 0]
provided_cost = 175.37317918852779

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    
    def test_total_cities(self):
        self.assertEqual(len(cities), 10)
    
    def test_depot_city(self):
        self.assertEqual(cities[0], (53, 68))  # Checking depot coordinates
    
    def test_tour_starts_ends_at_depot(self):
        self.assertEqual(provided_tour[0], 0)  # Starts at depot
        self.assertEqual(provided_tour[-1], 0)  # Ends at depot
    
    def test_exactly_five_cities_in_tour(self):
        self.assertEqual(len(set(provided_tour)), 5)  # Including depot city and repeated depot city
    
    def test_correct_travel_cost(self):
        calculated_cost = calculate_total_travel_cost(provided_tour)
        self.assertAlmostEqual(calculatedoutl_cost, provided_cost, places=5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_total_cities'))
    suite.addTest(TestTSPSolution('test_depot_city'))
    suite.addTest(TestTSPSolution('test_tour_starts_ends_at_depot'))
    suite.addTest(TestTSPSolution('test_exactly_five_cities_in_tour'))
    suite.addTest(TestTSPSolution('test_correct_travel_cost'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return "CORRECT" if result.wasSuccessful() else "FAIL"

# Execute the tests
output = run_tests()
print(output)