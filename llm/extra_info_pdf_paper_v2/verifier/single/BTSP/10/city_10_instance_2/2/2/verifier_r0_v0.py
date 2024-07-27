import unittest
from math import sqrt

# Input data
cities = {
    0: (90, 3),
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

# Proposed solution to be tested
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]

# Function to compute Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Unit Test Class
class TestTSPSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        """Check that the tour starts and ends at the depot city 0."""
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
    
    def test_visit_each_city_once(self):
        """Check that each city is visited exactly once excluding the return to the depot."""
        visited = set(tour[:-1])  # Exclude the last element since it's a return to start
        self.assertEqual(len(visited), len(cities))
    
    def test_minimize_maximum_distance(self):
        """Check if the maximum distance given is the longest single jump in the tour."""
        max_distance_given = 69.42621983083913
        distances = [euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)]
        max_distance_calculated = max(distances)
        self.assertAlmostEqual(max_distance_calculated, max_distance_given, places=5, 
                               msg=f'Expected max distance {max_distance_given}, got {max_distance_calculated}')

# Main function to run the test
def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()