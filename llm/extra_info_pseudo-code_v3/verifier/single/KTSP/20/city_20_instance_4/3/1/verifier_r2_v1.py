import unittest
from math import sqrt

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Proposed solution tour and cost
solution_tour = [0, 2, 14, 1, 8, 17, 11, 13, 5, 7, 12, 15, 10, 6, 4, 3, 0]
solution_cost = 460.95668696003327

def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_cost += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_solution_validity(self):
        calculated_cost = calculate_tour_cost(solution_tour, cities)
        self.assertEqual(len(solution_tour), 17, "The tour does not have exactly 17 stops (including return).")
        self.assertEqual(solution_tour[0], solution_tour[-1], "Tour does not start and end at the depot.")
        self.assertEqual(len(set(solution_tour)), 16, "Tour does not visit exactly 16 different cities.")
        self.assertAlmostEqual(calculated_cost, solution_cost, places=5, "The reported total travel cost is incorrect.")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_solution_validity'))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Run the tests and print the outcome
print(run_tests())