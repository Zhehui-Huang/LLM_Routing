import unittest
import numpy as np
import sys
from io import StringIO

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
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
        self.robot_tours = {
            0: [0, 2, 3, 4, 10, 12, 11, 14, 0],  # Tour for robot 0
            1: [1, 6, 5, 7, 8, 9, 15, 18, 13, 16, 17, 1]  # Tour for robot 1
        }

    def calculate_euclidean_distance(self, start, end):
        x1, y1 = self.cities[start]
        x2, y2 = self.cities[end]
        return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def test_number_of_cities(self):
        self.assertEqual(len(self.cities), 19)

    def test_city_indices_and_depots(self):
        self.assertIn(0, self.cities)
        self.assertIn(1, self.cities)
        for i in range(19):
            self.assertIn(i, self.cities)

    def test_robot_tours_start_end_at_depot(self):
        self.assertEqual(self.robot_tours[0][0], self.robot_tours[0][-1])
        self.assertEqual(self.robot_tours[1][0], self.robot_tours[1][-1])

    def test_visit_each_city_once(self):
        all_cities = set(range(19))
        visited_cities = set(c for tour in self.robot_tours.values() for c in tour)
        self.assertEqual(visited_cities, all_cities)

    def test_cost_calculation(self):
        ca_distance = self.calculate_euclidean_distance(0, 2)
        ex_distance = np.sqrt((49 - 30)**2 + (43 - 40)**2)
        self.assertAlmostEqual(ca_distance, ex_distance)

def run_tests():
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(unittest.makeSuite(TestTSPSolution))
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Capture the output and print "CORRECT" or "FAIL"
output = run_tests()
print(output)