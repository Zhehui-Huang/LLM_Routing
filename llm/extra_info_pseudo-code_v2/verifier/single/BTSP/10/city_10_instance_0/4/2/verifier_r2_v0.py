import unittest
from math import sqrt

# Function to calculate Euclidean distance between two coordinates
def distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Test class for the solution
class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
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
        self.tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
        self.total_cost = 295.9919678938414
        self.max_cost = 56.462376853972415

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_each_city_once(self):
        num_cities = len(self.cities)
        # Excluding the last city since it should be the depot repeated
        visited = sorted(self.tour[:-1])
        self.assertEqual(visited, list(range(num_cities)))

    def test_minimize_max_distance(self):
        computed_max_distance = max(distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]]) 
                                    for i in range(len(self.tour)-1))
        self.assertAlmostEqual(computed_max_distance, self.max_cost, places=5)

# Function to run the tests
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # Output result
    if len(result.failures) == 0 and len(result.errors) == 0:
        return "CORRECT"
    else:
        return "FAIL"

# Running the tests
output = run_tests()
print(output)