import math
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
            (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
            (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
        ]
        self.groups = [
            [1, 2, 5, 6],
            [8, 9, 10, 13],
            [3, 4, 7],
            [11, 12, 14]
        ]
        self.solution_tour = [0, 5, 10, 4, 11, 0]
        self.solution_cost = 184.24

    def distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_tour(self):
        # test if tour starts and ends at depot
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
        
        # test if tour visits exactly one city from each group
        visited = [False]*len(self.groups)
        for city in self.solution_tour[1:-1]:
            for i, group in enumerate(self.groups):
                if city in group:
                    visited[i] = True
                    break
        self.assertTrue(all(visited))

        # Calculate distance and compare it with given cost
        total_distance = sum(self.distance(self.solution_tour[i], self.solution_tour[i + 1]) for i in range(len(self.solution_tour) - 1))
        self.assertAlmostEqual(total_distance, self.solution_cost, places=2)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_tour'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # Check results and output "CORRECT" or "FAIL"
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()