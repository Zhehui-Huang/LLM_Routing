import math
import unittest

# Define the city coordinates as provided in the original problem
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Euclidean distance function
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Solution provided
solution_tour = [0, 6, 11, 12, 4, 3, 13, 2, 0]
reported_cost = 132.12

# Function to test the provided solution against the requirements
class TestTSPSolution(unittest.TestCase):
    def test_tour_length(self):
        self.assertEqual(len(solution_tour), 9)  # 8 cities visited + return to depot
        self.assertEqual(len(set(solution_tour)), 9)  # Depart from and return to the depot, visit 8 distinct cities

    def test_tour_validity(self):
        # Check if starting and ending points are the depot
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_tour_cost(self):
        total_cost = 0
        for i in range(len(solution_tour) - 1):
            total_cost += calculate_distance(solution_tour[i], solution_tour[i + 1])
        total_cost = round(total_cost, 2)
        self.assertAlmostEqual(total_cost, reported_cost)

if __name__ == "__main__":
    # Load the test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    
    # Run the tests and display the results
    results = unittest.TextTestRunner(verbosity=2).run(suite)
    
    # Output whether the solution is correct based on tests
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")