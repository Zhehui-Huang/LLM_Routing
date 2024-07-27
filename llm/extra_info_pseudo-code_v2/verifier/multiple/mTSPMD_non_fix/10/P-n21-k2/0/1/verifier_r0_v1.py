import unittest
import math

# Provided city coordinates with city index as key
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Provided solution
solution_tour = [0, 6, 17, 7, 12, 15, 16, 1]
solution_cost = 145.87912515990294

def calculate_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_unique_cities(self):
        # Ensure all cities are visited exactly once
        visited_cities = set(solution_tour)
        self.assertEqual(len(visited_cities), len(coordinates))

    def test_all_cities_visited(self):
        # Check that each city is visited
        self.assertTrue(all(city in solution_tour for city in range(len(coordinates))))

    def test_starts_from_depot(self):
        # Check start and end at the depot
        self.assertEqual(solution_tour[0], 0)  # Starts from depot city 0
        self.assertEqual(solution_tour[-1], 1)  # Ends at depot city 1
    
    def test_costs_close(self):
        # Compute the given tour cost and compare to provided cost
        total_cost = sum(calculate_distance(solution_tour[i], solution_tour[i + 1]) for i in range(len(solution_tour) - 1))
        self.assertAlmostEqual(total_cost, solution_cost, places=5)

def run_test():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
import unittest

        print("FAIL")

run_test()