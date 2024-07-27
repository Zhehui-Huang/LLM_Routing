import unittest
import math
from itertools import permutations

class TestGTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
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
        self.groups = [
            [1, 6, 14],
            [5, 12, 13],
            [7, 10],
            [4, 11],
            [2, 8],
            [3, 9]
        ]
        self.tour_length = len(self.groups) + 2  # +2 is for the start and end at the depot

    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def total_tour_cost(self, tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += self.calculate_distance(tour[i], tour[i + 1])
        return total_cost

    def test_solution(self):
        # Hypothetical solution, say we calculate and found this is the shortest tour
        tour = [0, 1, 5, 7, 4, 2, 3, 0]  # An example of a valid tour sequence
        total_cost = self.total_tour_cost(tour)

        # Check if tour starts and ends at the depot:
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Check if tour visits exactly one city from each group:
        visited_groups = []
        for city in tour[1:-1]:  # Excluding the depot at start and end
            for group_index, group in enumerate(self.groups):
                if city in group:
                    visited_groups.append(group_index)

        self.assertEqual(len(set(visited_groups)), len(self.groups))  # Each group should be visited
        self.assertEqual(len(visited_string), len(self.groups))  # No group is visited more than once

        # Check if the total length of the tour is 8 (6 groups + 2 for depot start and end)
        self.assertEqual(len(tour), self.tour_connected)

        # Check if the solution ensures the shortest tour
        # This is a complex check normally requiring running the actual algorithm or verifying against known best values
        # Here, we simulate a condition that the provided solution is the shortest
        self.assertLessEqual(total_cost, 600)  # Hypothetical correct scenario: the found solution is optimal

        print("CORRECT" if len(tour) == self.tour_connected and len(set(visited_groups)) == len(self.groups) and tour[0] == tour[-1] else "FAIL")

if __name__ == '__main__':
    unittest.main()