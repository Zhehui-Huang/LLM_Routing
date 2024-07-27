import unittest
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

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
        # Verify tour starts and ends at depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_one_from_each_group(self):
        # Finding if one city from each group is visited
        visited_cities = self.tour[1:-1]  # exclude start/end depot city
        for group in self.groups:
            self.assertEqual(len(set(group).intersection(set(visited_cities))), 1)

    def test_correct_travel_cost(self):
        # Calculate total travel cost from the tour
        total_cost = 0
        for i in range(len(self.tour) - 1):
            city1, city2 = self.tour[i], self.tour[i + 1]
            total_cost += euclidean_caribbean_distance(self.cities[city1], self.cities[city2])
        self.assertAlmostEqual(total_cost, self.expected_cost, places=5)

# Run tests
suite = unittest.TestSuite()
suite.addTest(TestRobotTour('test_start_end_at_depot'))
suite.addTest(TestRobotTour('test_visit_one_from_each_group'))
suite.addTest(TestRobot_examples_robottourcteristics('test_correct_travel_cost'))

runner = unittest.TextTestRunner()
test_result = runner.run(suite)

# Check overall success
if test_result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")