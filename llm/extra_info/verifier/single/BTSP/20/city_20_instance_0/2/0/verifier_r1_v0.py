import math
import unittest

# Cities coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Provided tour information
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.1974047195548
max_distance = 32.38826948140329

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_valid_tour(tour, n):
    return sorted(tour) == [0] + sorted(range(1, n))

def calculate_total_travel_cost(tour):
    return sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_max_distance(tour):
    return max(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestRobotTour(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visit_each_city_once(self):
        self.assertTrue(is_valid_tour(tour, len(cities)))

    def test_travel_cost_calculation(self):
        calculated_cost = calculate_total_travel_cost(tour)
        self.assertAlmostEqual(calculated_cost, total_travel_cost, places=5)

    def test_max_distance_between_cities(self):
        calculated_max_distance = find_max_distance(tour)
        self.assertAlmostEqual(calculated_max_distance, max_distance, places=5)

# Run the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
unittest.TextTestRunner().run(suite)