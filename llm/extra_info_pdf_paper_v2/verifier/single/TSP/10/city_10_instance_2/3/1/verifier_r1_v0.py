import math
import unittest

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coords = {
            0: (90, 3),   # Depot
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        self.proposed_tour = [0, 8, 5, 9, 1, 2, 7, 4, 6, 3, 0]
        self.proposed_total_cost = 354.91010610434057

    def test_tour_validity(self):
        self.assertEqual(self.proposed_tour[0], 0, "Tour should start at the depot city 0")
        self.assertEqual(self.proposed_tour[-1], 0, "Tour should end at the depot city 0")
        self.assertEqual(len(set(self.proposed_tour)), 10, "Tour should visit each city exactly once including depot")
        self.assertEqual(len(self.proposed_tour), 11, "Tour should have correct length visiting all cities and returning")

    def test_tour_distance(self):
        total_calculated_distance = 0
        for i in range(len(self.proposed_tour) - 1):
            city_from = self.proposed_tour[i]
            city_to = self.proposed_tour[i + 1]
            total_calculated_distance += calculate_euclidean_distance(self.coords[city_from], self.coords[city_to])
        
        self.assertAlmostEqual(total_calculated_distance, self.proposed_total_cost, places=5, 
                               msg="Calculated tour distance should match the provided total travel cost")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_tour_validity'))
    test_suite.addTest(TestTSPSolution('test_tour_distance'))

    runner = unittest.TextTestRunner()
    results = runner.run(test_suite)
    
    if len(results.failures) == 0 and len(results.errors) == 0:
        print("CORRECT")
    else:
        print("FAIL")