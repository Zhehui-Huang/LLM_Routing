import unittest
from math import sqrt

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Provided solution
robot_tours = {
    0: [0, 6, 18, 5, 13, 0],
    1: [1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 9, 15, 7, 2, 1]
}
robot_costs = {
    0: 65.38588785567701,
    1: 152.87924674656497
}
overall_cost = 218.26513460224197

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_cost += sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_cost

class TestRobotTours(unittest.TestCase):
    def test_tour_coverage(self):
        all_visited_cities = robot_tours[0] + robot_tours[1]
        unique_cities = set(all_visited_cities)
        self.assertEqual(len(unique_cities), 19)

    def test_return_to_depot(self):
        self.assertEqual(robot_tours[0][0], robot_tours[0][-1])
        self.assertEqual(robot_tours[1][0], robot_tours[1][-1])

    def test_cost_calculation(self):
        self.assertAlmostEqual(calculate_cost(robot_tours[0]), robot_costs[0])
        self.assertAlmostEqual(calculate_cost(robot_tours[1]), robot_costs[1])

    def test_overall_cost(self):
        calculated_overall_cost = calculate_cost(robot_tours[0]) + calculate_cost(robot_tours[1])
        self.assertAlmostEqual(calculated_overall_cost, overall_cost)

# Running the tests
suite = unittest.TestSuite()
suite.addTest(TestRobotTours('test_tour_coverage'))
suite.addTest(TestRobotTours('test_return_to_depot'))
suite.addTest(TestRobotTours('test_cost_calculation'))
suite.addTest(TestRobotTours('test_overall_cost'))

runner = unittest.TextTestRunner()
result = runner.run(suite)
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")