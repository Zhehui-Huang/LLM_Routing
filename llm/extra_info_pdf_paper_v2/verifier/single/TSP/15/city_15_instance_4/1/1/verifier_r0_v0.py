import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
            (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
            (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
        ]
        self.tour = [0, 10, 13, 14, 8, 3, 6, 11, 12, 4, 7, 2, 9, 5, 1, 0]
        self.reported_cost = 288.5242816725832

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Does not start at the depot city")
        self.assertEqual(self.tour[-1], 0, "Does not end at the depot city")

    def test_visit_each_city_once(self):
        visited_once = all(self.tour.count(city) == 1 for city in range(1, 15))
        self.assertTrue(visited_once, "Each city other than depot must be visited exactly once.")
        self.assertEqual(len(self.tour), len(set(self.tour)), "Each city must be visited exactly once including the depot.")

    def test_total_travel_cost(self):
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, msg="Reported total travel cost is incorrect.")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_starts_and_ends_at_depot'))
    test_suite.addTest(TestTSPSolution('test_visit_each_city_once'))
    test_suite.addTest(TestTSPSolution('test_total_travel_cost'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")