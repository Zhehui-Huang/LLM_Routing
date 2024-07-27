import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = None  # This should be replaced with the actual tour list when available
        self.total_cost = 328.40
        self.max_distance = 45.19

        # Example city coordinates (according to the provided ones)
        self.coordinates = [
            (50, 42), (41, 1), (18, 46), (40, 98),
            (51, 69), (47, 39), (62, 26), (79, 31),
            (61, 90), (42, 49)
        ]

    def test_starts_and_ends_at_depot(self):
        if self.tour:
            self.assertEqual(self.tour[0], 0)
            self.assertEqual(self.tour[-1], 0)
    
    def test_visits_each_city_once(self):
        if self.tour:
            tour_cities = sorted(self.tour[1:-1])
            expected_cities = list(range(1, 10))
            self.assertEqual(tour_cities, expected_cities)

    def test_output_tour_format(self):
        if self.tour:
            self.assertIsInstance(self.tour, list)
            self.assertTrue(all(isinstance(i, int) for i in self.tour))

    def test_total_travel_cost(self):
        calculated_cost = 0
        if self.tour:
            for i in range(len(self.tour) - 1):
                start = self.tour[i]
                end = self.tour[i+1]
                distance = math.sqrt((self.coordinates[start][0] - self.coordinates[end][0])**2 +
                                     (self.coordinates[start][1] - self.coordinates[end][1])**2)
                calculated_cost += distance
            self.assertAlmostEqual(calculated_cost, self.total_cost, places=2)

    def test_max_distance_between_consecutive_cities(self):
        max_distance = 0
        if self.tour:
            for i in range(len(self.tour) - 1):
                start = self.tour[i]
                end = self.tour[i+1]
                distance = math.sqrt((self.coordinates[start][0] - self.coordinates[end][0])**2 +
                                     (self.coordinates[start][1] - self.coordinates[end][1])**2)
                if distance > max_distance:
                    max_distance = distance
            self.assertAlmostEqual(max_distance, self.max_distance, places=2)

if __name__ == "__main__":
    # Run the tests
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_starts_and_ends_at_depot'))
    test_suite.addTest(TestTSPControlSolution('test_visits_each_city_once'))
    test_suite.addTest(TestTSPSolution('test_output_tour_format'))
    test_suite.addTest(TestTSPSolution('test_total_travel_cost'))
    test_suite.addTest(TestTSPSolution('test_max_distance_between_consecutive_cities'))

    test_runner = unittest.TextTestRunner()
    results = test_runner.run(test_suite)
    
    # Check if all tests are passed
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")