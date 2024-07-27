import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.positions = [
            (35, 40),  # Depot
            (39, 41),
            (81, 30),
            (5, 50),
            (72, 90),
            (54, 46),
            (8, 70),
            (97, 62),
            (14, 41),
            (70, 44),
            (27, 47),
            (41, 74),
            (53, 80),
            (21, 21),
            (12, 39)
        ]
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.reported_cost = 337.84

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot")

    def test_all_cities_visited_exactly_once(self):
        tour_without_depot = self.tour[1:-1]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 14, "Not all cities are visited exactly once")

    def test_calculate_total_travel_cost(self):
        calculated_cost = self.calculate_total_distance(self.tour)
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2, msg="Calculated cost does not match reported cost")

    def calculate_distance(self, pos1, pos2):
        return sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

    def calculate_total_distance(self, tour):
        total_distance = 0
        for i in range(len(tour) - 1):
            pos1, pos2 = self.positions[tour[i]], self.positions[tour[i + 1]]
            total_distance += self.calculate_distance(pos1, pos2)
        return total_distance

# Activate the test
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)