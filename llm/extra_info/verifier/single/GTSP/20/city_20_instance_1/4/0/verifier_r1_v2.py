import unittest
from math import sqrt

# Coordinates of cities (index corresponds to city number)
cities_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Define city groups
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Test tour and travel cost provided
test_tour = [0, 6, 13, 2, 9, 0]
test_total_travel_cost = 114.66

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y·2 = cities_coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestTourSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(test_tour[0], 0, "Tour should start at city 0.")
        self.assertEqual(test_tour[-1], 0, "Tour should end at city 0.")
        
    def test_one_city_from_each_group(self):
        included_groups = [False] * len(city_groups)
        for city in test_tour[1:-1]:
            for i, group in enumerate(city_groups):
                if city in group:
                    included_groups[i] = True
        self.assertTrue(all(included_groups), "Not all groups are represented exactly once in the tour.")
    
    def test_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(test_tour) - 1):
            calculated_cost += calculate_euclidean_distance(test_tour[i], test_tour[i+1])
        self.assertAlmostEqual(calculated_cost, test_total_travel_cost, delta=0.1, msg="Total travel cost does not match.")

if __name__ == '__main__':
    unittest.main()