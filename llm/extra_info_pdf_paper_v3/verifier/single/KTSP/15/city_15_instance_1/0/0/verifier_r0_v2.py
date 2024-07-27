import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
            5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
            10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
        }
        self.tour = [0, 6, 1, 7, 3, 9, 0]
        self.reported_cost = 118.9

    def euclidean_distance(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def test_tour_validity(self):
        # Start and end at the depot
        self.assertEqual(self.tour[0], 0, "Does not start at city 0")
        self.assertEqual(self.tour[-1], 0, "Does not end at city 0")
        
        # Visit exactly 6 cities
        self.assertEqual(len(set(self.tour)), 6, "Does not visit exactly 6 cities")
        
        # Calculate the total cost
        total_cost_calculated = sum(self.euclidean_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost_calculated, self.reported_cost, places=1, "Travel cost calculated incorrectly")

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestKTPDFSolver("test_tour_validity"))
    
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()