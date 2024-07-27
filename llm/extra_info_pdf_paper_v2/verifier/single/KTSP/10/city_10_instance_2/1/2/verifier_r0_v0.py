import unittest
import math

class TestKTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 8, 5, 2, 1, 9, 0]
        self.total_cost = 183.85
        self.coordinates = {
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

    def test_starts_and_ends_at_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_includes_exactly_six_cities(self):
        # Requirement 2
        self.assertEqual(len(set(self.tour)), 6)

    def test_tour_output_format(self):
        # Requirement 5
        self.assertIsInstance(self.tour, list)
        # Check if all items are integers
        self.assertTrue(all(isinstance(city, int) for city in self.tour))

    def test_cost_output(self):
        # Requirement 6
        self.assertIsInstance(self.total_cost, float)

    def calculate_distance(self, a, b):
        return math.sqrt((self.coordinates[b][0] - self.coordinates[a][0]) ** 2 + (self.coordinates[b][1] - self.coordinates[a][1]) ** 2)

    def test_correct_total_travel_cost(self):
        # Requirement 4
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += self.calculate_distance(self.tour[i], self.tour[i + 1])
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=2)

    def test_solution_is_correct(self):
        try:
            self.test_starts_and_ends_at_depot()
            self.test_tour_includes_exactly_six_cities()
            self.test_tour_output_format()
            self.test_cost_output()
            self.test_correct_total_travel_cost()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# Run the tests
if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestKTravelingSalesmanSolution('test_solution_is_correct'))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)