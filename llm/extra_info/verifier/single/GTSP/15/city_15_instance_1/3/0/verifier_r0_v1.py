import unittest
from math import sqrt

# Coordinates for each city
cities_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Groups of cities
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

def euclidean_distance(city1, city2):
    # Correct formula usage
    return sqrt((cities_coordinates[city1][0] - cities_coordinates[city2][0]) ** 2 +
                (cities_coordinates[city1][1] - cities_coordinates[city2][1]) ** 2)

def calculate_total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

class TestTSPSolution(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        tour = [0, 5, 10, 4, 11, 0]
        self.assertEqual(tour[0], 0, "Tour should start at the depot")
        self.assertEqual(tour[-1], 0, "Tour should end at the depot")

    def test_visit_one_city_per_group(self):
        tour = [0, 5, 10, 4, 11, 0]
        visited_from_group = [0] * len(city_groups)
        for city in tour[1:-1]:  # Exclude the depot city at start and end
            for group_index, group in enumerate(city_groups):
                if city in group:
                    visited_from_group[group_index] += 1

        self.assertTrue(all(count == 1 for count in visited_from_group),
                        "Should visit exactly one city from each group")

    def test_total_travel_cost(self):
        tour = [0, 5, 10, 4, 11, 0]
        expected_cost = 184.24203302868492
        calculated_cost = calculate_total_tour_cost(tour)
        self.assertAlmostEqual(calculated_cost, expected_cost, places=4, msg="Calculated cost is incorrect")

if __name__ == '__main__':
    unittest.main()