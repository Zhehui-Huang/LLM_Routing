import numpy as np
import unittest

class TestTravelingRobot(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56), 6: (2, 65),
            7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53), 12: (11, 14),
            13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58),
            19: (30, 48)
        }
        self.tour = [0, 7, 3, 4, 1, 15, 13, 18, 19, 16, 0]
        self.reported_cost = 252.57716996890326

    def test_tour_length(self):
        # Check if exactly 10 cities are visited
        expected_cities_count = 10  # Include both start/end city
        self.assertEqual(len(set(self.tour)), expected_cities_count)

    def test_tour_loop(self):
        # Check if the tour starts and ends at the depot
        self.assertEqual(self.tour[0], self.tour[-1])

    def test_tour_cost(self):
        # Calculate and compare travel cost
        def calculate_distance(city_a, city_b):
            x1, y1 = city_a
            x2, y2 = city_b
            return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        
        np.testing.assert_almost_equal(total_cost, self.reported_cost, decimal=5)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTravelingRobot))
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")