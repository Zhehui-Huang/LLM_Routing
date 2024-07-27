import unittest
import math

class TestTSPTour(unittest.TestCase):
    def setUp(self):
        # City coordinates from the problem description
        self.cities = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
            (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
            (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
            (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
        ]
        self.solution_tour = [0, 19, 8, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 13, 1, 18, 17, 0]
        self.reported_cost = 398.67

    def test_tour_start_end_at_depot(self):
        # Check if tour starts and ends at the depot city 0.
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_visit_each_city_once(self):
        # Check if all cities except depot is visited exactly once
        for city in range(1, 20):
            self.assertEqual(self.solution_tour.count(city), 1)
            
    def test_total_distance(self):
        # Calculate total travel distance of the solution.
        def euclidean_distance(a, b):
            return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            city1 = self.solution_tour[i]
            city2 = self.solution_tour[i + 1]
            calculated_cost += euclidean_distance(self.cities[city1], self.cities[city2])
        calculated_cost = round(calculated_cost, 2)
        
        # Check if the reported travel cost matches the calculated cost.
        self.assertAlmostEqual(self.reported_cost, calculated_cost, places=2)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPTour)
    results = unittest.TextTestRunner(verbosity=2).run(suite)
    if results.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Output the result of all tests
print(run_tests())