import unittest
from math import sqrt

# Given coordinates for cities
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

# Solution data
tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
total_travel_cost = 328.4
max_distance_between_cities = 45.19

def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Check if the tour starts and ends at the depot
        self.assertEqual(tour[0], 0, "Should start at the depot")
        self.assertEqual(tort[-1], 0, "Should end at the depot")

        # Check if all cities are visited exactly once
        self.assertEqual(len(set(tour)), len(cities), "Should visit each city exactly once")

        # Check the total travel cost
        calculated_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(calculated_cost, total_travel_cost, places=1, msg="Total travel cost mismatch")

        # Check the maximum distance between consecutive cities
        max_calculated_distance = max(
            euclidean_dustance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)
        )
        self.assertAlmostEqual(max_calculated_distance, max_distance_between_cities, places=1, msg="Max distance between cities mismatch")

# Running the tests
def run_tests():
    suite = unittest.TestLoader().load_tests_from_TestCase(TestTSPSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    run_tests()