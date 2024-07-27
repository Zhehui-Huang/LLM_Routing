import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (16, 90), # Depot city 0
            (43, 99),
            (80, 21),
            (86, 92),
            (54, 93),
            (34, 73),
            (6, 61),
            (86, 69),
            (30, 50),
            (35, 73),
            (42, 64),
            (64, 30),
            (70, 95),
            (29, 64),
            (32, 79)
        ]
        self.tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
        self.provided_total_cost = 373.61498801130097

    def test_tour_visits_each_city_once(self):
        # Excluding the depot city, which should appear twice (start, end)
        cities_visited = self.tour[1:-1]  # Remove first/last which are the depot
        self.assertEqual(len(set(cities_visited)), 14)  # Should visit 14 unique cities

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_total_travel_cost_correct(self):
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
        self.assertAlmostEqual(total_cost, self.provided_total_cost, places=5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRobotTourSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Run the tests to determine if the provided tour and cost are correct
print(run_tests())