import unittest
from math import sqrt

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
            16: (62, 63), 17: (63, 69), 18: (45, 35)
        }

        self.robot_0_tour = [0, 10, 4, 11, 14, 12, 3, 2, 7, 18, 5, 13, 15, 9, 16, 17, 8, 6, 0]
        self.robot_1_tour = [1, 10, 12, 3, 17, 16, 8, 7, 2, 6, 18, 5, 13, 15, 9, 14, 11, 4, 1]

    def test_tours_for_correctness(self):
        all_tours = sorted(self.robot_0_tour[:-1] + self.robot_1_tour[:-1])
        all_cities = list(range(19))
        self.assertEqual(all_tours, all_cities, "Tours do not visit all cities exactly once")
        
    def test_costs_for_minimization(self):
        total_cost_0 = sum(euclidean_distance(self.cities[self.robot_0_tour[i]], self.cities[self.robot_0_tour[i + 1]]) for i in range(len(self.robot_0_tour)-1))
        total_cost_1 = sum(euclidean_distance(self.cities[self.robot_1_tour[i]], self.cities[self.robot_1_tour[i + 1]]) for i in range(len(self.robot_1_tour)-1))

        expected_cost_0 = 205.86
        expected_cost_1 = 184.41
        combined_cost = total_cost_0 + total_cost_1
        
        actual_combined_cost = 390.26

        self.assertAlmostEqual(total_cost_0, expected_cost_0, delta=0.1, msg="Robot 0's cost incorrect")
        self.assertAlmostEqual(total_cost_1, expected_cost_1, delta=0.1, msg="Robot 1's cost incorrect")
        self.assertAlmostEqual(combined_cost, actual_combined_cost, delta=0.1, msg="Combined cost incorrect")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_tours_for_correctness'))
    suite.addTest(TestTSPSolution('test_costs_for_minimization'))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()