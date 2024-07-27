import unittest
import numpy as np

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Coordinates as provided for the cities
        self.cities = {
            0: (30, 40),
            1: (37, 52),
            2: (49, 49),
            3: (52, 64),
            4: (31, 62),
            5: (52, 33),
            6: (42, 41),
            7: (52, 41),
            8: (57, 58),
            9: (62, 42),
            10: (42, 57),
            11: (27, 68),
            12: (43, 67),
            13: (58, 48),
            14: (58, 27),
            15: (37, 69),
            16: (38, 46),
            17: (61, 33),
            18: (62, 63),
            19: (63, 69),
            20: (45, 35)
        }
        
        self.robot_0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 8, 18, 19, 3, 2, 7, 13, 9, 17, 14, 5, 20, 6, 0]
        self.robot_1_tour = [1, 16, 6, 20, 5, 7, 14, 17, 9, 13, 8, 18, 19, 3, 12, 15, 4, 11, 10, 2, 0, 1]
        
        self.robot_0_cost = round(203.36904934904857, 2)
        self.robot_1_cost = round(204.35668675029683, 2)
        self.total_cost = round(407.7257360993454, 2)

    def test_city_count(self):
        # Ensure all cities including the depots are accounted for
        unique_cities = set(self.robot_0_tour + self.robot_1_tour)
        self.assertEqual(len(unique_cities), 21)

    def test_start_and_end_depot(self):
        # Both robots should start and end at their assigned depots
        self.assertEqual(self.robot_0_tour[0], self.robot_0_tour[-1])
        self.assertEqual(self.robot_0_tour[0], 0)
        self.assertEqual(self.robot_1_tour[0], self.robot_1_tour[-1])
        self.assertEqual(self.robot_1_tour[0], 1)

    def test_total_travel_cost(self):
        # Calculate the total travel cost for each robot using the Euclidean distance
        def calculate_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        robot_0_calc_cost = sum(calculate_distance(self.robot_0_tour[i], self.robot_0_tour[i+1]) for i in range(len(self.robot_0_tour) - 1))
        robot_1_calc_cost = sum(calculate_distance(self.robot_1_tour[i], self.robot_1_tour[i+1]) for i in range(len(self.robot_1_tour) - 1))

        self.assertAlmostEqual(robot_0_calc_cost, self.robot_0_cost, places=2)
        self.assertAlmostEqual(robot_1_calc_cost, self.robot_1_cost, places=2)
        self.assertAlmostEqual(robot_0_calc_cost + robot_1_calc_config, self.total_cost, places=2)

    def test_city_visit_once(self):
        # Ensure each city other than depots is visited exactly once
        city_visits = [0] * 21
        for tour in [self.robot_0_tour, self.robot_1_tour]:
            for city in tour:
                city_visits[city] += 1

        for i in range(2, 21):  # Cities other than depots should be visited exactly once
            self.assertEqual(city_visits[i], 1)
        # Depots are visited twice because each robot starts and ends there
        self.assertEqual(city_visits[0], 2)
        self.assertEqual(city_visits[1], 2)

if __name__ == '__main__':
    unittest.main()