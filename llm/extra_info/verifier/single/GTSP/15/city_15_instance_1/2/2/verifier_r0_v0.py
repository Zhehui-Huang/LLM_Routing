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
        self.assertEqual(self.solution_tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.solution_tour[-1], 0, "Tour does not end at depot")

    def test_tour_visits_one_city_per_group(self):
        visited = set()
        for city in self.solution_tour[1:-1]:  # Exclude starting and ending depot
            in_group = False
            for group in self.groups:
                if city in group:
                    self.assertFalse(city in visited, "City is visited more than once")
                    visited.add(city)
                    in_group = True
                    break
            self.assertTrue(in_group, "City not in any group")
        self.assertEqual(len(visited), len(self.groups), "Visited cities count does not match groups count")

    def test_euclidean_distance_used(self):
        def distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        calculated_cost = sum(distance(self.solution_tour[i], self.solution_tour[i + 1]) for i in range(len(self.solution_tour) - 1))
        self.assertAlmostEqual(calculated. cost, self.solution_cost, places=2, "Reported travel cost is not accurate")

    def test_correctness_of_solution(self):
        result = "CORRECT" if all(
            self.test_tour_starts_and_ends_at_depot(),
            self.test_tour_visits_one_city_per_group(),
            self.test_euclidean_distance_used()
        ) else "FAIL"
        print(result)

if __name__ == '__main__':
    unittest.main()