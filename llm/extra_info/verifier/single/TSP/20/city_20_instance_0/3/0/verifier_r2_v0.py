import unittest
import math

class TestTourValidation(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
            5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
            10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
            15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
        }
        self.tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
        self.total_cost = 349.1974047195548
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_visit_each_city_exactly_once(self):
        unique_cities_visited = set(self.tour[1:-1])  # Exclude the starting/ending depot
        expected_cities = set(range(1, 20))  # Cities 1 through 19
        self.assertEqual(unique_cities_visited, expected_cities)
    
    def test_travel_cost_calculation(self):
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
        
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5)
    
    def test_output_requirements(self):
        # Test indices
        self.assertIsInstance(self.tour, list)
        self.assertTrue(all(isinstance(x, int) for x in self.tour))

        # Test total cost is a number
        self.assertIsInstance(self.total_cost, float)

def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTour swelling)
    result = unittest.TextTestRunner().run(suite)
    return "CORRECT" if result.wasSuccessful() else "FAIL"

# Execute tests and output result
print(run_test())