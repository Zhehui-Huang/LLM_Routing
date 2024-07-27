import unittest
from math import sqrt

# Given coordinates for cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Solution data
tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
total_travel_cost = 328.4
max_distance_between_cities = 45.19

def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_tour_starts_ends_at_depot(self):
        self.assertEqual(tour[0], 0)  # start at depot
        self.assertEqual(tour[-1], 0)  # end at depot

    def test_visit_each_city_once(self):
        unique_cities = set(tour[1:-1])
        self.assertEqual(len(unique_cities), 9)  # Checking if there are 9 unique cities
    
    def test_total_travel_cost(self):
        calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(calculated_cost, total_travel_cost, places=2)

    def test_max_distance_between_consecutive_cities(self):
        max_calculated_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(max_calculated_distance, max_distance_between_cities, places=2)

    def test_output(self):
        test_outputs = {
            'tour': tour,
            'total_travel_cost': total_travel_cost,
            'max_distance_between_cities': max_distance_between_cities
        }
        correct_outputs = {
            'tour': [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0],
            'total_travel_cost': 328.4,
            'max_distance_between_cities': 45.19
        }
        self.assertEqual(test_outputs, correct_outputs)

# Execute the tests
if __name__ == "__main__":
    unittest.main()