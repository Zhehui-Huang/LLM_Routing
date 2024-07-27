import unittest
import math

class TestRobotTourSolution(unittest.TestCase):
    
    def setUp(self):
        # City coordinates
        self.cities = [
            (16, 90),  # Depot city 0
            (43, 99),  # City 1
            (80, 21),  # City 2
            (86, 92),  # City 3
            (54, 93),  # City 4
            (34, 73),  # City 5
            (6, 61),   # City 6
            (86, 69),  # City 7
            (30, 50),  # City 8
            (35, 73),  # City 9
            (42, 64),  # City 10
            (64, 30),  # City 11
            (70, 95),  # City 12
            (29, 64),  # City 13
            (32, 79)   # City 14
        ]
        # City groups
        self.groups = [
            [1, 6, 14],  # Group 0
            [5, 12, 13], # Group 1
            [7, 10],     # Group 2
            [4, 11],     # Group 3
            [2, 8],      # Group 4
            [3, 9]       # Group 5
        ]
        # Robot's provided solution tour and tour cost
        self.tour = [0, 14, 5, 10, 11, 8, 9, 0]
        self.provided_cost = 166.75801920718544
        
    def test_solution_validity(self):
        # Checking that tour starts and ends at the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
        # Checking one city from each group is visited
        visited_groups = [False] * len(self.groups)
        for city in self.tour[1:-1]:
            for i, group in enumerate(self.groups):
                if city in group:
                    visited_groups[i] = True
        self.assertTrue(all(visited_groups))
        
        # Recalculate the total travel cost
        def euclidean(a, b):
            return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        
        calc_cost = sum(euclidean(self.cities[self.tour[i]], self.cities[self.tour[i+1]]) for i in range(len(self.tour) - 1))
        
        # Test the provided vs calculated cost
        self.assertAlmostEqual(self.provided_cost, calc_cost, places=5)
        
        # Correctness based on all checks
        self.assertTrue(True)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTourSolution))
    runner = unittest.TextTestRunner()

    result = runner.run(test_suite)
    
    # Determining output from result
    if result.wasSuccessful():
        print("CORRECT")
    else:
        read_count = sum(1 for _ in result.errors + result.failures)
        print("FAIL")