import math
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.coordinates = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
            (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
            (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
            (64, 72), (14, 89)
        ]
        self.tour = [0, 19, 8, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 13, 1, 18, 17, 0]
        self.reported_cost = 398.67
    
    def calculate_distance(self, p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at city 0 (depot)")
        self.assertEqual(self.tour[-1], 0, "Tour should end at city 0 (depot)")
    
    def test_visit_each_city_once(self):
        # Since the robot visits each city exactly once except the depot city, and to and from the depot,
        # we should have each city from 1 to 19 exactly once in the tour.
        unique_cities = set(self.tour[1:-1])  # Do not include the starting and ending depot.
        self.assertEqual(len(unique_cities), 19, "Each city except the depot should be visited exactly once.")
        self.assertEqual(set(range(1, 20)), unique_cities, "All cities from 1 to 19 should be visited.")

    def test_total_travel_cost(self):
        total_cost = sum(self.calculate_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]])
                         for i in range(len(self.tour) - 1))
        # We compare the calculated cost with a small threshold for floating point inaccuracies 
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2, msg="Reported cost should match the calculated cost.")
    
    def test_output_format(self):
        # Ensuring that the output format adheres to the [0, ..., 0] followed by total cost.
        self.assertIsInstance(self.tour, list, "Output tour should be a list.")
        self.assertIsInstance(self.reported_body_cost, (float, int), "Output cost should be a numeric type.")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    test_runner = unittest.TextTestRunner()
    results = test_runner.run(test_suite)

    # Print outcome based on the test results
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")