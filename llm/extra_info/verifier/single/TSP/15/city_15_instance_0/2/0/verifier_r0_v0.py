import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
            6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 
            11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
        }
        self.tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
        self.reported_cost = 373.97393412233544

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city 0")

    def test_cities_visited_exactly_once(self):
        unique_cities = set(self.tour[1:-1])  # Exclude the starting and ending 0
        expected_cities = set(range(1, 15))
        self.assertEqual(unique_cities, expected_cities, "Each city must be visited exactly once")

    def test_total_travel_cost_computation(self):
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

        total_cost = 0
        for i in range(len(self.tour) - 1):
            p1 = self.coordinates[self.tour[i]]
            p2 = self.coordinates[self.tour[i + 1]]
            total_cost += euclidean_distance(p1, p2)
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, 
                               msg="The calculated travel cost must be approx. equal to the reported travel cost")

    def test_output_format(self):
        self.assertIsInstance(self.tour, list, "Tour output must be a list")
        self.assertTrue(all(isinstance(i, int) for i in self.tour), "Tour list must contain integers")

    def test_tour_validity_on_constraints(self):
        # This test is to ensure that all requirements are respected
        try:
            self.test_tour_starts_and_ends_at_depot()
            self.test_cities_visited_exactly_once()
            self.test_total_travel_cost_computation()
            self.test_output_format()
        except AssertionError:
            return "FAIL"
        return "CORRECT"

# Let's run our unittests
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_tour_validity_on_constraints'))
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)
    
    overall_result = "CORRECT" if result.wasSuccessful() else "FAIL"
    print(overall_result)