import unittest
import math

class TestTravelingRobotSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
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
        self.tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
        self.reported_cost = 384.7863591860825
        self.reported_max_distance = 78.63841300535

    def test_tour_validity(self):
        # Check if the tour starts and ends at the depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

        # Check if all cities are visited exactly once, except the depot (which appears twice)
        city_visit_counts = {k: 0 for k in range(10)}
        for city in self.tour:
            city_visit_counts[city] += 1

        self.assertEqual(city_visit_counts[0], 2)
        for count in city_visit_counts.values():
            self.assertEqual(count, 1, msg="Each city must be visited exactly once")

    def test_travel_cost(self):
        def euclidean_distance(a, b):
            return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        
        total_calculated_cost = 0.0
        max_calculated_distance = 0.0

        for i in range(len(self.tour)-1):
            distance = euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
            total_calculated_cost += distance
            max_calculated_distance = max(max_calculated_distance, distance)

        # Check total travel cost
        self.assertAlmostEqual(total_calculated_cost, self.reported_cost, places=5)

        # Check maximum distance between consecutive cities
        self.assertAlmostEqual(max_calculated_distance, self.reported_max_distance, places=5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTravelingRobotSolution('test_tour_validity'))
    suite.addTest(TestTravelingRobotSolution('test_travel_cost'))
    
    runner = unittest.TextTestRunner()
    results = runner.run(suite)
    
    return "CORRECT" if results.wasSuccessful() else "FAIL"

# Output the result of the tests
print(run_tests())