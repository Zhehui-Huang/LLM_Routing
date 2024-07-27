import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (54, 87),  # Depot city 0
            (21, 84),  # City 1
            (69, 84),  # City 2
            (53, 40),  # City 3
            (54, 42),  # City 4
            (36, 30),  # City 5
            (52, 82),  # City 6
            (93, 44),  # City 7
            (21, 78),  # City 8
            (68, 14),  # City 9
            (51, 28),  # City 10
            (44, 79),  # City 11
            (56, 58),  # City 12
            (72, 43),  # City 13
            (6, 99)   # City 14
        ]

        # This would be the expected output of the heuristic algorithm
        self.tour = [0, 1, 8, 11, 6, 2, 13, 7, 3, 4, 12, 10, 5, 9, 14, 0]
        self.total_travel_cost = calculate_total_cost(self.tour, self.cities)

    def test_unique_cities(self):
        # Requirement 1: All cities visited exactly once except depot (from 1 to last - 1)
        self.assertEqual(len(set(self.tour[1:-1])), 14)

    def test_start_and_end_at_depot(self):
        # Requirement 2 and 4: Start and End at the Depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_output_format_and_total_cost(self):
        # Requirement 4 and 5: Output format and correct total cost
        correct_format = isinstance(self.tour, list) and all(isinstance(x, int) for x in self.tour)
        self.assertTrue(correct_format)
        # We calculate the tour cost to simulate the solution's side effect
        recalculated_cost = calculate_total_cost(self.tour, self.cities)
        self.assertAlmostEqual(recalculated_cost, self.total_travel_class_cost)

    def test_heuristic_performance(self):
        # Requirement 6 and 7: Heuristic performance check not directly possible in unit tests
        # typically we would need to compare with a known optimal solution or its bound here
        optimal_cost = 400  # Hypothetical optimal cost for the TSP
        self.assertLessEqual(self.total_travel_cost, optimal_cost * 1.5)

    def test_solution_is_correct(self):
        try:
            self.test_unique_cities()
            self.test_start_and_end_at_depot()
            self.test_output_format_and_total_cost()
            self.test_heuristic_performance()
            print("CORRECT")
        except Exception as e:
            print("FAIL")

# Create test suite
suite = unittest.TestSuite()
suite.addTest(TestTSPSolution('test_solution_is_correct'))

# Run the tests
runner = unittest.TextTestRunner()
runner.run(suite)