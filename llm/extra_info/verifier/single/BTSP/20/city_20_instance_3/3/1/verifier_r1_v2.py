import unittest
import math

# Coordinates for each city, including the depot
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    
    def test_tour_start_and_end_at_depot(self):
        tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
    
    def test_visit_each_city_once_except_depot(self):
        tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        unique_cities_set = set(tour)
        all_cities_set = set(range(20))
        self.assertEqual(unique_cities_set, all_cities_set)
        self.assertEqual(tour.count(0), 2)
        for i in range(1, 20):
            self.assertEqual(tour.count(i), 1)
    
    def test_optimize_longest_consecutive_distance(self):
        tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        submitted_max_distance = 128.81770064707723
        calculated_distances = [euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1)]
        calculated_max_distance = max(calculated_distances)
        self.assertAlmostEqual(calculated_max_distance, submitted_max_distance, delta=0.001)
        
# Executing the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)