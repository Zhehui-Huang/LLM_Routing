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
        self.robot_0_tour = [0, 0]
        self.robot_1_tour = [1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.total_cost = 0  # As per provided solution, though it is likely incorrect.

    def test_starts_from_depot(self):
        # Test if each robot starts from its designated depot
        self.assertEqual(self.robot_0_tour[0], 0)
        self.assertEqual(self.robot_1_tour[0], 1)

    def test_each_city_visited_once(self):
        # Test if every city except depots is visited exactly once
        all_cities = self.robot_0_tour + self.robot_1_tour
        visited_cities = set(all_cities)
        self.assertEqual(len(all_cities), len(visited_cities))

    def test_optimized_travel_cost(self):
        # Calculate the total travel cost from the path
        def distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # Total distance traveled by robot 0
        cost_robot_0 = sum(distance(self.robot_0_tour[i], self.robot_0_tour[i + 1]) for i in range(len(self.robot_0_tour) - 1))
        # Total distance traveled by robot 1
        cost_robot_1 = sum(distance(self.robot_1_tour[i], self.robot_1_tour[i + 1]) for i in range(len(self.robot_1_tour) - 1))

        # Compare with given cost
        self.assertEqual(cost_robot_0 + cost_robot_1, self.total

    def test_no_city_visited_more_than_once(self):
        # Check if no city is visited more than once across all robots
        all_tour = self.robot_0_tour + self.robot_1_tour
        unique_cities = set(all_tour)

        # Verify that the count in list matches set lengths
        self.assertEqual(len(all_tour), len(unique_cities))
        

if __name__ == "__main__":
    unittest.main()