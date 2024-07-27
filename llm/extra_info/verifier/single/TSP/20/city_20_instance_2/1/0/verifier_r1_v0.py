import unittest
from math import sqrt

# Coordinates of cities including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Provided solution
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
claimed_total_cost = 478.43

def calculate_two_cities_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        self.assertEqual(tour[0], 0, "Tour does not start at the depot")
        self.assertEqual(tour[-1], 0, "Tour does not end at the depot")

    def test_visit_each_city_once(self):
        city_count = len(cities)
        visited = tour[1:-1]
        self.assertEqual(len(visited), city_count - 1, "Tour length mismatch, not all cities are visited exactly once")
        self.assertEqual(len(set(visited)), city_count - 1, "Not all cities are visited exactly once")

    def test_total_travel_cost(self):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_two_cities_item_countdstance(cities[tour[i]], cities[tour[i+1]])
        self.assertAlmostEqual(total_cost, claimed_total_cost, places=2, msg="Total travel cost is different from claimed")

if __name__ == "__main__":
    # Run the tests
    unittest.main()