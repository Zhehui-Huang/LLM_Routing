import unittest
import math

# Define the input of cities coordinates with depot as index 0
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Given solution
tour = [0, 12, 14, 16, 11, 7, 18, 15, 13, 19, 0]
given_total_cost = 190.66  # The actual given value should be a float rounded to two decimal places

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return round(total_cost, 2)

class TestRobotTour(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_tour_length(self):
        # Should visit 10 cities including the depot
        self.assertEqual(len(set(tour)), 10)

    def test_travel_between_any_cities(self):
        # Implicitly true by functionality, this ensures that each city pair is valid
        all_cities = cities.keys() 
        for i in tour:
            self.assertIn(i, all_cities)

    def test_calculated_cost(self):
        total_cost = calculate_total_cost(tour)
        self.assertEqual(total_cost, given_total_cost)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)