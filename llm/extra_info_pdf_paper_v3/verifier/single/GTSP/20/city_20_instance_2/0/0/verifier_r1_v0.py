import unittest
from math import sqrt

# City positions
positions = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
             (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# City groups
groups = [[7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]]

class TestTSPSolution(unittest.TestCase):
    def test_tour_meets_requirements(self):
        tour = [0, 12, 18, 16, 14, 6, 0]
        reported_cost = 170.22489356581875
        
        # Check tour starts and ends at the depot city (City 0)
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        
        # Check one city from each group
        visited_groups = [0] * len(groups)
        for city in tour[1:-1]:  # Skip the depot
            for i, group in enumerate(groups):
                if city in group:
                    visited_groups[i] += 1
        self.assertTrue(all(count == 1 for count in visited_groups))
        
        # Check total number of distinct cities in the tour (including depot)
        self.assertEqual(len(set(tour)), len(tour) - 1)  # minus one because depot appears twice

        # Calculate and verify total travel cost
        calculated_cost = 0
        for i in range(len(tour) - 1):
            pt1, pt2 = positions[tour[i]], positions[tour[i+1]]
            calculated_cost += sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2)
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5)
        
        # All tests passed
        print("CORRECT")

# Running the test
if __name__ == '__main__':
    unittest.main(argv=['first-arg-ignored'], exit=False)