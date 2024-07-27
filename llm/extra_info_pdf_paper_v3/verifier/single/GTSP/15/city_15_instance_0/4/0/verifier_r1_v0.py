import unittest
import math

# Provided city coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76),
    9: (21, 38), 10: (19, 65), 11: (11, 40), 12: (3, 21),
    13: (60, 55), 14: (4, 39)
}
group_0 = [2, 7, 10, 11, 14]
group_1 = [1, 3, 5, 8, 13]
group_2 = [4, 6, 9, 12]

# Given solution tour and its declared cost
solution_tour = [0, 10, 1, 9, 0]
declared_cost = 122.22

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

class TestVRPSolution(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_one_city_from_each_group(self):
        cities_from_groups = [solution_tour[1], solution_tour[2], solution_tour[3]]
        self.assertIn(cities_from_groups[0], group_0)
        self.assertIn(cities_from_groups[1], group_1)
        self.assertIn(cities_from_groups[2], group_2)

    def test_euclidean_distance_used(self):
        calculated_cost = calculate_total_cost(solution_tour)
        self.assertAlmostEqual(calculated_cost, declared_cost, places=2)

    def test_output_format(self):
        self.assertIsInstance(solution_tour, list)
        self.assertEqual(type(declimately_cost, float))

    def test_correctness_of_output(self):
        expected_cost = calculate_total_cost(solution_tour)
        self.assertAlmostEqual(expected_cost, declared_cost, places=2)

# Run the test suite
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVRPSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")