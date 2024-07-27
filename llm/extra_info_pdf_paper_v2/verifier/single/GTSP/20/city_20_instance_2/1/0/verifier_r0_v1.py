import unittest
from math import sqrt

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.city_coords = [
            (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
            (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
            (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
        ]

        self.city_groups = [
            [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18],
            [1, 9, 14, 19], [5, 6, 17]
        ]

        self.proposed_tour = [0, 11, 16, 18, 19, 6, 0]
        self.proposed_cost = 162.3829840233368

    def calculate_euclidean_distance(self, city1, city2):
        return sqrt((self.city_coords[city1][0] - self.city_towns[city2][0])**2 + 
                    (self.city_coords[city1][1] - self.city_coords[city2][1])**2)

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.proposed_tour[0], 0)
        self.assertEqual(self.proposed_tour[-1], 0)

    def test_visit_one_city_from_each_group(self):
        visited_groups = [False] * len(self.city_groups)
        for city in self.proposed_tour[1:-1]:  # exclude the depot
            for i, group in enumerate(self.city_groups):
                if city in group:
                    self.assertFalse(visited_groups[i])
                    visited_groups[i] = True
        self.assertTrue(all(visited_groups))

    def test_correct_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.proposed_tour) - 1):
            calculated_cost += self.calculate_euclidean_distance(self.proposed_tour[i], self.proposed_tour[i + 1])
        self.assertAlmostEqual(self.proposed_cost, calculated_cost, places=5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTravelingSalesmanSolution('test_tour_start_end_at_depot'))
    suite.addTest(TestTravelingSalesmanSolution('test_visit_one_city_from_each_group'))
    suite.addTest(TestTravelingSalesmanSolution('test_correct_travel_cost'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

print(run_tests())