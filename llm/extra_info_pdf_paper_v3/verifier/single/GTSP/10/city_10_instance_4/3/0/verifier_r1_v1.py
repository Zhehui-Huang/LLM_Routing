import unittest
import math

class TestGTSPSolution(unittest.TestCase):
    def setUp(self):
        # Initialize coordinates of cities and the groups
        self.coords = {
            0: (79, 15), 1: (79, 55), 2: (4, 80), 
            3: (65, 26), 4: (92, 9), 5: (83, 61), 
            6: (22, 21), 7: (97, 70), 8: (20, 99), 
            9: (66, 62)
        }
        
        self.groups = {
            0: [1, 4], 1: [2, 6], 2: [7], 
            3: [5], 4: [9], 5: [8], 6: [3]
        }
        
        self.solution_tour = [0, 1, 5, 7, 9, 8, 2, 3, 0]
        self.solution_cost = 279.02

    def test_solution_validity(self):
        try:
            # Test start and end at depot
            self.assertEqual(self.solution_tour[0], 0, "Start at depot")
            self.assertEqual(self.solution_tour[-1], 0, "End at depot")
            
            # Test visiting one city per group
            visited = set(self.solution_tour[1:-1])  # exclude the depot occurrences
            self.assertEqual(len(visited), 7, "Visit one per group")
            for city in visited:
                found = False
                for group in self.groups.values():
                    if city in group:
                        found = True
                        break
                self.assertTrue(found, "City must be from a required group")
    
            # Test using Euclidean distance
            def euclidean(a, b):
                return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    
            calculated_cost = 0
            tour_costs = []
            for i in range(len(self.solution_tour) - 1):
                city_a = self.solution_tour[i]
                city_b = self.solution_tour[i + 1]
                tour_costs.append(euclidean(self.coords[city_a], self.coords[city_b]))
                calculated_cost += euclidean(self.coords[city_a], self.coords[city_b])
    
            # This test has a hidden assumption about known solution cost
            self.assertAlmostEqual(calculated_cost, self.solution_cost, delta=0.1, msg="Check total travel cost computation.")
            
            print("CORRECT")
        except Exception as e:
            print("FAIL")
            print(e)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # Corrects argv for notebooks and IDEs.