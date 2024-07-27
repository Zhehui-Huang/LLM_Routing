import math
import unittest

# Input data for cities with their coordinates
city_coordinates = {
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
tour = [0, 12, 16, 14, 11, 7, 3, 10, 18, 13, 0]
reported_cost = 248.8529597536688

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_total_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(
            city_coordinates[tour[i]],
            city_coordinates[tour[i + 1]]
        )
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visit_exactly_10_cities(self):
        self.assertEqual(len(set(tour)), 10)

    def test_tour_covers_only_existing_cities(self):
        all_cities = set(city_coordinates.keys())
        self.assertTrue(set(tour).issubset(all_cities))

    def test_correct_travel_cost_calculation(self):
        calculated_cost = calculate_total_cost(tour, city_coordinates)
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5)

    def test_solution_city_indices(self):
        for index in tour:
            self.assertIn(index, city_coordinates)

if __name__ == "__main__":
    test_suite = unittest.TestSuite(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()

    result = runner.run(test_suite)
    
    # Check if any test failed
    if result.failures or result.errors:
        print("FAIL")
    else:
        print("CORRECT")