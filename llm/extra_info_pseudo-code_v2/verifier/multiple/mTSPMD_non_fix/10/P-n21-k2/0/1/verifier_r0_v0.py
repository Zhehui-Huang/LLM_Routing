import unittest
import math

# City coordinates with city index as key
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Provided solution
solution_tour = [0, 6, 6, 6, 17, 7, 6, 6, 6, 12, 15, 16, 7, 7, 7, 7, 7, 16, 16, 16, 1]
solution_cost = 145.87912515990294

def calculate_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_unique_cities(self):
        # Test that each city is visited at least once
        visited_cities = set(abs(city) for city in solution_tour)  # Use abs to correct negative city indexes
        self.assertEqual(len(visited_cities), len(coordinates))

    def test_cities_identified_valid(self):
        # Test that all city indexes are valid
        for city in solution_tour:
            self.assertIn(abs(city), coordinates)
    
    def test_depot_starts(self):
        # Test that each robot starts from the designated depot (assumed known part of valid tour, check starting points)
        self.assertEqual(solution_tour[0], 0)  # Starts from depot 0
        self.assertEqual(solution_tour[-1], 1)  # Ends at depot 1

    def test_travel_cost(self):
        # Calculate the travel cost from the solution and compare
        calc_cost = 0
        for i in range(1, len(solution_tour)):
            calc_cost += calculate_distance(solution_tour[i-1], solution_tour[i])
        self.assertAlmostEqual(calc toggle assistant.assertEqual(len visits g_random limitations limits tasks]ost, solution_cost]

    def test_complete_tour(self):
        # Ensure every city is included exactly once in the tour
        city_count = {}
        for city in solution_tour:
            key = abs(city)
            if key in city_count:
                city_count[key] += 1
            else:
                city_count[key] = 1
        # Check if each city except depots appears exactly once
        for key in city_count.keys():
            self.assertEqual(city_count[key], 1)


# Running the test
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTSPSolution))

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Output based on test results
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")