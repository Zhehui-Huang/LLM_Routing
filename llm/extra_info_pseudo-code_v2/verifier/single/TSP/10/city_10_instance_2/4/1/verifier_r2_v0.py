import unittest
from math import sqrt

# Provided cities data
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Provided solution
tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
reported_cost = 384.7863591860825

def calculate_distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def calculate_total_cost(tour, cities):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_cities_visited_exactly_once(self):
        visited = tour[1:-1]  # Remove the starting and ending depot city
        expected = list(range(1, 10))
        self.assertEqual(sorted(visited), expected)

    def test_calculated_travel_cost(self):
        calculated_cost = calculate_total_cost(tour, cities)
        # Allow a small numerical tolerance
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5)

    def test_output_format(self):
        self.assertIsInstance(tour, list)
        for city in tour:
            self.assertIsInstance(city, int)
        self.assertIsInstance(reported_cost, float)

# Execution of unit tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)