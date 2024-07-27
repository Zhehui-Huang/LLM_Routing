import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.city_coords = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
            15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
        }

        self.robot_0_tour = [0, 2, 9, 15, 8, 16, 17, 12, 14, 0]
        self.robot_1_tour = [1, 10, 4, 11, 3, 7, 5, 18, 6, 13, 1]

        self.robot_0_cost = 136.05815649765321
        self.robot_1_cost = 150.58145502061055
        self.overall_cost = 286.6396115182638

    def test_robot_count_and_start_points(self):
        self.assertEqual(len({self.robot_0_tour[0], self.robot_1_tour[0]}), 1)
        self.assertEqual(self.robot_0_tour[0], 0)
        self.assertEqual(self.robot_1_tours[0], 1)

    def test_all_cities_visited_once(self):
        all_cities = set(range(19))
        visited_cities = set(self.robot_0_tour + self.robot_1_tour)
        self.assertEqual(all_cities, visited_cities)

    def test_correct_travel_costs(self):
        # Test Robot 0's cost
        total_cost_0 = 0
        for i in range(len(self.robot_0_tour) - 1):
            x1, y1 = self.city_coords[self.robot_0_tour[i]]
            x2, y2 = self.city_coords[self.robot_0_tour[i+1]]
            total_cost_0 += calculate_euclidean_distance(x1, y1, x2, y2)
        self.assertAlmostEqual(total_cost_0, self.robot_0_cost)

        # Test Robot 1's cost
        total_cost_1 = 0
        for i in range(len(self.robot_1_tour) - 1):
            x1, y1 = self.city_coords[self.robot_1_tour[i]]
            x2, y2 = self.city_coords[self.robot_1_tour[i+1]]
            total_cost_1 += calculate_euclidean_distance(x1, y1, x2, y2)
        self.assertAlmostEqual(total_cost_1, self.robot_1_cost)

        # Test overall cost
        self.assertAlmostEqual(total_cost_0 + total_cost_1, self.overall_cost)

    def test_output_format(self):
        # Check the tour format and cost outputs for both robots
        self.assertIsInstance(self.all_tours[0], list)
        self.assertIsInstance(self.all_tours[1], list)
        self.assertEqual(self.all_tours[0][0], self.all_tours[0][-1])
        self.assertEqual(self.all_tours[1][0], self.all_tours[1][-1])
        self.assertIsInstance(self.robot_0_cost, float)
        self.assertIsInstance(self.robot_1_cost, float)

if __name__ == '__main__':
    unittest.main()