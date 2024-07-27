import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
            5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
            10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
            15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
        }
        self.tour = [0, 14, 6, 8, 17, 2, 15, 3, 19, 18, 10, 4, 12, 13, 1, 7, 5, 9, 11, 16, 0]
        self.total_cost = 908.4530364944552

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot")

    def test_visit_all_cities_exactly_once(self):
        self.assertCountEqual(self.tour[1:-1], list(range(1, 20)), "All other cities should be visited exactly once")

    def test_correct_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.cities[self.tour[i]]
            city2 = self.cities[self.tour[i + 1]]
            distance = math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
            calculated_cost += distance
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5, "Total travel cost should be accurately calculated")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTravelingSalesmanSolution('test_tour_starts_and_ends_at_depot'))
    suite.addTest(TestTravelingSalesmanSolution('test_visit_all_cities_exactly_once'))
    suite.addTest(TestTravelingSalesmanSolution('test_correct_total_travel_cost'))

    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()