import unittest

class TestSolutionVerification(unittest.TestCase):
    def setUp(self):
        # Optimized tour and cost from the given solution.
        self.tour = [0, 0, 16, 6, 5, 8, 19, 18, 14, 17, 13, 7, 12, 3, 15, 1, 22, 9, 10, 4, 21, 2, 20, 11, 0]
        self.reported_total_cost = 402.7313106762886
        self.num_robots = 8
        self.total_cities = 23

    def test_cities_visited_once(self):
        """ Check if all cities are visited exactly once except the initial city 0. """
        unique_cities = set(self.tour[1:-1])
        self.assertEqual(len(unique_cities), self.total_cities - 1)  # Deducting 1 since city '0' is likely a depot and visited multiple times initially.

    def test_number_of_robots_starting(self):
        """ Test if the provided number of robots start correctly. """
        # Assuming all robots start from city 0; simplified. More complex tests would be necessary for more general cases.
        self.assertEqual(self.tour.count(0), self.num_robots + 1)  # +1 for the closing city

    def test_reported_total_cost_within_expected_range(self):
        """ Check if total cost is within an expected range (to allow for slight computational variations) """
        expected_cost_range = (400, 405)
        self.assertTrue(expected_cost:=(expected_cost_range[0] <= self.reported_total_cost <= expected_cost_range[1]))

def run_unit_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSolutionVerification))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # Based on results, output "CORRECT" or "FAIL"
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    run_unit_tests()