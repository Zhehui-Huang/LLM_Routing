import unittest
from math import sqrt

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestVerifyTour(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
        self.total_travel_cost = 458.36719998557066
        self.maximum_distance = 68.15423684555495

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot")

    def test_visit_all_cities_exactly_once(self):
        visited_cities = sorted(set(self.tour[1:-1]))  # Exclude the first and last element (depot)
        self.assertListEqual(visited_cities, list(range(1, 20)), "Not visiting all cities exactly once")

    def test_travel_cost(self):
        calculated_cost = sum(calculate_distance(cities[self.tour[i]], cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.total_travel_cost, places=8, "Total calculated travel cost does not match")

    def test_maximum_distance(self):
        distances = [calculate_distance(cities[self.tour[i]], cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1)]
        calculated_max_distance = max(distances)
        self.assertAlmostEqual(calculated_max_distance, self.maximum_distance, places=8, "Maximum distance between consecutive cities is incorrect")

# Run unit tests
if __name__ == "__main__":
    unittest.main()