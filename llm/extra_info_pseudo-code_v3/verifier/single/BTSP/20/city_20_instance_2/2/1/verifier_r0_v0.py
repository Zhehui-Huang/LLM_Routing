import unittest
import math

def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestBottleneckTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (3, 26), 
            (85, 72), 
            (67, 0), 
            (50, 99), 
            (61, 89), 
            (91, 56), 
            (2, 65), 
            (38, 68), 
            (3, 92), 
            (59, 8), 
            (30, 88), 
            (30, 53), 
            (11, 14), 
            (52, 49), 
            (18, 49), 
            (64, 41), 
            (28, 49), 
            (91, 94), 
            (51, 58), 
            (30, 48)
        ]
        self.tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        self.total_travel_cost = 1121.3977961950163
        self.max_consecutive_distance = 100.9554357129917
    
    def test_tour_start_end_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_visit_each_city_once(self):
        # Requirement 2
        tour_without_depot_return = self.tour[:-1]
        unique_cities = set(tour_without_depot_return)
        self.assertEqual(len(unique_cities), 20)
        self.assertEqual(sorted(unique_cities), list(range(20)))
    
    def test_output_tour_format(self):
        # Requirement 4
        self.assertIsInstance(self.tour, list)
        self.assertTrue(all(isinstance(city, int) for city in self.tour))
    
    def test_output_total_travel_cost(self):
        # Requirement 5
        calculated_cost = sum(
            calc_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            for i in range(len(self.tour) - 1)
        )
        self.assertAlmostEqual(calculated_cost, self.total_travel_cost)
    
    def test_output_max_distance(self):
        # Requirement 6
        calculated_max_distance = max(
            calc_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            for i in range(len(self.tour) - 1)
        )
        self.assertAlmostEqual(calculated_max_distance, self.max_consecutive_distance)

# Run the tests
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestBottleneckTSPSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")