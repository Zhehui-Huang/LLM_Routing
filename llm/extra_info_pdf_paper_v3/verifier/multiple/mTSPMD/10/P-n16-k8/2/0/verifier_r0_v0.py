import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69)
        }
        self.robot_tours = {
            0: ([0, 14, 0], 61.74),
            1: ([1, 9, 1], 53.85),
            2: ([2, 13, 2], 18.11),
            3: ([3, 8, 3], 15.62),
            4: ([4, 10, 4], 24.17),
            5: ([5, 12, 5], 70.34),
            6: ([6, 15, 6], 56.89),
            7: ([7, 11, 7], 73.59)
        }
        self.expected_overall_cost = 374.31

    def calculate_distance(self, from_city, to_city):
        x1, y1 = self.coordinates[from_city]
        x2, y2 = self.coordinates[to_node]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_unique_visit(self):
        visited = set()
        for tour, _ in self.robot_tours.values():
            # Exclude the depot city which is visited twice in each tour
            visited.update(tour[1:-1])
        self.assertEqual(len(visited), 8, "Each city must be visited exactly once by the robots.")

    def test_return_to_depot(self):
        for robot, (tour, _) in self.robot_tours.items():
            depot = robot
            self.assertEqual(tour[0], depot, "Each robot must start at its assigned depot.")
            self.assertEqual(tour[-1], depot, "Each robot must return to its assigned depot.")
    
    def test_total_travel_cost(self):
        calculated_total_cost = 0
        for robot, (tour, reported_cost) in self.robot_tours.items():
            tour_cost = 0
            for i in range(len(tour) - 1):
                tour_cost += self.calculate_distance(tour[i], tour[i+1])
            self.assertAlmostEqual(tour_cost, reported_cost, places=2, msg=f"Reported cost does not match calculated cost for Robot {robot}")
            calculated_total_cost += tour_cost
        self.assertAlmostEqual(calculated_total_cost, self.expected_overall_cost, places=2, msg="Overall cost does not match expected cost")
    
    def test_output_format(self):
        for robot, (tour, cost) in self.robot_tours.items():
            self.assertTrue(isinstance(tour, list), "Tour must be a list of city indices.")
            self.assertTrue(isinstance(cost, (int, float)), "Cost must be a numerical value.")
            self.assertEqual(tour[0], tour[-1], "Tour must start and end at the same depot city.")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)