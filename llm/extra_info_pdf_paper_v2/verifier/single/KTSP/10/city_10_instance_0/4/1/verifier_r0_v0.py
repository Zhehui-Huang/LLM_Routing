import math
import unittest

# Provided city coordinates
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

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Test class
class TestKTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Proposed solution
        tour = [0, 9, 5, 6, 0]
        reported_total_cost = 61.66

        # Verify tour starts and ends at the depot city
        self.assertEqual(tour[0], 0, "Tour does not start at depot city")
        self.assertEqual(tour[-1], 0, "Tour does not end at depot city")

        # Verify the robot visits exactly 4 cities including the depot
        self.assertEqual(len(set(tour)), 4, "Tour does not visit exactly 4 cities")

        # Calculate the actual travel cost of the tour
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(tour[i], tour[i+1])

        # Check if calculated cost matches the provided cost and format matches
        self.assertAlmostEqual(total_cost, reported_total_cost, places=2, msg="Reported and calculated costs do not match")

        # Check if the output contains the right tour start, end, and cost
        self.assertEqual(tour, [0, 9, 5, 6, 0], "Output does not specify the correct tour")
        self.assertEqual(math.isclose(total_cost, reported_total_cost, abs_tol=0.01), True, 
                         "Output travel cost is not within acceptable error margin")

# Run the test
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
    test_result = unittest.TextTestRunner().run(suite)
    
    if test_title:
        print("CORRECT" if test_result.wasSuccessful() else "FAIL")