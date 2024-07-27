import unittest
import math

class TestSolutionValidity(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (9, 93),
            1: (8, 51),
            2: (74, 99),
            3: (78, 50),
            4: (21, 23),
            5: (88, 59),
            6: (79, 77),
            7: (63, 23),
            8: (19, 76),
            9: (21, 38),
            10: (19, 65),
            11: (11, 40),
            12: (3, 21),
            13: (60, 55),
            14: (4, 39)
        }
        # Provided solution
        self.tour = [0, 14, 1, 8, 0]
        self.reported_cost = 113.92

    def test_tour_length(self):
        self.assertEqual(len(self.tour), 5)  # Tour length includes return to depot

    def test_visit_exactly_4_cities(self):
        # Unique cities visited (excluding depot return)
        unique_cities = set(self.tour[:-1])
        self.assertEqual(len(unique_cities), 4)

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_calculate_cost(self):
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city_a = self.cities[self.tour[i]]
            city_b = self.cities[self.tour[i+1]]
            calculated_cost += euclidean_distance(city_a, city_b)

        # Comparing reported vs calculated with a tolerance for floating point arithmetic
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2)

    def test_correct_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertTrue(all(isinstance(x, int) for x in self.tour))
        self.assertIsInstance(self.reported_cost, float)

# Running the tests to validate the tour and cost.
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestSolutionValidity))

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Determine output based on test results
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")