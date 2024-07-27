import unittest
from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
            (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
            (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
            (50, 28), (69, 9)
        ]
        self.groups = [
            [5, 6, 7, 11, 17], [1, 4, 8, 13, 16], [2, 10, 15, 18, 19], [3, 9, 12, 14]
        ]
        self.solution_tour = [0, 2, 1, 5, 3, 0]
        self.solution_cost = 173.47

    def test_solution(self):
        # Check that the tour starts and ends at the depot city 0
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

        # Check that exactly one city from each group is visited
        groups_visited = [False] * len(self.groups)
        for city in self.solution_tour[1:-1]:  # Ignore the depot city at start/end
            for index, group in enumerate(self.groups):
                if city in group:
                    self.assertFalse(groups_visited[index], f"Group {index} visited more than once.")
                    groups_visited[index] = True
        self.assertTrue(all(groups_visited), "Not all groups are visited.")

        # Check the total travel cost calculation
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            city_from = self.solution_tour[i]
            city_to = self.solution_tour[i + 1]
            x1, y1 = self.coordinates[city_from]
            x2, y2 = self.coordinates[city_to]
            calculated_cost += euclidean_distance(x1, y1, x2, y2)
        self.assertAlmostEqual(calculated_cost, self.solution_cost, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)