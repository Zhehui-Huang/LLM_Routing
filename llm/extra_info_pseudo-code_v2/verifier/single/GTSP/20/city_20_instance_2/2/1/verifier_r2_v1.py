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

    def test_correctness_of_solution(self):
        # Test start and end at depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
        # Test visiting exactly one city from each group
        visited_groups = {}
        for city in self.tour[1:-1]:
            for idx, group in enumerate(self.groups):
                if city in group:
                    visited_groups[idx] = visited_groups.get(idx, 0) + 1
        self.assertTrue(all(v == 1 for v in visited_groups.values()))
        self.assertEqual(len(visited_groups), len(self.groups))
        
        # Calculate and validate travel cost
        travel_cost = sum(self.calculate_euclidean_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(travel_cost, self.provided_cost, places=5)
        
        # Ensure all checks are passed
        self.assertTrue(all(v == 1 for v in visited_groups.values()) and
                        len(visited_groups) == len(self.groups) and
                        math.isclose(travel_cost, self.provided_cost, abs_tol=1e-5) and
                        self.tour[0] == 0 and self.tour[-1] == 0)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTourSolution('test_correctness_of_solution'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    correct = result.wasSuccessful()
    if correct:
        print("CORRECT")
    else:
        print("FAIL")

run_tests()