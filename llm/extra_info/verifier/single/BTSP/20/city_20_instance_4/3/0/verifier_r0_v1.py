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
    
    def test_solution_validity(self):
        # Test starting and ending at depot
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
        
        # Test visiting each city exactly once except the depot
        city_visit_counts = {i: 0 for i in range(20)}
        for city in self.solution_tour:
            city_visit_counts[city] += 1
        self.assertTrue(all(count == 1 for city, count in city_visit_counts.items() if city != 0))
        self.assertEqual(city_visit_counts[0], 2)  # Start and end at depot
        
        # Test correct calculation of Euclidean distances and total cost
        calculated_total_cost = 0
        calculated_max_distance = 0
        for i in range(len(self.solution_tour) - 1):
            dist = euclidean_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i+1]])
            calculated_total_cost += dist
            if dist > calculated_max_distance:
                calculated_max_distance = dist
        
        self.assertAlmostEqual(calculated_total_cost, self.total_utf8_cost, places=5)
        self.assertAlmostEqual(calculated_max_distance, self.max_distance, places=5)
        
        # If all tests pass without assertion error
        print("CORRECT")

# Run the tests
if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass