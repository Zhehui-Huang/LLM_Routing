import unittest
from math import sqrt

# Coordinates for cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 
    14: (58, 27), 15: (37, 69)
}

# Tours given in the solution
tours = [
    [0, 9, 13, 0], [0, 12, 15, 0], [0, 6, 0], [0, 4, 11, 0], [0, 5, 14, 0], 
    [0, 8, 3, 0], [0, 10, 1, 0], [0, 2, 7, 0]
]

def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

given_costs = [68.39, 66.12, 24.08, 57.39, 62.44, 72.82, 41.77, 51.59]

class VerifyMTSPSolution(unittest.TestCase):
    def test_all_requirements(self):
        # Check if all tours start and end at depot
        for tour in tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)
        
        # Check if all cities are visited exactly once
        visited = [0] * 16
        for tour in tours:
            for city in tour[1:-1]:  # Only count non-depot visits
                visited[city] += 1
        
        # Each city except depot should be visited exactly once
        self.assertTrue(all(v == 1 for i, v in enumerate(visited) if i != 0))
        
        # Check travel costs and max cost requirement
        calculated_costs = []
        for tour in tours:
            cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
            calculated_costs.append(cost)
        
        max_calculated_cost = max(calculated_costs)
        expected_max_cost = 72.82
        self.assertAlmostEqual(max_calculated_cost, expected_max_cost, places=2)

        # Check if provided costs are correct
        for given, calculated in zip(given_costs, calculated_costs):
            self.assertAlmostEqual(given, calculated, places=2)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(VerifyMTSPSolution('test_all_requirements'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()