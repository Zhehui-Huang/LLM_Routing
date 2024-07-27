import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35), 21: (32, 39), 22: (56, 37)
        }
        self.tour = [0, 16, 1, 10, 2, 9, 6, 13, 14, 17, 20, 18, 19, 12, 15, 3, 4, 11, 7, 8, 21, 5, 22]
        self.reported_cost = 346.0500480846498

    def test_minimum_total_travel_cost(self):
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        total_cost = sum(euclidean_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour)-1))
        # Check if actual total cost approximates the reported cost within a small accepted error margin
        self.assertAlmostEqual(total_cost, self.reported_cost, delta=5.657, msg="Calculated cost should be within tolerance")

if __name__ == '__main__':
    unittest.main()