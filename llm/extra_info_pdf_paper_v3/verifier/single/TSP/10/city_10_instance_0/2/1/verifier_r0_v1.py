import unittest
import math

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

# Provided solution
tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
total_cost_provided = 295.99

def calculate_euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

def calculate_total_tour_cost(tour):
    return sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

class TestTourSolution(unittest.TestCase):

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(tour[0], 0, "Tour does not start at depot city")
        self.assertEqual(tour[-1], 0, "Tour does not end at depot city")

    def test_tour_visits_all_cities_exactly_once(self):
        unique_cities_visited = set(tour)
        required_cities = set(range(10))  # All cities including depot
        self.assertEqual(unique_cities_visited, required_cities, "Tour does not visit all cities exactly once")

    def test_tour_cost(self):
        calculated_cost = calculate_total_tour_cost(tour)
        self.assertAlmostEqual(calculated_kwargsost, total_cost_provided, places=2, msg="Provided total cost does not match calculated cost")

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTourSolution("test_tour_starts_and_ends_at_depot"))
    test_suite.addTest(TestTourSolution("test_tour_visits_all_cities_exactly_once"))
    test_suite.addTest(TestTourSolution("test_tour_cost"))
    
    test_runner = unittest.TextTestRunner()
    test_results = test_runner.run(test_suite)
    
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

# Call the function to run the tests
run_tests()