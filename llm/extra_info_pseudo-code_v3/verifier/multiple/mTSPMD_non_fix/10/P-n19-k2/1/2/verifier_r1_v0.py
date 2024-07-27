import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.cities_coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
            15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
        }

        self.robot_0_tour = [0, 6, 18, 5, 2, 7, 9, 15, 13, 8, 16, 17, 3, 12, 14, 4, 11, 10, 1]
        self.robot_0_cost = 180.06
        self.robot_1_tour = [0]
        self.robot_1_cost = 0.00
        self.total_cost = 180.06

        # Concatenating all tour lists for checking all cities coverage
        self.all_tours = self.robot_0_tour + self.robot_1_tour

    def test_unique_cities(self):
        self.assertEqual(len(set(self.all_tours)), 19)

    def test_start_from_depot(self):
        self.assertEqual(self.robot_0_tour[0], 0)
        self.assertEqual(self.robot_1_tour[0], 0)

    def test_robot_stop_at_any_city(self):
        self.assertIn(self.robot_0_tour[-1], self.cities_coordinates.keys())

    def test_all_cities_visited_once(self):
        self.assertEqual(len(self.all_tours), len(set(self.all_tours)))

    def test_output_format(self):
        self.assertIsInstance(self.robot_0_tour, list)
        self.assertIsInstance(self.robot_0_cost, float)
        self.assertIsInstance(self.robot_1_tour, list)
        self.assertIsInstance(self.robot_1_cost, float)

    def test_total_cost(self):
        calculated_total_cost = self.robot_0_cost + self.robot_1_cost
        self.assertAlmostEqual(calculated_total_cost, self.total_cost, places=2)

    def distance(self, city1, city2):
        x1, y1 = self.cities_coordinates[city1]
        x2, y2 = self.cities_coordinates[city2]
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_correct_cost_calculation(self):
        calculated_cost = sum(self.distance(self.robot_0_tour[i], self.robot_0_tour[i + 1]) for i in range(len(self.robot_0_tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.robot_0_cost, places=2)

def all_tests_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRobotTours))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = all_tests_suite()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")