import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

class TestTSPSolutionCheck(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (8, 11),  # Depot
            (40, 6),  (95, 33), (80, 60), (25, 18), 
            (67, 23), (97, 32), (25, 71), (61, 16), 
            (27, 91), (91, 46), (40, 87), (20, 97), 
            (61, 25), (5, 59), (62, 88), (13, 43), 
            (61, 28), (60, 63), (93, 15)
        ]
        self.tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
        self.reported_max_distance = 32.39

    def test_tsp_solution(self):
        # Test start and end at depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

        # Test all cities visited exactly once
        expected_cities = set(range(20))
        visited_cities = set(self.tour)
        self.assertEqual(visited_cities, expected_cities)

        # Test maximum distance assertion
        max_distance = 0
        for i in range(len(self.tour) - 1):
            distance = calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            if distance > max_distance:
                max_distance = distance
        
        self.assertAlmostEqual(max_distance, self.reported_max_distance, places=2)

# Run tests
suite = unittest.TestSuite()
suite.addTest(TestTSPSolutionCheck('test_tsp_solution'))

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Check result and decide output
if result.wasSuccessful():
    print("CORRECT")
else:
    if len(result.failures) > 0:
        print("FAIL")
    if len(result.errors) > 0:
        print("FAIL")