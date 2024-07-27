import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
            5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
            10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
        }
        self.tour = [0, 6, 13, 10, 9, 5, 14, 8, 11, 2, 7, 3, 12, 4, 1, 0]
        self.reported_cost = 293.15958883368387
    
    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot.")
    
    def test_visits_each_city_once(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 15, "Each city must be visited exactly once, excluding repeats of the depot.")
    
    def test_total_travel_cost(self):
        total_cost = 0
        for i in range(1, len(self.tour)):
            x1, y1 = self.cities[self.tour[i-1]]
            x2, y2 = self.cities[self.tour[i]]
            total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, msg="Calculated cost does not match reported cost.")
    
    def test_correct_output_format(self):
        self.assertIsInstance(self.tour, list, "Tour should be a list")
        self.assertIsInstance(self.reported_cost, float, "Total cost should be a float")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)