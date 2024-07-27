import math
import unittest

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

        self.robot0_tour = [0, 6, 10, 18, 15, 13, 5, 7, 2, 0]
        self.robot1_tour = [1, 8, 3, 4, 11, 14, 12, 17, 16, 9, 1]
        self.robot0_cost = 112.40
        self.robot1_cost = 147.48
        self.total_cost = 259.88
    
    def test_all_cities_visited_once(self):
        all_cities_visited = set(self.robot0_tour[1:-1] + self.robot1_tour[1:-1])
        self.assertEqual(len(all_cities_visited), 18)  # Since there are 18 cities excluding depots

    def test_robot_starts_ends_depot(self):
        self.assertEqual(self.robot0_tour[0], self.robot0_tour[-1])
        self.assertEqual(self.robot0_tour[0], 0)
        self.assertEqual(self.robot1_tour[0], self.robot1_tour[-1])
        self.assertEqual(self.robot1_tour[0], 1)

    def test_travel_cost_accuracy(self):
        def calculate_distance(city1, city2):
            x1, y1 = self.coordinates[city1]
            x2, y2 = self.coordinates[city2]
            return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        calc_robot0_cost = sum(calculate_distance(self.robot0_tour[i], self.robot0_tour[i + 1]) for i in range(len(self.robot0_tour) - 1))
        calc_robot1_cost = sum(calculate_distance(self.robot1_tour[i], self.robot1_tour[i + 1]) for i in range(len(self.robot1_tour) - 1))
        
        # Comparing calculated costs with provided costs, allowing small margin for floating point discrepancies
        self.assertAlmostEqual(calc_robot0_cost, self.robot0_cost, places=2)
        self.assertAlmostEqual(calc_robot1_cost, self.robot1_cost, places=2)
        self.assertAlmostEqual(calc_robot0_cost + calc_robot1_cost, self.total_cost, places=2)
    
    def test_output_format(self):
        self.assertIsInstance(self.robot0_tour, list)
        self.assertIsInstance(self.robot1_tour, list)
        self.assertTrue(all(isinstance(city, int) for city in self.robot0_tour))
        self.assertTrue(all(isinstance(city, int) for city in self.robot1_tour))

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    test_result = unittest.TextTestRunner().run(test_suite)
    
    overall_result = "CORRECT" if test_result.wasSuccessful() else "FAIL"
    print(overall_result)