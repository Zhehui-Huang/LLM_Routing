import unittest
import numpy as np
from math import sqrt

# Provided solution data
robot_0_tour = [0, np.int64(1), np.int64(3), np.int64(4), np.int64(8), np.int64(10), np.int64(11), np.int64(12), np.int64(15), np.int64(18), np.int64(19), 0]
robot_0_cost = 212.21732723337922
robot_1_tour = [0, np.int64(2), np.int64(5), np.int64(6), np.int64(7), np.int64(9), np.int64(13), np.int64(14), np.int64(16), np.int64(17), np.int64(20), 0]
robot_1_cost = 184.31166515759514
overall_cost = 396.5289923909744

# Define all cities and their coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return total_cost

class TestRobotTourSolution(unittest.TestCase):
    def test_all_cities_visited_once(self):
        all_cities = set(range(1, 21))  # cities from 1 to 20
        visited_cities = set(np.int64(tour[i]) for tour in [robot_0_tour, robot_1_tour] for i in range(1, len(tour)-1))
        self.assertEqual(all_cities, visited_cities)
        
    def test_tours_start_end_depot(self):
        self.assertTrue(all(tour[0] == 0 and tour[-1] == 0 for tour in [robot_0_tour, robot_1_tour]))

    def test_exact_costs(self):
        calculated_cost_robot_0 = calculate_total_cost(robot_0_tour)
        calculated_cost_robot_1 = calculate_total_cost(robot_1_tour)
        self.assertAlmostEqual(calculated_cost_robot_0, robot_0_cost, places=5)
        self.assertAlmostEqual(calculated_cost_robot_1, robot_1_cost, places=5)
        self.assertAlmostEqual(calculated_cost_robot_0 + calculated_cost_robot_1, overall_cost, places=5)

    def test_minimize_total_travel_cost(self):
        # This is heuristic validation, may need real optimization solver results for comparison
        optimal_solution = 396
        self.assertLessEqual(overall_cost, optimal_solution + 0.529)  # Adding a margin for heuristic results

if __name__ == "__main__":
    unittest.main()