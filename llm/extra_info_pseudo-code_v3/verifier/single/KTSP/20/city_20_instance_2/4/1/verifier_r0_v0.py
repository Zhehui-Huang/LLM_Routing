import numpy as np
import unittest

class TestTravelingRobot(unittest.TestCase):
    def setUp(self):
        # Define city coordinates as given in the original problem
        self.cities = {
            0: (3, 26),
            1: (85, 72),
            2: (67, 0),
            3: (50, 99),
            4: (61, 89),
            5: (91, 56),
            6: (2, 65),
            7: (38, 68),
            8: (3, 92),
            9: (59, 8),
            10: (30, 88),
            11: (30, 53),
            12: (11, 14),
            13: (52, 49),
            14: (18, 49),
            15: (64, 41),
            16: (28, 49),
            17: (91, 94),
            18: (51, 58),
            19: (30, 48)
        }
        self.tour = [0, 7, 3, 4, 1, 15, 13, 18, 19, 16, 0]
        self.reported_cost = 252.57716996890326

    def test_tour_length(self):
        # Requirement 1: Check if exactly 10 cities are visited (including the depot)
        self.assertEqual(len(set(self.tour)), 10)

    def test_tour_loop(self):
        # Requirement 2: Check if the tour starts and ends at the depot city (city index 0)
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_cost(self):
        # Requirement 3: Calculate the traveled distance and compare with the reported cost.
        def calculate_distance(city_a, city_b):
            return np.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])

        # Checking the total calculated cost with a small allowance for floating point arithmetic issues
        self.assertAlmostEqual(total_cost, self.reported_cost, places=4)

unittest.main(argv=[''], exit=False)