import math
import unittest

# Define the cities based on coordinates
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
    8: (49, 29), 9: (13, 17)
}

# Given solution
solution_tour = [0, 8, 5, 2, 1, 9, 0]
solution_cost = 183.85

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Helper function to calculate tour cost
def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i + 1]]
        total_cost += euclidean_distance(city1, city2)
    return total_cost

# Test class to ensure solution correctness
class TestKTSPSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)
    
    def test_visit_six_cities(self):
        # Plus one because city 0 is counted twice (start and end)
        self.assertEqual(len(set(solution_tour)), 6)
    
    def test_cost_calculation(self):
        calculated_cost = calculate_total_travel_cost(solution_tour)
        self.assertAlmostEqual(calculated_cost, solution_cost, places=2)
    
    def test_solution_correctness(self):
        # Run all checks
        if (solution_tour[0] == 0 and solution_tour[-1] == 0) and \
        len(set(solution_tour)) == 6 and \
        abs(calculate_total_travel_cost(solution_tour) - solution_cost) < 1e-2:
            print("CORRECT")
        else:
            print("FAIL")

# Execute the test
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)