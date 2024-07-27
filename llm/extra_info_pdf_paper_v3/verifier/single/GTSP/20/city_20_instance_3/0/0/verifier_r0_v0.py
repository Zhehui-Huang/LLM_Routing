import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

class TestGTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
            (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
            (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
        ]
        self.groups = [
            [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
        ]
        self.tour = [0, 4, 7, 12, 15, 3, 18, 0]
        self.total_cost = 227.40171050114

    def test_unique_cities(self):
        self.assertEqual(len(set(self.cities)), len(self.cities), "Cities are not unique")

    def test_group_integrity(self):
        total_cities_in_groups = sum(len(group) for group in self.groups)
        unique_cities_in_groups = len(set(city for group in self.groups for city in group))
        self.assertEqual(total_cities_in_groups, unique_cities_in_groups, "Cities in groups are not distinct")

    def test_robot_starts_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot")

    def test_visit_one_city_per_group(self):
        visited_groups = [False] * len(self.groups)
        for city in self.tour[1:-1]:
            for i, group in enumerate(self.groups):
                if city in group:
                    self.assertFalse(visited_groups[i], f"Multiple cities from group {i} visited")
                    visited_groups[i] = True
        self.assertTrue(all(visited_groups), "Not all groups were visited exactly once")

    def test_cost_accuracy(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5, msg="Total travel cost is incorrect")

    def test_solution_correctness(self):
        try:
            self.test_unique_cities()
            self.test_group_integrity()
            self.test_robot_starts_ends_at_depot()
            self.test_visit_one_city_per_group()
            self.test_cost_accuracy()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# To run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)