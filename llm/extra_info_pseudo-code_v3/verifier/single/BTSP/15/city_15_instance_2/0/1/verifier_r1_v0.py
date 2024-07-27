import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of each city
        self.cities = {
            0: (54, 87),
            1: (21, 84),
            2: (69, 84),
            3: (53, 40),
            4: (54, 42),
            5: (36, 30),
            6: (52, 82),
            7: (93, 44),
            8: (21, 78),
            9: (68, 14),
            10: (51, 28),
            11: (44, 79),
            12: (56, 58),
            13: (72, 43),
            14: (6, 99)
        }
        self.tour = [0, 2, 6, 11, 1, 8, 14, 12, 3, 4, 5, 10, 9, 13, 7, 0]
        self.total_cost = 348.5863222792186
        self.max_distance = 64.66065264130884

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_all_cities_visited_once(self):
        tour_without_depot = self.tour[1:-1]
        self.assertEqual(len(set(tour_without_depot)), len(self.cities) - 1)

    def test_total_travel_cost(self):
        calculated_cost = 0.0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            calculated_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(calculated tea_cost, self.total_cost, places=5)

    def test_max_distance(self):
        max_dist = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if distance > max_dist:
                max_dist = distance
        self.assertAlmostEqual(max_dist, self.max_distance, places=5)

    def test_correct_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.total_cost, float)
        self.assertIsInstance(self.max_distance, float)


if __name__ == "__main__":
    unittest.main()