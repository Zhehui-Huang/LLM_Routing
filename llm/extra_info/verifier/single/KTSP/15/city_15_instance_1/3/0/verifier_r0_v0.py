import math
import unittest

# Provided city locations
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Class to perform unit testing
class TestVRPSolution(unittest.TestCase):
    def test_solution(self):
        # Provided solution
        tour = [0, 6, 1, 7, 3, 9, 0]
        reported_cost = 118.90
        
        # [Requirement 1]
        self.assertEqual(len(cities), 15)  # Check there are 15 cities
        
        # [Requirement 2 & 6]
        self.assertEqual(tour[0], 0)  # Check route starts at depot
        self.assertEqual(tour[-1], 0)  # Check route ends at depot
        
        # [Requirement 3]
        self.assertEqual(len(tour), 7)  # Check that exactly 6 cities are visited including the depot
        
        # [Requirement 4] & [Requirement 7]
        calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        # Since floating-point precision might vary, we use a small threshold for comparing reported vs calculated cost
        self.assertAlmostEqual(calculated_cost, reported_cost, places=2)

# Run the test
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestVRPSolution('test_solution'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    # Output the result based on whether all tests pass
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")