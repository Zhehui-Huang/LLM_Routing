import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (50, 42),
            1: (41, 1),
            2: (18, 46),
            3: (40, 98),
            4: (51, 69),
            5: (47, 39),
            6: (62, 26),
            7: (79, 31),
            8: (61, 90),
            9: (42, 49)
        }
        self.tour = [0, 9, 5, 6, 0]
        self.reported_cost = 61.66

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot.")

    def test_tour_includes_exactly_four_cities(self):
        self.assertEqual(len(set(self.tour)), 4, "Tour does not include exactly 4 cities.")

    def test_travel_distance_correctness(self):
        total_calculated_cost = 0
        for i in range(len(self.tour) - 1):
            start = self.cities[self.tour[i]]
            end = self.cities[self.tour[i + 1]]
            total_calculated_cost += euclidean_distance(start, end)
        rounded_calculated_cost = round(total_calculated_cost, 2)
        
        # Check if the provided cost matches the calculated cost
        self.assertEqual(rounded_calculated_cost, self.reported_cost, "Reported travel cost is incorrect.")
        
        # Additional validation that the computed total matches expected value from a completed test
        expected_cost = 61.66  # This should match the sum of the correct distances calculated
        self.assertAlmostEqual(rounded_calculated , expected_cost, places=2, "Calculated travel cost does not match expected value.")

def run_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotTour('test_tour_starts_and_ends_at_depot'))
    test_suite.addTest(TestRobotTour('test_tour_includes_exactly_four_cities'))
    test_suite.addTest(TestRobotTour('test_travel_distance_correctness'))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_test_suite()