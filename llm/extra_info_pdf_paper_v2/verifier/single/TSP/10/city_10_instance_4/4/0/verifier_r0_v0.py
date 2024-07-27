import unittest
from math import sqrt

# Coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculating Euclidean distance
def euclidean_distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Verifying the provided solution
class TestTSPSolution(unittest.TestCase):
    def test_tour(self):
        solution_tour = [0, 4, 7, 5, 1, 9, 8, 2, 6, 3, 0]
        solution_cost = 320.7939094250147

        # Test tour starts and ends at depot city 0
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

        # Test all cities are visited exactly once except the depot
        visited_once = all(solution_tour.count(city) == 1 for city in solution_tour[1:-1])
        self.assertTrue(visited_once)
        self.assertEqual(len(set(solution_tour)), 11)  # including repeating depot city

        # Test calculates correct Euclidean distance as total travel cost
        calculated_cost = sum(
            euclidean_distance(cities[solution_tour[i]], cities[solution_tour[i + 1]])
            for i in range(len(solution_tour) - 1)
        )
        self.assertAlmostEqual(calculated_cost, solution_cost, places=5)

        # Test cities match requirement there are 10 cities
        self.assertEqual(len(cities), 10)

        # Test Complete tour path verification
        expected_path_length = 11
        self.assertEqual(len(solution_tour), expected_path_length)

# Running the test
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)