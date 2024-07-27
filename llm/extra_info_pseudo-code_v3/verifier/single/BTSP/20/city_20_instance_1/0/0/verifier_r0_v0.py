import unittest
import math
from typing import List, Tuple

def calculate_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

class TestBottleneckTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
            (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
            (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
            (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
        ]
        self.tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
        self.expected_total_cost = 477.0516251264448
        self.expected_max_distance = 87.45856161634491

    def test_tour_validity(self):
        # Check if all cities are visited exactly once and tour starts/ends at depot
        self.assertEqual(len(self.tour), len(set(self.tour)))
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_total_travel_cost(self):
        total_cost = sum(calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=5)

    def test_maximum_distance_between_consecutive_cities(self):
        max_distance = max(calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(max_distance, self.expected_max_stop_distance, places=5)

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestBottleneckTSPSolution)
    test_result = unittest.TextTestRunner().run(test_suite)
    output = "CORRECT" if test_result.wasSuccessful() else "FAIL"
    print(output)