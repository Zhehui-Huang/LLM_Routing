import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (9, 93),  # City 0
            (8, 51),  # City 1
            (74, 99), # City 2
            (78, 50), # City 3
        ]
        self.tour = [0, 1, 2, 3, 0]
        self.total_cost = 254.08562683745149
        self.max_distance = 81.60882305241266

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], self.tour[-1], "The tour does not start and end at the depot city.")

    def test_visit_each_city_once(self):
        unique_cities = list(set(self.tour[1:-1]))
        self.assertCountEqual(unique_cities, range(1, len(self.cities)-1), "Each city is not visited exactly once.")

    def test_total_travel_cost(self):
        calculated_cost = 0
        for i in range(1, len(self.tour)):
            calculated_cost += calculate_distance(self.cities[self.tour[i - 1]], self.cities[self.tour[i]])
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5, msg="Total cost does not match.")

    def test_maximum_distance(self):
        max_calculated_distance = max(
            calculate_distance(self.cities[self.tour[i - 1]], self.cities[self.tour[i]]) for i in range(1, len(self.tour))
        )
        self.assertAlmostEqual(max_calculated_distance, self.max_distance, places=5, msg="Maximum distance between consecutive cities does not match.")

# Helper function to run the tests
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTravelingSalesmanSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Execute the tests
output = run_tests()
print(output)