import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Given cities and their coordinates
        self.cities = {
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
        # Proposed solution tour and total cost
        self.tour_solution = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
        self.total_cost_solution = 384.7863591860825

    def test_tour_starts_and_ends_in_depot(self):
        # Check if tour starts and ends at the depot city
        self.assertEqual(self.tour_solution[0], 0)
        self.assertEqual(self.tour_solution[-1], 0)

    def test_visits_each_city_once(self):
        # Check if each city is visited exactly once
        cities_visited = sorted(self.tour_solution[1:-1])
        expected_cities = sorted(self.cities.keys())[1:]  # city 0 is depot, visited twice
        self.assertEqual(cities_visited, expected_cities)

    def test_total_travel_cost(self):
        # Calculate the distance using the provided tour
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
        
        calculated_cost = 0
        for i in range(len(self.tour_solution) - 1):
            city_a_idx = self.tour_solution[i]
            city_b_idx = self.tour_solution[i + 1]
            city_a = self.cities[city_a_idx]
            city_b = self.cities[city_b_idx]
            calculated_cost += euclidean_distance(city_a, city_b)

        # Compare the calculated cost to the provided solution cost
        self.assertAlmostEqual(calculated_cost, self.total_cost_solution, places=5)

    def test_solution_correctness(self):
        # Run all tests
        self.test_tour_starts_and_ends_in_depot()
        self.test_visits_each_in_city_once_with_exactly_one_visit()
        self.test_total_travel_cost()

# Execute the test suite
suite = unittest.TestSuite()

# Add tests to the suite
suite.addTest(TestTSPSolution('test_tour_starts_and_ends_in_depot'))
suite.addTest(TestTSPSolution('test_visits_each_city_once'))
suite.addTest(TestTSPSolution('test_total_travel_cost'))
suite.addTest(TestTSPSolution('test_solution_correctness'))

# Create the test runner and run the suite
runner = unittest.TextTestRunner()
result = runner.run(suite)

# Providing result based on the assertions passing
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")