import unittest
import math

class VerifyRobotSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
            5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
            10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
            15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 
            19: (129, 189), 20: (155, 185), 21: (139, 182)
        }
        
        self.tours = [
            [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21, 0],
            [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21, 0],
            [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21, 0],
            [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21, 0]
        ]
        
        self.expected_total_cost = 1248.36

    def test_cost_calculation(self):
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        total_cost = 0
        for tour in self.tours:
            cost = 0
            for i in range(len(tour) - 1):
                cost += euclidean_distance(self.coordinates[tour[i]], self.coordinates[tour[i + 1]])
            total_cost += cost
        
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=2, msg="Total travel costs mismatch.")
    
    def test_unique_city_visit(self):
        all_visited = sum((tour[:-1] for tour in self.tours), [])
        self.assertEqual(len(all_visited), len(set(all_visited)), "Some cities are visited more than once.")
    
    def test_solution_validity(self):
        if self._outcome.errors:
            print("FAIL")
        else:
            print("CORRECT")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)