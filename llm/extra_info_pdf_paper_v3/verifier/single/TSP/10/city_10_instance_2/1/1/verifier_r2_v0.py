import math
import unittest

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (90, 3),
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        self.tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
        self.total_travel_cost = 384.7863591860825  # This is provided as the optimal cost

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city")

    def test_all_cities_visited_exactly_once(self):
        for city in range(1, 10):
            self.assertEqual(self.tour.count(city), 1, f"City {city} is not visited exactly once")

    def test_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
        self.assertAlmostEqual(calculated_cost, self.total_travel_cost, places=5, msg="Total travel cost calculated does not match")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")