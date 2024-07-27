import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }
        # As provided:
        self.robot_0_tour = [0, 0]   
        self.robot_1_tour = [1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.total_cost = 0  # Placeholder for calculated total cost

    def test_starts_from_depot_and_ends_at_any(self):
        # Ensure correct start; endings are not back at depot under task rules
        correct_start_0 = self.robot_0_tour[0] == 0
        correct_start_1 = self.robot_1_tour[0] == 1
        self.assertTrue(correct_start_0 and correct_start_1)

    def test_each_city_visited_once(self):
        # All cities are visited exactly once in the solution
        all_cities = set(self.robot_0_tour + self.robot_1_tour)
        self.assertEqual(len(all_cities), 21) # 21 cities from 0 to 20

    def test_optimized_travel_cost(self):
        # Test for correct optimized travel cost
        def distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.hypot(x2 - x1, y2 - y1)

        # Calculate total travel distance considering tours of both robots
        cost_robot_0 = sum(distance(self.robot_0_tour[i], self.robot_0_tour[i + 1]) for i in range(len(self.robot_0_tour) - 1))
        cost_robot_1 = sum(distance(self.robot_1_tour[i], self.robot_1_tour[i + 1]) for i in range(len(self.robot_1_tour) - 1))

        self.assertAlmostEqual(cost_robot_0 + cost_robot_1, 0)  # Using provided total cost

    def test_no_city_visited_more_than_once(self):
        all_visits = self.robot_0_tour + self.robot_1_tour
        unique_visits = set(all_visits)
        self.assertEqual(len(all_visits), len(unique_visits) + 1)  # Only depot cities can repeat

if __name__ == "__main__":
    unittest.main()