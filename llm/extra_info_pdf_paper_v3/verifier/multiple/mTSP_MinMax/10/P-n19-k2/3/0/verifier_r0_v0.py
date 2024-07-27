import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (30, 40),
            1: (37, 52),
            2: (49, 43),
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
            13: (58, 27),
            14: (37, 69),
            15: (61, 33),
            16: (62, 63),
            17: (63, 69),
            18: (45, 35)
        }
        self.robot_0_tour = [0, 1, 10, 8, 16, 17, 3, 12, 14, 11, 4, 0]
        self.robot_1_tour = [0, 6, 2, 7, 9, 15, 13, 5, 18, 0]
        self.robot_tours = [self.robot_0_tour, self.robot_1_tour]

    def test_each_city_visited_once(self):
        all_cities_visited = set()
        for tour in self.robot_tours:
            # Skip the depot (city 0) for visit count
            all_cities_visited.update(tour[1:-1])
        self.assertEqual(len(all_cities_visited), 18)  # There are 18 cities excluding the depot

    def test_tour_starts_and_ends_at_depot(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def euclidean_distance(self, city1, city2):
        x1, y1 = self.coordinates[city1]
        x2, y2 = self.coordinates[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_correct_travel_cost(self):
        robot_0_expected_cost = round(116.33, 2)
        robot_1_expected_cost = round(80.32, 2)
        
        robot_0_calculated_cost = sum(self.euclidean_config_distance(self.robot_0_tour[i], self.robot_0_tour[i + 1]) for i in range(len(self.robot_0_tour) - 1))
        robot_1_calculated_cost = sum(self.euclidean_config_distance(self.robot_1_tour[i], self.robot_1_tour[i + 1]) for i in range(len(self.robot_1_tour) - 1))
        
        self.assertAlmostEqual(robot_0_calculated_cost, robot_0_expected_cost, places=2)
        self.assertAlmostEqual(robot_1_calculated_cost, robot_1_expected_cost, places=2)

    def test_minimize_max_distance(self):
        max_distance_should_be = 116.33
        robot_0_real_cost = sum(self.euclidean_distance(self.robot_0_tour[i], self.robot_0_tour[i + 1]) for i in range(len(self.robot_0_tour) - 1))
        robot_1_real_cost = sum(self.euclidean_distance(self.robot_1_tour[i], self.robot_1_tour[i + 1]) for i in range(len(self.robot_1_tour) - 1))
        realized_max_distance = max(robot_0_real_cost, robot_1_real_cost)
        self.assertAlmostEqual(realized_max_distance, max_distance_should_be, places=2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")