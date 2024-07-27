import unittest
import math

# City Coordinates
cities = [
    (8, 11),  # City 0 - Depot
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

# Provided solution details
tour = [0, 1, 5, 13, 17, 8, 19, 2, 6, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 4, 0]
provided_cost = 374.97
provided_max_distance = 32.39

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTourSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_all_cities_visited_once(self):
        self.assertEqual(len(set(tour[:-1])), len(cities))  # Exclude last city as it's the repeat of the first

    def test_max_distance_between_consecutive_cities(self):
        max_distance = 0
        for i in range(len(tour) - 1):
            city1, city2 = cities[tour[i]], cities[tour[i+1]]
            distance = calculate_euclidean_distance(city1, city2)
            if distance > max_distance:
                max_distance = distance
        self.assertAlmostEqual(max_distance, provided_max_distance, delta=0.01)

    def test_total_travel_cost(self):
        total_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = cities[tour[i]], cities[tour[i+1]]
            total_cost += calculate_euclidean_distance(city1, city2)
        self.assertAlmostEqual(total_cost, provided_cost, delta=0.01)

# Run the test suite
if __name__ == '__main__':
    unittest.main()