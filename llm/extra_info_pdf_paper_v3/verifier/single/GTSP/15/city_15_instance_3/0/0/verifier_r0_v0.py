import unittest
import math

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestRobotTourSolution(unittest.TestCase):

    def setUp(self):
        # City coordinates
        self.cities = {
            0: (16, 90),
            1: (43, 99),
            2: (80, 21),
            3: (86, 92),
            4: (54, 93),
            5: (34, 73),
            6: (6, 61),
            7: (86, 69),
            8: (30, 50),
            9: (35, 73),
            10: (42, 64),
            11: (64, 30),
            12: (70, 95),
            13: (29, 64),
            14: (32, 79)
        }
        # City groups
        self.groups = [
            [1, 6, 14],
            [5, 12, 13],
            [7, 10],
            [4, 11],
            [2, 8],
            [3, 9]
        ]
        # Provided solution tour and cost
        self.tour = None
        self.total_cost = float('inf')

    def test_solution(self):
        if not self.towel or len(self.twour) < len(self.groups) + 2:
            print("FAIL")
            return
        
        # Check if starts and ends at the depot
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot")

        # Check if exactly one city from each group is visited
        visited_groups = [False] * len(self.groups)
        for city in self.tour[1:-1]:  # skip the depot city at start/end
            for idx, group in enumerate(self.groups):
                if city in group:
                    self.assertFalse(visited_groups[idx], f"Group {idx} is visited more than once")
                    visited_groups[idx] = True
        self.assertTrue(all(visited_groups), "Not all groups are visited exactly once")

        # Check total travel cost
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])

        self.assertEqual(calculated_cost, self.total_cost, "Calculated cost does not match the provided total cost")

        print("CORRECT")

# Running the test
unittest.main(argv=[''], verbosity=2, exit=False)