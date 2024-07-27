import unittest
import numpy as np

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTravelSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
            4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
            8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
            12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
            16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
            20: (155, 185), 21: (139, 182)
        }
        self.robot_tours = {
            0: [0, 14, 16, 17, 19, 21, 20, 18, 15, 12, 9, 7, 5, 10, 8, 6, 4, 11, 13, 0],
            1: [1, 1],
            2: [2, 2],
            3: [3, 3]
        }
        self.expected_costs = {
            0: 256.27,
            1: 0.00,
            2: 0.00,
            3: 0.00
        }

    def test_all_cities_visited_exactly_once(self):
        visited = set()
        for robot, tour in self.robot_tours.items():
            if len(tour) > 2:
                visited.update(tour[1:-1])
        self.assertEqual(len(visited), 18)

    def test_each_robot_returns_to_start(self):
        for robot, tour in self.robot_tours.items():
            self.assertEqual(tour[0], tour[-1])

    def test_calculate_travel_costs(self):
        for robot, tour in self.robot_tours.items():
            total_cost = 0
            for i in range(len(tour) - 1):
                city1, city2 = tour[i], tour[i + 1]
                total_cost += calculate_distance(self.coordinates[city1], self.coordinates[city2])
            rounded_cost = round(total_cost, 2)
            self.assertAlmostEqual(rounded_cost, self.expected_costs[robot], places=2)

def run_tests():
    suite = unittest.TestSuite(unittest.makeSuite(TestTravelSolution))
    result = unittest.TextTestRunner().run(suite)
    print("CORRECT" if result.wasSuccessful() else "FAIL")

run_tests()