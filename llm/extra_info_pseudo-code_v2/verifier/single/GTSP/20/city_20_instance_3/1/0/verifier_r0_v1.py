import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
            4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
            8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
            12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
            16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
        }
        self.groups = [
            [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15],
            [1, 3, 19], [8, 11, 18]
        ]
        self.solution_tour = [0, 4, 7, 12, 15, 3, 18, 0]
        self.expected_cost = 227.40

    def test_satisfaction_of_requirements(self):
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        # Test starting and ending at the depot
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

        # Test visiting one city from each group
        visited_groups = set()
        for city in self.solution_tour[1:-1]:  # exclude the depot at start and end
            for idx, group in enumerate(self.groups):
                if city in group:
                    visited_groups.add(idx)
        self.assertEqual(len(visited_groups), len(self.groups))
        
        # Test travel cost calculation
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            calculated_cost += euclidean_distance(self.cities[self.solution_tour[i]], 
                                                  self.cities[self.solution_tour[i + 1]])
        # Check the cost up to one decimal
        self.assertAlmostEqual(calculated_cost, self.expected_cost, places=1)

        # If all tests passed
        if self._outcome.success:
            print("CORRECT")
        else:
            print("FAIL")

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)