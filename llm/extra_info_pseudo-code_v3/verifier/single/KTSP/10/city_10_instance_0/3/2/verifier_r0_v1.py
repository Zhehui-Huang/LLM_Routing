import unittest
import math

# Given solution
solution_tour = [0, 9, 5, 6, 0]
solution_cost = 61.65991894151281

# Provided coordinates of cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_solution_correctness(self):
        self.assertEqual(len(cities), 10, "FAIL: The number of cities does not match 10.")
        self.assertEqual(solution_tour[0], 0, "FAIL: Tour does not start at depot city 0.")
        self.assertEqual(solution_tour[-1], 0, "FAIL: Tour does not end at depot city 0.")
        self.assertEqual(len(set(solution_tour)), 4, "FAIL: Robot does not visit exactly 4 unique cities including the depot.")
        
        total_distance = 0
        for i in range(len(solution_tour) - 1):
            city_from = solution_tour[i]
            city_to = solution_tour[i + 1]
            total_distance += calculate_distance(cities[city_from], cities[city_to])
        
        self.assertAlmostEqual(total_distance, solution_cost, places=5, "FAIL: The calculated travel cost does not match the given solution cost.")
        
        print("CORRECT")

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_solution_correctness'))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

run_tests()