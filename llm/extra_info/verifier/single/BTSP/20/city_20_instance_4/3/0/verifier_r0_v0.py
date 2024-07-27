import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
            5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
            10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
            15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
        }
        self.solution_tour = [0, 13, 19, 8, 15, 11, 10, 7, 18, 16, 17, 5, 1, 3, 9, 4, 6, 2, 12, 14, 0]
        self.total_cost = 1119.1132061819012
        self.max_distance = 102.07840124139877
    
    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
    
    def test_visits_each_city_once(self):
        unique_cities = set(self.solution_tour)
        self.assertEqual(len(unique_cities), 20)
    
    def test_travel_cost(self):
        calculated_cost = sum(euclidean_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i + 1]]) 
                               for i in range(len(self.solution_tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5)
    
    def test_max_distance(self):
        max_dist = max(euclidean_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i + 1]]) 
                       for i in range(len(self.solution_tour) - 1))
        self.assertAlmostEqual(max_dist, self.max_distance, places=5)
    
    def test_output(self):
        # Test if output requirements are correctly implemented
        tour = self.solution_tour
        total_travel_cost = self.total_cost
        maximum_distance = self.max_distance
        condition1 = tour[0] == 0 and tour[-1] == 0
        condition2 = len(set(tour)) == 20 and len(tour) == 21
        condition3 = approximately_equal(total_travel_cost, 1119.1132061819012)
        condition4 = approximately_equal(maximum_distance, 102.07840124139877)
        
        if condition1 and condition2 and condition3 and condition4:
            result = "CORRECT"
        else:
            result = "FAIL"
        
        self.assertEqual(result, "CORRECT")

def approximately_equal(a, b, tol=0.0001):
    return abs(a - b) < tol

if __name__ == "__main__":
    unittest.main()