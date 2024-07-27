import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69)
        }

        self.solutions = {
            0: ([0, 9, 13, 0], 68.39),
            1: ([0, 12, 15, 0], 66.12),
            2: ([0, 6, 0], 24.08),
            3: ([0, 4, 11, 0], 57.39),
            4: ([0, 5, 14, 0], 62.44),
            5: ([0, 3, 8, 0], 72.82),
            6: ([0, 1, 10, 0], 41.77),
            7: ([0, 2, 7, 0], 51.59)
        }

    def test_unique_visits(self):
        visited = sum((tour[1:-1] for _, (tour, _) in self.solutions.items()), [])
        self.assertCountEqual(visited, list(range(1, 16)))  # Include city indices 1 to 15, exclude the depot.

    def test_start_end_depot(self):
        for tour, _ in self.solutions.values():
            self.assertEqual(tour[0], 0)  # Start at depot
            self.assertEqual(tour[-1], 0)  # End at depot

    def test_total_cost_calculation(self):
        for tour, declared_cost in self.solutions.items():
            calculated_cost = sum(math.sqrt((self.cities[tour[i]][0] - self.cities[tour[i + 1]][0])**2 +
                                            (self.cities[tour[i]][1] - self.cities[tour[i + 1]][1])**2)
                                  for i in range(len(tour) - 1))
            self.assertAlmostEqual(calculated_cost, declared_cost, places=2)

    def test_overall_total_cost(self):
        total_cost = sum(cost for _, cost in self.solutions.values())
        self.assertAlmostEqual(total_cost, 444.62, places=2)  # Check if total is close to the given total

if __name__ == '__main__':
    unittest.main()