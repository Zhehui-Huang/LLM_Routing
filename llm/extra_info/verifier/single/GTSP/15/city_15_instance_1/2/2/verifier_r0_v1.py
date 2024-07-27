import math
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
            (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
            (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
        ]
        self.groups = [
            [1, 2, 5, 6],
            [8, 9, 10, 13],
            [3, 4, 7],
            [11, 12, 14]
        ]
        self.solution_tour = [0, 5, 10, 4, 11, 0]
        self.solution_cost = 184.24

    def test_tour_starts_and_ends_at_depot(self):
        # Check if tour starts and ends at city 0
        self.assertEqual(self.solution_tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.solution_tour[-1], 0, "Tour does not end at depot")

    def test_tour_visits_one_city_per_group(self):
        # Check if exactly one city from each group is visited
        visited = set()
        for city in self.solution_tour[1:-1]:
            for group in self.groups:
                if city in group:
                    visited.add(tuple(group))  # Add group as a tuple to track visited groups
                    break
        self.assertEqual(len(visited), len(self.groups), "Not all groups are visited exactly once")

    def test_euclidean_distance_used(self):
        # Calculate distance using Euclidean formula and compare with given solution cost
        def distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        calculated_cost = sum(distance(self.solution_tour[i], self.solution_tour[i + 1]) for i in range(len(self.solution_tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.solution_cost, places=2, msg="Reported travel cost is not accurate")

if __name__ == "__main__":
    unittest.main()