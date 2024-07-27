import unittest
from math import sqrt

class TestBottleneckTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (50, 42),  # Depot City 0
            (41, 1),   # City 1
            (18, 46),  # City 2
            (40, 98),  # City 3
            (51, 69),  # City 4
            (47, 39),  # City 5
            (62, 26),  # City 6
            (79, 31),  # City 7
            (61, 90),  # City 8
            (42, 49)   # City 9
        ]
        self.tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
        self.provided_total_cost = 328.3966856465968
        self.provided_max_distance = 45.18849411078001

    def test_cities_visited_once(self):
        # Check if all cities except depot city are visited exactly once and starts/ends at depot city
        unique_cities = set(self.tour)
        self.assertTrue(len(unique_cities) == len(self.cities) and self.tour.count(0) == 2)

    def test_minimized_max_distance(self):
        # Calculate the maximum distance between consecutive cities
        def distance(city1, city2):
            return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        actual_max_distance = max(
            distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]]) for i in range(len(self.tour) - 1)
        )
        self.assertEqual(actual_max_distance, self.provided_max_distance)

    def test_correct_output_format(self):
        # Verify the total distance and output format
        calculated_total_distance = sum(
            sqrt((self.cities[self.tour[i]][0] - self.cities[self.tour[i+1]][0])**2 +
                 (self.cities[self.tour[i]][1] - self.cities[self.tour[i+1]][1])**2)
            for i in range(len(self.tour) - 1)
        )
        
        self.assertAlmostEqual(calculated_total_distance, self.provided_total_cost)

    def test_solution(self):
        try:
            self.test_cities_visited_once()
            self.test_minimized_max_distance()
            self.test_correct_output_format()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# Running the tests
test_suite = unittest.TestSuite()
test_suite.addTest(TestBottleneckTSPSolution('test_solution'))

runner = unittest.TextTestRunner()
runner.run(test_suite)