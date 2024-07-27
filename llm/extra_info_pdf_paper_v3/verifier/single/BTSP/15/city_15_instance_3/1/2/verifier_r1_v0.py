import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
            (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
            (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
        ]
        self.tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
        self.total_cost_provided = 373.61498801130097
        self.max_distance_provided = 94.11163583744573
    
    def test_unique_visit(self):
        # Check if all cities except the depot are visited exactly once
        tour_without_depot = self.tour[1:-1]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 14)  # There are 14 other cities
        self.assertEqual(len(tour_without_depot), 14)  # Each city is visited once
    
    def test_start_end_depot(self):
        # Check if the tour starts and ends at the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_total_cost_and_max_distance(self):
        # Calculate total travel cost and maximum distance
        total_cost_calculated = 0
        max_distance_calculated = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            distance = math.sqrt((self.cities[city1][0] - self.cities[city2][0])**2 + (self.cities[city1][1] - self.cities[city2][1])**2)
            total_cost_calculated += distance
            if distance > max_distance_calculated:
                max_distance_calculated = distance
        
        # Assert the total cost and maximum distance
        self.assertAlmostEqual(total_cost_calified, self.total_cost_provided, places=5)
        self.assertAlmostEqual(max_distance_calculated, self.max_distance_provided, places=5)

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTourSolution)
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")