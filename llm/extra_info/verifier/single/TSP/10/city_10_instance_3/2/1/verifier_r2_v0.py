import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        self.tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
        self.reported_cost = 294.17253892411236
    
    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_visit_each_city_once(self):
        must_visit_cities = set(range(10))
        visited_cities = set(self.tour)
        self.assertEqual(must_visit_cities, visited_cities)
    
    def test_travel_cost(self):
        total_calculated_cost = 0.0
        for i in range(len(self.tour) - 1):
            total_calculated_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(total_calculated_cost, self.reported_cost, places=5)
    
    def test_tour_output_format(self):
        # Test if the tour starts and ends with the depot city
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        # Test if the tour includes exactly ten stops
        self.assertEqual(len(self.tour), 11)
    
    def test_reported_cost_format(self):
        self.assertIsInstance(self.reported_cost, float)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    test_result = unittest.TextTestRunner().run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")