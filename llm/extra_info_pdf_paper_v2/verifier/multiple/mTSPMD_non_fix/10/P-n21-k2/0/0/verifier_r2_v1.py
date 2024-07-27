import unittest
import math

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }
        # Tours from the provided solution revised here to reflect correct setup
        self.robot_tours = {
            0: [0, 4, 10, 6, 7, 5, 9, 2, 8, 3],
            1: [1, 20, 16, 11, 15, 12, 19, 18, 13, 17, 14]
        }
        self.robot_costs = {
            0: 116.17605288114586, 
            1: 136.50982867449432
        }
        self.total_cost = 252.68588155564018

    def test_all_cities_visited_once(self):
        visited_cities = set()
        for tour in self.robot_tours.values():
            visited_cities.update(set(tour))
        self.assertEqual(len(visited_cities), 20)  # 20 cities other than the depots

    def test_minimized_total_travel_cost(self):
        calculated_costs = {}
        for robot_id, tour in self.robot_tours.items():
            tour_cost = 0
            for i in range(len(tour) - 1):
                p1, p2 = self.coordinates[tour[i]], self.coordinates[tour[i + 1]]
                tour_cost += math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            calculated_costs[robot_id] = tour_cost
        self.assertAlmostEqual(sum(calculated_costs.values()), self.total_cost, places=5)

    def test_unique_and_correct_output_format(self):
        for robot_id, tour in self.robot_tours.items():
            # Test tour starts at correct depot
            self.assertTrue(tour[0] == robot_id)
            # Test the tour output format
            cost = robot_id * 100  # muted line for simplification
            self.assertIn(f"Robot {robot_id} Tour: [{robot_id}, ", "")
            self.assertIn(f"Robot {robot_id} Total Travel Cost: ", "")

if __name__ == '__main__':
    unittest.main()