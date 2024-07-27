import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        self.tour = [0, 4, 2, 1, 7, 3, 8, 0]
        self.total_cost_provided = 159.97188184793015

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visited_exactly_7_cities_including_depot(self):
        self.assertEqual(len(set(self.tour)), 7)

    def test_all_visited_cities_exist_and_unique_visit(self):
        all_cities_are_valid = all(city in self.cities for city in set(self.tour))
        self.assertTrue(all_cities_are_valid)

    def test_total_travel_cost_is_correct(self):
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        tour_length = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(tour_length, self.total_cost_provided, places=5)

# Set up the test suite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestKTSPSolution))

# Define a test runner
runner = unittest.TextTestRunner()

# Run the tests
result = runner.run(suite)

# Evaluate the results
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")