import unittest
from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

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
        # Validate start and end at depot
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

        # Validate one city from each group is visited
        visited_groups = [False] * len(self.groups)
        for city in self.solution_tour[1:-1]:
            for i, group in enumerate(self.groups):
                if city in group:
                    self.assertFalse(visited_groups[i], f"Group {i} already visited.")
                    visited_groups[i] = True
        self.assertTrue(all(visited_groups), "Not all groups were visited.")

        # Validate the travel cost
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            idx_from = self.solution_tour[i]
            idx_to = self.solution_tour[i + 1]
            calculated_cost += euclidean_distance(
                self.coordinates[idx_from][0], self.coordinates[idx_from][1],
                self.coordinates[idx_to][0], self.coordinates[idx_to][1]
            )
        self.assertAlmostEqual(calculated_cost, self.solution_cost, delta=0.01)

# Execute tests
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTourSolution)
    test_result = unittest.TextTestRunner().run(test_suite)

    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")