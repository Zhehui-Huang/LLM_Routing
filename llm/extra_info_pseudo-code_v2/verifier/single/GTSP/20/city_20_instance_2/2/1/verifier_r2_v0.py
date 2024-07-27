import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # City Coordinates given in the description
        self.cities = {
            0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
            5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
            10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
            15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
        }
        # City groups
        self.groups = [
            [7, 10, 11, 12],
            [3, 8, 13, 16],
            [2, 4, 15, 18],
            [1, 9, 14, 19],
            [5, 6, 17]
        ]
        # Tour provided in the solution
        self.tour = [0, 11, 16, 18, 19, 6, 0]
        # Total provided travel cost
        self.provided_cost = 162.3829840233368

    def calculate_euclidean_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_robot_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_robot_visits_one_city_from_each_group(self):
        visited = set()
        for i in self.tour[1:-1]:  # Ignoring the start (0) and end (0)
            for j, group in enumerate(self.groups):
                if i in group:
                    visited.add(j)
        self.assertEqual(len(visited), len(self.groups))

    def test_travel_cost_calculation(self):
        calculated_cost = sum(self.calculate_euclidean_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.provided_cost, places=5)

    def test_output_tour_and_cost(self):
        result = "CORRECT" if self.provided_cost == sum(self.calculate_euclidean_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1)) and len(self.tour) == 7 and len({*self.tour}) == 6 else "FAIL"
        self.assertEqual(result, "CORRECT")

if __name__ == '__main__':
    unittest.main()