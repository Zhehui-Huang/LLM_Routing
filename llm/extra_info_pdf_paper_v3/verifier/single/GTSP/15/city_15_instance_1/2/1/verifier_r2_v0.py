import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

class TestRobotTour(unittest.TestCase):
    def test_tour_validation(self):
        # Cities with coordinates
        cities = {
            0: (29, 51),
            1: (49, 20),
            2: (79, 69),
            3: (17, 20),
            4: (18, 61),
            5: (40, 57),
            6: (57, 30),
            7: (36, 12),
            8: (93, 43),
            9: (17, 36),
            10: (4, 60),
            11: (78, 82),
            12: (83, 96),
            13: (60, 50),
            14: (98, 1)
        }
        
        # Groups of cities
        groups = [
            [1, 2, 5, 6],
            [8, 9, 10, 13],
            [3, 4, 7],
            [11, 12, 14]
        ]
        
        # Proposed solution
        proposed_tour = [0, 5, 10, 4, 11, 0]
        proposed_cost = 184.24203302868492
        
        # Check if the tour starts and ends at the depot
        self.assertEqual(proposed_tour[0], 0, "Tour should start at depot")
        self.assertEqual(proposed_tour[-1], 0, "Tour should end at depot")
        
        # Check if tour visits only one city from each group and all groups are visited
        visited_groups = set()
        for city in proposed_tou[1:-1]:
            for idx, group in enumerate(groups):
                if city in group:
                    visited_groups.add(idx)
                    
        self.assertEqual(len(visited_groups), 4, "Should visit all four groups")
        self.assertEqual(len(set(provided_tour[1:-1])), 4, "Should visit one city from each group")
        
        # Calculate and verify the travel cost
        cost_calculated = sum(euclidean_distance(cities[proposed_tour[i]], cities[proposed_tour[i + 1]])
                              for i in range(len(proposed_tour) - 1))
        self.assertAlmostEqual(cost_calculated, proposed_cost, places=5, msg="Calculated cost does not match the provided cost")
        
if __name__ == "__main__":
    unittest.main()