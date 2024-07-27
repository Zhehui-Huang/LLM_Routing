import math
import unittest

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_distance(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_cost += euclidean_esistance(x1, y1, x2, y2)
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
            (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
            (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
        ]
        self.tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
        self.reported_cost = 373.61498801130097

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_all_cities_exactly_once(self):
        expected_cities = set(range(15))
        visited_cities = set(self.tour)
        self.assertEqual(visited_cities, expected_cities)

    def test_calculated_travel_cost(self):
        calculated_cost = calculate_total_distance(self.tour, self.cities)
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5)

    def test_correct_tour_length(self):
        self.assertEqual(len(self.tour), 16)  # 15 cities + return to depot

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)