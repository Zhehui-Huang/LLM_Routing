import unittest
import numpy as np

# Coordinates of the cities including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

def calculate_distance(city_a, city_b):
    return np.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.robot_tours = [
            [0, 2, 7, 0],
            [0, 9, 10, 0],
            [0, 15, 5, 0],
            [0, 3, 14, 0],
            [0, 11, 8, 0],
            [0, 12, 4, 0],
            [0, 1, 6, 0],
            [0, 13, 0]
        ]
        self.robot_costs = [51.59, 77.87, 91.92, 100.91, 92.23, 64.99, 38.02, 58.24]
        self.overall_cost = 575.77

    def test_unique_visits(self):
        all_visited = set()
        for tour in self.robot_tours:
            all_visited.update(tour[1:-1])  # Collect all the nodes, excluding the depot
        self.assertEqual(len(all_visited), 15)  # Check if all 15 other cities are visited

    def test_correct_start_end_city(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)  # start at depot
            self.assertEqual(tour[-1], 0)  # end at depot

    def test_correct_travel_cost(self):
        calculated_costs = []
        for tour in self.robot_tours:
            cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            calculated_costs.append(cost)
        np.testing.assert_almost_equal(calculated_costs, self.robot_costs, decimal=2)  # Comparing costs

    def test_overall_cost(self):
        total_cost = sum(self.robot_costs)
        self.assertAlmostEqual(total_cost, self.overall_cost, places=2)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 'CORRECT' if result.wasSuccessful() else 'FAIL'

# Run the tests
output = run_tests()
print(output)