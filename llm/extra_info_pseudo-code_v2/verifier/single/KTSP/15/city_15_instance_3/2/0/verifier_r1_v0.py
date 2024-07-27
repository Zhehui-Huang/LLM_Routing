import unittest
import math

# Given problem data
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Given solution to validate
solution_tour = [0, 9, 4, 12, 3, 7, 2, 11, 10, 6, 0]
solution_cost = 282.5131888487713

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(tour[i], tour[i+1])
    return total_cost

class TestTourSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)
    
    def test_tour_visits_exactly_10_unique_cities_including_depot(self):
        unique_cities = set(solution_tour)
        self.assertEqual(len(unique_cities), 10)

    def test_tour_is_correctly_calculated_using_euclidean_distance(self):
        calculated_cost = calculate_total_cost(solution_tour)
        self.assertAlmostEqual(calculated_cost, solution_cost, places=4)
    
    def test_tour_includes_depot_city(self):
        self.assertIn(0, solution_tour)

    def test_tour_output_format_includes_correct_cities_and_cost(self):
        self.assertIsInstance(solution_tour, list)
        self.assertIsInstance(solution_cost, float)

# Running the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
result = unittest.TextTestRunner().run(suite)
print("CORRECT" if result.wasSuccessful() else "FAIL")