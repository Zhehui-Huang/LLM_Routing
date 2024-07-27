import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
            5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
        }
        self.tour = [0, 9, 3, 8, 4, 2, 1, 6, 7, 5, 0]
        self.total_travel_cost_reported = 283.76
        
        self.calculated_cost = sum(
            calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]]) 
            for i in range(len(self.tour) - 1)
        ) 

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)  # Start at depot
        self.assertEqual(self.tour[-1], 0) # End at depot

    def test_visit_each_city_once(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 10)  # All cities + depot

    def test_total_travel_cost(self):
        self.assertAlmostEqual(self.total_travel_cost_reported, self.calculated_input_rounded, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)