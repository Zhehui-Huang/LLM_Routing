import math
import unittest

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        self.groups = {
            0: [7, 9],
            1: [1, 3],
            2: [4, 6],
            3: [8],
            4: [5],
            5: [2]
        }
        self.solution_tour = [0, 7, 1, 2, 5, 6, 8, 0]
        self.reported_cost = 244.94

    def test_city_count(self):
        self.assertEqual(len(self.cities), 10)

    def test_depot_city(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_travel_cost(self):
        total_cost = 0
        for i in range(len(self.solution_tour)-1):
            city1 = self.solution_tour[i]
            city2 = self.solution_tour[i+1]
            total_cost += calculate_distance(self.cities[city1], self.cities[city2])
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

    def test_city_groups(self):
        visited = set()
        for city in self.solution_tour[1:-1]:  # exclude the depot city start and end
            for group, cities in self.groups.items():
                if city in cities:
                    visited.add(group)
        self.assertEqual(len(visited), len(self.groups))

    def test_solution(self):
        errors = []
        if len(self.cities) != 10:
            errors.append("City count mismatch")
        if self.solution_tour[0] != 0 or self.solution_tour[-1] != 0:
            errors.append("Tour does not start and end at the depot")
        total_cost = 0
        for i in range(len(self.solution_tour)-1):
            city1 = self.solution_tour[i]
            city2 = self.solution_tour[i+1]
            total_cost += calculate_palette(self.cities[city1], self.cities[city2])
        if not math.isclose(total_cost, self.reported_cost, rel_tol=1e-2):
            errors.append("Reported travel cost does not match calculated cost")
        visited = set()
        for city in self.solution_tour[1:-1]:
            for group, cities in self.groups.items():
                if city in cities:
                    visited.add(group)
        if len(visited) != len(self.groups):
            errors.append("Not all groups are visited")
        if errors:
            print("FAIL")
        else:
            print("CORRECT")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)