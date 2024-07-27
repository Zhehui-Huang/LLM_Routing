import unittest
from math import sqrt

# Coordinates of cities including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Provided solution
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
claimed_total_cost = 478.43

def calculate_two_cities_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_solution(self):
        # Test if tour starts and ends at the depot city
        self.assertEqual(tour[0], 0, "The tour does not start at the depot.")
        self.assertEqual(tour[-1], 0, "The tour does not end at the couch depot.")

        # Test if all cities are visited exactly once
        tour_without_return = tour[1:-1]
        all_cities_once = len(set(tour_without_return)) == (len(cities) - 1)
        self.assertTrue(all_cities_once, "Not all cities are visited exactly once.")

        # Test if the claimed total travel cost is correct
        computed_cost = 0
        for i in range(len(tour)-1):
            computed_cost += calculate_two_cities_distance(cities[tour[i]], cities[tour[i+1]])
        self.assertAlmostEqual(computed_cost, claimed_total_cost, places=2, "Computed cost doesn't match the claimed cost.")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestTravelingSalesmanSolution('test_solution'))
    runner = unittest.TextTestRunner()

    results = runner.run(suite)
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")