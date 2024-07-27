import unittest
import math

class TestMTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
            (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
            (61, 33), (62, 63), (63, 69), (45, 35)
        ]
        self.robot0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 16, 0]
        self.robot1_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 0]
        self.expected_robot0_cost = 142.067115100104
        self.expected_robot1_cost = 143.35854658836402
        self.expected_overall_cost = 285.42566168846804

    def compute_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def test_robot_tours_start_end_at_depot(self):
        self.assertEqual(self.robot0_tour[0], self.robot0_tour[-1])
        self.assertEqual(self.robot1_tour[0], self.robot1_tour[-1])
        self.assertEqual(self.robot0_tour[0], 0)
        self.assertEqual(self.robot1_tour[0], 0)

    def test_total_travel_cost(self):
        robot0_cost = sum(self.compute_distance(self.coordinates[self.robot0_tour[i]], self.coordinates[self.robot0_tour[i + 1]]) for i in range(len(self.robot0_tour) - 1))
        robot1_cost = sum(self.compute_distance(self.coordinates[self.robot1_tour[i]], self.coordinates[self.robot1_tour[i + 1]]) for i in range(len(self.robot1_tour) - 1))
        total_cost = robot0_cost + robot1_cost
        self.assertAlmostEqual(robot0_cost, self.expected_robot0_cost, places=5)
        self.assertAlmostEqual(robot1_cost, self.expected_robot1_cost, places=5)
        self.assertAlmostEqual(total_cost, self.expected_overall_cost, places=5)

    def test_no_city_is_unvisited(self):
        all_visited = set(self.robot0_tour[1:-1] + self.robot1_tour[1:-1])
        self.assertEqual(len(all_visited), 18)  # Check if 18 unique cities visited

    def test_no_city_is_visited_more_than_once(self):
        combined_tour = self.robot0_tour + self.robot1_tour
        for city in set(combined_tour):
            # Expect exactly 2 visits for depot and 1 visit for all other cities
            expected_visits = 2 if city == 0 else 1
            self.assertEqual(combined_tour.count(city), expected_visits)

    def test_all_cities_included(self):
        all_cities = set(range(19)) # Cities 0 through 18
        visited_cities = set(self.robot0_tour + self.robot1_tour)
        self.assertEqual(visited_cities, all_cities)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

print(run_tests())