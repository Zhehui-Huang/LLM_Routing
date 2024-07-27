import unittest
from math import sqrt

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35)
}

# Tours from the proposed solution
robot_0_tour = [0, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 0]
robot_1_tour = [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0]

# Provided costs
robot_0_cost = 143.98241284438606
robot_1_cost = 109.8362166450987
total_cost = 253.81862948948475

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_tour_cost(tour):
    return sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

class TestMTSPSolution(unittest.TestCase):
    def test_start_end_at_depot(self):
        self.assertEqual(robot_0_tour[0], 0)
        self.assertEqual(robot_0_tour[-1], 0)
        self.assertEqual(robot_1_tour[0], 0)
        self.assertEqual(robot_1_tour[-1], 0)

    def test_each_city_visited_once(self):
        all_cities_visited = sorted(robot_0_tour[1:-1] + robot_1_tour[1:-1])
        expected_cities = list(range(1, 21))  # cities 1 through 20
        self.assertEqual(all_cities_visited, expected_cities)

    def test_correct_tour_costs(self):
        calculated_robot_0_cost = calculate_total_tour_cost(robot_0_tour)
        calculated_robot_1_cost = calculate_total_tour_cost(robot_1_tour)
        self.assertAlmostEqual(calculated_robot_0_cost, robot_0_cost, places=5)
        self.assertAlmostEqual(calculated_robot_1_cost, robot_1_cost, places=5)

    def test_correct_total_costs(self):
        calculated_total_cost = calculate_total_tour_cost(robot_0_tour) + calculate_total_tour_cost(robot_1_tour)
        self.assertAlmostEqual(calculated_total_cost, total_cost, places=5)

def verify_solution():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMTSPSolution)
    result = unittest.TextTestRunner(verbosity=0).run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

print(verify_solution())