import unittest
from math import sqrt

class TestTravelingSalesmanProblem(unittest.TestCase):
    def test_solution(self):
        # Provided tour and cost
        proposed_tour = [0, 11, 16, 18, 19, 6, 0]
        proposed_cost = 162.3829840233368

        # City coordinates
        city_coords = [
            (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
            (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
            (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
        ]

        # City groups
        city_groups = [
            [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18],
            [1, 9, 14, 19], [5, 6, 17]
        ]

        def calculate_euclidean_distance(city1, city2):
            return sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

        # Check Requirement 3: Starts and ends at depot
        self.assertEqual(proposed_tour[0], 0)  # start at depot
        self.assertEqual(proposed_tour[-1], 0)  # end at depot

        # Check Requirement 4: Visit exactly one from each group
        visited_groups = [False] * len(city_groups)
        for city in proposed_tour[1:-1]:  # Exclude the depot at the beginning and end
            for i, group in enumerate(city_groups):
                if city in group:
                    self.assertFalse(visited_groups[i])  # City not yet visited from this group
                    visited_groups[i] = True
        self.assertTrue(all(visited_groups))  # All groups were visited

        # Check Requirement 5 & 8: Correct travel cost calculation
        calculated_cost = 0
        for i in range(len(proposed_tour) - 1):
            calculated_cost += calculate_euclidean_distance(proposed_tour[i], proposed_tour[i + 1])

        self.assertAlmostEqual(proposed_cost, calculated_cost, places=5)

        # Check Requirement 7 & 9: Output format and direct travel possibility
        self.assertTrue(isinstance(proposed_tour, list))
        self.assertIsInstance(proposed_cost, float)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)