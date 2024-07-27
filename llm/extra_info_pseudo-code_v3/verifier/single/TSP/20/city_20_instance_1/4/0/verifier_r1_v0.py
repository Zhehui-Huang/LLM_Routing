import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Provided solution tour and cost
        tour = [0, 6, 2, 19, 15, 18, 17, 12, 13, 8, 9, 11, 10, 16, 4, 7, 5, 14, 3, 1, 0]
        cost = 610.8605077173856

        # Given cities coordinates
        cities = {
            0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84), 6: (4, 56),
            7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29),
            14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
        }

        # [Requirement 1] Start and end at the depot city 0
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # [Requirement 2] Visit each city exactly once, except depot
        self.assertCountEqual(tour[1:-1], list(range(1, 20)))

        # [Requirement 3] Travel cost using Euclidean distance
        calculated_cost = 0
        for i in range(len(tour) - 1):
            x1, y1 = cities[tour[i]]
            x2, y2 = cities[tour[i + 1]]
            calculated_cost += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(calculated_cost, cost, places=5)

        # Final check [Requirement 4, 5] cannot be explicitly verified since they involve algorithmic and output specifics
        # The test assumes correct implementation; focusing on result verification from algorithm

if __name__ == "__main__":
    result = unittest.main(argv=[''], exit=False)
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")