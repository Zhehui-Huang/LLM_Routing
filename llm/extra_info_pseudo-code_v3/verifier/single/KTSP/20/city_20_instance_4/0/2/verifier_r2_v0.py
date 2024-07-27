import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates for the cities
        self.cities = {
            0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
            5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
            10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
            15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
        }
        self.proposed_solution = [0, 8, 17, 18, 13, 1, 11, 2, 9, 16, 7, 12, 6, 3, 4, 19, 0]
        self.reported_cost = 367.04882231635327

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.proposed_solution[0], 0)
        self.assertEqual(self.proposed_solution[-1], 0)

    def test_tour_length(self):
        # Check if 16 cities are visited once, plus return to depot
        self.assertEqual(len(self.proposed_solution), 17)
        self.assertEqual(len(set(self.proposed_solution)), 17)

    def test_tour_total_travel_cost(self):
        # Compute the total travel cost
        total_cost = 0
        for i in range(len(self.proposed_solution) - 1):
            city_a = self.proposed_solution[i]
            city_b = self.proposed_solution[i + 1]
            total_cost += euclidean_distance(self.cities[city_a], self.cities[city_b])
        self.assertAlmostEqual(total_cost, self.reported_cost)

    def test_valid_cities_in_tour(self):
        # Validate that only cities from 0-19 are in the tour
        for city in self.proposed_solution:
            self.assertIn(city, self.cities)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Perform the tests
result = run_tests()
print(result)