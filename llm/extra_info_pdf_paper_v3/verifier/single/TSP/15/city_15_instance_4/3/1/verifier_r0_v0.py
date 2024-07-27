import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
            (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
            (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
        ]
        self.tour = [0, 1, 5, 9, 2, 7, 10, 8, 3, 6, 14, 13, 11, 12, 4, 0]
        self.reported_cost = 413.62

    def test_tour_length(self):
        # Test that all cities are visited exactly once, except depot which is the start and end
        tour_visits = [0] * len(self.coordinates)
        for city in self.tour:
            tour_visits[city] += 1
        # Checking that each city from 1 to 14 is visited exactly once
        self.assertEqual(tour_visits[1:], [1] * 14)
        # Checking that the starting city (depot) is visited twice
        self.assertEqual(tour_visits[0], 2)

    def test_tour_cost(self):
        # Calculate the total tour cost using the Euclidean distance formula
        def distance(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        calc_cost = 0
        for i in range(len(self.tour) - 1):
            city1, city2 = self.tour[i], self.tour[i + 1]
            calc_cost += distance(self.coordinates[city1], self.coordinates[city2])
        
        # Compare the calculated cost with the reported cost
        # Allow a small error margin due to possible rounding differences
        self.assertAlmostEqual(calc_cost, self.reported_cost, places=2)

    def test_output_format_correct(self):
        # Check that the output format is a list starting and ending at the depot
        self.assertEqual(self.tour[0], self.tour[-1])
        self.assertEqual(self.tour[0], 0)

    def run_all_tests(self):
        test_methods = [method for method in dir(self) if method.startswith('test_')]
        for method in test_methods:
            try:
                getattr(self, method)()
                print(f'{method}: PASS')
            except AssertionError as e:
                print(f'{method}: FAIL - {str(e)}')
                return "FAIL"
        return "CORRECT"

# Create the test object
test_tsp = TestTSPSolution()
# Running all unit tests
result = test_tsp.run_all_tests()
# Output test result
print(result)