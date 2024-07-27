import unittest
import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
            (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
            (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
        ]
        self.tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
        self.expected_total_cost = 373.61
        self.expected_max_distance = 94.11

    def test_tour_start_end_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_visit_each_city_once(self):
        tour_without_depot = self.tour[1:-1]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 14)
        for city in range(1, 15):
            self.assertIn(city, unique_cities)

    def test_max_distance(self):
        max_dist = max(
            distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            for i in range(len(self.tour) - 1)
        )
        self.assertAlmostEqual(max_dist, self.expected_max_distance, places=2)
    
    def test_total_cost(self):
        total_cost = sum(
            distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            for i in range(len(self.tour) - 1)
        )
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)