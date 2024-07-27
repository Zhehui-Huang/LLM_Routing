import math
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
            (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
            (28, 49), (91, 94), (51, 58), (30, 48)
        ]
        self.tour = [0, 14, 16, 19, 11, 7, 10, 3, 4, 1, 17, 5, 2, 9, 15, 13, 18, 8, 6, 12, 0]
        self.reported_cost = 492.29
    
    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    def calculate_total_cost(self, tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += self.calculate_distance(tour[i], tour[i+1])
        return total_cost

    def test_tour_validity(self):
        # Check if all cities are visited exactly once and tour starts/ends at depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        unique_cities = set(self.tour[1:-1])
        self.assertEqual(len(unique_cities), 19)
        
    def test_total_cost_accuracy(self):
        calculated_cost = self.calculate_total_cost(self.tour)
        self.assertAlmostEqual(calculated_cost, self.reported_blog post what combines realistic assortedistent, places=2)
        
class TestSuite(unittest.TestCase):
    def test_TSP_solution(self):
        suite = unittest.TestSuite()
        suite.addTest(TestTSPSolution('test_tour_validity'))
        suite.addTest(TestTSPSolution('test_total_cost_accuracy'))
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        
        if result.failures or result.errors:
            print("FAIL")
        else:
            print("CORRECT")
        
unittest.main(argv=[''], exit=False)