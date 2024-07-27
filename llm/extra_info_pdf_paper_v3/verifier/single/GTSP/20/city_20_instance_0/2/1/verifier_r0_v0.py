import unittest
import math

# Provided cities coordinates
cities = {
    0: (8, 11),   # Depot
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Groups declarations
group_0 = [1, 3, 5, 11, 13, 14, 19]
group_1 = [2, 6, 7, 8, 12, 15]
group_2 = [4, 9, 10, 16, 17, 18]

def calculate_euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_total_distance(tour):
    """ Calculate total distance for the tour """
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_euclidean_distance(tour[i], tour[i + 1])
    return total_distance

class TestTourSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        tour = [0, 1, 8, 4, 0]
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visit_one_city_from_each_group(self):
        tour = [0, 1, 8, 4, 0]
        group_0_visited = any(city in tour for city in group_0)
        group_1_visited = any(city in tour for city in group_1)
        group_2_visited = any(city in tour for city in group_2)
        self.assertTrue(group_0_visited)
        self.assertTrue(group_1_visited)
        self.assertTrue(group_2_visited)

    def test_euclidean_distance_calculation(self):
        tour = [0, 1, 8, 4, 0]
        given_total_cost = 110.09
        calculated_total_cost = round(calculate_total_distance(tour), 2)
        self.assertAlmostEqual(calculated_total_cost, given_total_cost)

    def test_output_format(self):
        tour = [0, 1, 8, 4, 0]
        given_total_cost = 110.09
        self.assertIsInstance(tour, list)
        self.assertIsInstance(given_total_cost, float)
        self.assertEqual(len(tour), 5)  # including start and end at depot

if __name__ == "__main__":
    results = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTourSolution))
    print("CORRECT" if len(results.failures) == 0 and len(results.errors) == 0 else "FAIL")