import unittest
from math import sqrt

class TestKTSPSolution(unittest.TestCase):

    def setUp(self):
        self.cities = {
            0: (54, 87), 1: (21, 84),  2: (69, 84),  3: (53, 40),
            4: (54, 42),  5: (36, 30),  6: (52, 82),  7: (93, 44),
            8: (21, 78),  9: (68, 14), 10: (51, 28), 11: (44, 79),
            12: (56, 58), 13: (72, 43), 14: (6, 99)
        }
        self.solution_tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
        self.reported_cost = 132.1185774560832

    def test_start_and_end_at_depot(self):
        # Test if the tour starts and ends at the depot
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_exactly_eight_cities_visited(self):
        # Test if exactly 8 cities are visited
        self.assertEqual(len(set(self.solution_tour)), 8)

    def test_correct_computation_of_travel_cost(self):
        # Calculate the Euclidean distance and compare with reported cost
        def euclidean_distance(city1, city2):
            return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        total_cost = 0
        for i in range(len(self.solution_tour) - 1):
            city_index_1 = self.solution_tour[i]
            city_index_2 = self.solution_tour[i + 1]
            total_cost += euclidean_distance(self.cities[city_index_1], self.cities[city_index_2])

        self.assertAlmostEqual(total_cost, self.reported_cost, places=5)

    def test_solution_covers_required_cities(self):
        # Test fit to task's requirement of visiting 8 unique cities including depot.
        self.assertTrue(all(city in self.solution_tour for city in [0, 2, 13, 3, 4, 12, 11, 6]))

# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)