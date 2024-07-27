import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    """ Compute Euclidean distance between two points. """
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
        
        # Check if the tour visits only one city from each group
        visited_groups = set()
        for city in proposed_tour[1:-1]:
            for idx, group in enumerate(groups):
                if city in group:
                    visited_groups.add(idx)
                    
        self.assertEqual(len(visited_groups), 4, "Should visit one city from each group")
        self.assertEqual(len(set(proposed_tour[1:-1])), 4, "Should visit only 4 cities")
        
        # Calculate and verify the travel cost
        calculated_cost = sum(euclidean_distance(cities[proposed_tour[i]], cities[proposed_tour[i + 1]])
                              for i in range(len(proposed_tour) - 1))
        self.assertAlmostEqual(calculated_cost, proposed_cost, places=5, "Calculated cost does not match the provided cost")

# To run the test
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)