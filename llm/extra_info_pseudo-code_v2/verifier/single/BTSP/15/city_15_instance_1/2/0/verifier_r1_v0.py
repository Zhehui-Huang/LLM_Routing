import unittest
from math import sqrt

# Provided cities' coordinates indexed by city ID
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
        self.total_cost = 442.570870788815
        self.max_distance = 85.21150157109074
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_each_city_visited_once(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), len(cities))
    
    def test_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.total_cost, float)
        self.assertIsInstance(self.max_distance, float)
    
    def test_total_travel_cost(self):
        calculated_cost = sum(calculate_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated, self.total_cost, places=2)
    
    def test_max_distance(self):
        distances = [calculate_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1)]
        self.assertAlmostEqual(max(distances), self.max_distance, places=2)


# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)