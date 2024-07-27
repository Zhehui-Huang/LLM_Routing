import unittest
import math

class TestRobotTourEnhanced(unittest.TestCase):
    def setUp(self):
        # Provided solution
        self.solution = {
            "Tour": [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0],
            "Total travel cost": 337.8447016788252,
            "Maximum distance between consecutive cities": 60.67124524847005
        }
        
        self.coordinates = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }

    def euclidean_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def test_verification(self):
        tour = self.solution["Tour"]
        expected_cost = self.solution["Total travel cost"]
        expected_max_distance = self.solution["Maximum distance between consecutive cities"]
        
        # Check tour starts and ends at the depot
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        
        # Check all cities visited exactly once except the depot
        self.assertCountEqual(tour[1:-1], list(range(1, 15)))
        
        # Calculate total travel cost
        calculated_cost = sum(self.euclidean_distance(self.coordinates[tour[i]], self.coordinates[tour[i+1]]) for i in range(len(tour)-1))
        
        # Calculate max distance between consecutive cities
        max_distance = max(self.euclidean_distance(self.coordinates[tour[i]], self.coordinates[tour[i+1]]) for i in range(len(tour)-1))
        
        correct_cost = math.isclose(calculated_cost, expected_cost, rel_tol=0.01)
        correct_max_distance = math.isclose(max_distance, expected_max_constraint, rel_tol=0.01)

        # Check the cost and max distance calculated matches the expected ones
        self.assertTrue(correct_cost and correct_max_distance, f"FAIL: Cost or Max Distance constraint failed. Cost: {calculated_cost} vs {expected_cost}, Max Dist: {max_distance} vs {expected_max_distance}")

        # If all checks pass, output CORRECT
        print("CORRECT")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)