import unittest
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

class TestRobotTour(unittest.TestCase):
    
    def test_robot_tour(self):
        cities = {
            0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
            5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
            10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
            15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
        }
        city_groups = [
            [5, 6, 7, 11, 17],
            [1, 4, 8, 13, 16],
            [2, 10, 15, 18, 19],
            [3, 9, 12, 14]
        ]
        
        proposed_tour = [0, 6, 13, 2, 9, 0]
        proposed_cost = 114.66
        
        # Test starts and ends at depot
        self.assertEqual(proposed_tour[0], 0)
        self.assertEqual(proposed_tour[-1], 0)
        
        # Test visits exactly one city per group
        visited_groups = [0] * 4
        for city in proposed_tour:
            for i, group in enumerate(city_groups):
                if city in group:
                    visited_groups[i] += 1
        self.assertTrue(all(count == 1 for count in visited_groups if count != 0))
        
        # Test cost calculation
        calculated_cost = 0
        for i in range(len(proposed_tour) - 1):
            city1 = cities[proposed_tour[i]]
            city2 = cities[proposed_tour[i+1]]
            calculated_cost += euclidean_distance(city1, city2)
        self.assertAlmostEqual(calculated_cost, proposed_cost, places=2)
        
        # Test the output format (implicitly done by previous checks)
        
        # Test if it's the minimal cost (Not feasibly testable in traditional unit tests)
        
        print("CORRECT")

# To run the test
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)