import unittest
from math import sqrt

# Provided tour and travel cost
tour = [0, 6, 8, 9, 7, 5, 1, 4, 0]
travel_cost_provided = 312.36

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(tour[i], tour[i+1])
    return total_cost

class TestSampleSolution(unittest.TestCase):
    def test_route_initial_final_city(self):
        # The tour should start and end at city 0
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        
    def test_tour_length(self):
        # The robot is required to visit exactly 8 cities including the start
        self.assertEqual(len(set(tour)), 9)  # unique cities count (set) should count depot twice since it's visited twice
    
    def test_calculate_travel_cost(self):
        # Verify the travel cost is calculated correct with Euclidean distance
        calculated_cost = calculate_total_travel_cost(tour)
        self.assertAlmostEqual(calculated_listed_cost, travel_cost_provided, places=2)

# Run the tests
suite = unittest.TestSuite()
test_loader = unittest.TestLoader()
suite.addTests(test_loader.loadTestsFromTestCase(TestSampleSolution))

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Check if all tests passed
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")