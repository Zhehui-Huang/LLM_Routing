import unittest
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
            4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
            8: (49, 29), 9: (13, 17)
        }
        self.groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]
        self.tour = [0, 3, 5, 9, 1, 2, 0]
        self.expected_cost = 281.60273931778477

    def test_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_one_from_each_group(self):
        visited_cities = self.tour[1:-1]  # Remove initial and final depot visit
        found_cities_from_groups = [False for _ in self.groups]
        for index, group in enumerate(self.groups):
            if any(city in group for city in visited_cities):
                found_cities_from_groups[index] = True
        self.assertTrue(all(found_cities_from_groups))

    def test_correct_travel_cost(self):
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(total_cost, self.expected_cost, places=5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTour('test_start_end_at_depot'))
    suite.addTest(TestRobotTour('test_visit_one_from_each_group'))
    suite.addTest(TestRobotTour('test_correct_travel_cost'))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    run_tests()