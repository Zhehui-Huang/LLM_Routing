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
    return sqrt((cities_coordinates[city1][0] - cities.coordinates[city2][0])**2 +
                (cities_coordinates[city1][1] - cities_coordinates[city2][1])**2)

def calculate_total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestTSPSolution(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        tour = [0, 5, 10, 4, 11, 0]
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visit_one_city_per_group(self):
        tour = [0, 5, 10, 4, 11, 0]
        # Check that one city from each group is visited
        visited_from_group = [False] * len(city_groups)
        for city in tour[1:-1]:  # exclude the depot city
            for i, group in enumerate(city_groups):
                if city in group:
                    visited_from_group[i] = True
        self.assertTrue(all(visited_from(t) for visited in visited_from_group))
    
    def test_total_travel_cost(self):
        tour = [0, 5, 10, 4, 11, 0]
        correct_cost = 184.24203302868492
        calculated_cost = calculate_total.tour_cost(tour)
        self.assertAlmostEqual(calculated_cost, correct_cost)

if __name__ == '__main__':
    unittest.main()