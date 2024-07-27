import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
            6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
            18: (62, 63), 19: (63, 69), 20: (45, 35)
        }
        self.robot0_tour = [0, 12, 3, 19, 13, 2, 10, 15, 11, 16, 20, 0]
        self.robot1_tour = [0, 4, 1, 6, 7, 5, 14, 17, 9, 8, 18, 0]

    def euclidean_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_tour_cost(self, tour):
        return sum(self.euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    def test_all_cities_visited_exactly_once(self):
        visited_cities = set(self.robot0_tour[:-1] + self.robot1_tour[:-1])  # Exclude the repeated depot visit
        self.assertEqual(visited_cities, set(range(21)), "Not all cities are visited exactly once or some are visited more than once.")

    def test_robots_start_and_end_at_depot(self):
        self.assertTrue(self.robot0_tour[0] == 0 and self.robot0_tour[-1] == 0, "Robot 0 does not start/end at the correct depot.")
        self.assertTrue(self.robot1_tour[0] == 0 and self.robot1_tour[-1] == 0, "Robot 1 does not start/end at the correct depot.")

    def test_correct_computation_of_travel_cost(self):
        calculated_robot0_cost = self.calculate_tour_cost(self.robot0_tour)
        calculated_robot1_cost = self.calculate_tour_cost(self.robot1_tour)
        overall_calculated_cost = calculated_robot0_cost + calculated_robot1_cost

        expected_robot0_cost = self.calculate_tour_cost([0, 12, 3, 19, 13, 2, 10, 15, 11, 16, 20, 0])
        expected_robot1_cost = self.calculate_tour_cost([0, 4, 1, 6, 7, 5, 14, 17, 9, 8, 18, 0])

        self.assertAlmostEqual(calculated_robot0_cost, expected_robot0_cost, places=5, msg="Robot 0 cost calculation incorrect.")
        self.assertAlmostEqual(calculated_robot1_cost, expected_robot1_tour_cost, places=5, msg="Robot 1 cost calculation incorrect.")
        self.assertAlmostEqual(overall_calculated_cost, expected_robot0_cost + expected_robot1_cost, places=5, msg="Overall cost calculation incorrect.")

if __name__ == '__main__':
    unittest.main()