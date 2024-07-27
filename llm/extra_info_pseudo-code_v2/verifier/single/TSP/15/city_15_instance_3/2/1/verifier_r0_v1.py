import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (16, 90), 
            (43, 99), 
            (80, 21), 
            (86, 92), 
            (54, 93), 
            (34, 73), 
            (6, 61), 
            (86, 69), 
            (30, 50), 
            (35, 73), 
            (42, 64), 
            (64, 30), 
            (70, 95), 
            (29, 64), 
            (32, 79) 
        ]
        self.tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
        self.reported_cost = 373.61498801130097

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        visited_cities = set(self.tour[1:-1])
        expected_cities = set(range(1, 15))
        self.assertEqual(visited_cities, expected_cities)

    def test_travel_cost(self):
        actual_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            actual_cost += sqrt((x2 - x1)**2 + (y2 - y1)**2)
        self.assertAlmostEqual(actual_cost, self.reported_cost, places=5)

    def test_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.reported_cost, float)

def run_tests():
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestRobotTour))

    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == '__main__':
    runTests()