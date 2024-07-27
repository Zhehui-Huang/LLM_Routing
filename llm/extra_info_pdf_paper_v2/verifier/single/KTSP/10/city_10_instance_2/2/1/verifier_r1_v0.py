import math
import unittest

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 
            4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56), 
            8: (49, 29), 9: (13, 17)
        }
        self.solution_tour = [0, 8, 5, 2, 1, 9, 0]
        self.solution_cost = 183.85
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
    
    def test_tour_includes_six_cities(self):
        self.assertEqual(len(set(self.solution_tour)), 6)
    
    def test_travel_cost_calculation(self):
        calculated_cost = calculate_total_travel_cost(self.solution_tour, self.cities)
        # Allowing a small numeric tolerance for floating point arithmetic issues
        self.assertAlmostEqual(calculated_cost, self.solution_cost, places=2)
    
    def test_only_considers_given_cities(self):
        for city_index in self.solution_tour:
            self.assertIn(city_index, self.cities)

unittest.main(argv=[''], exit=False)