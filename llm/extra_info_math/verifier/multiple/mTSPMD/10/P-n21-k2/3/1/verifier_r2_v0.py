import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # City Coordinates
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
            16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }

        # Robot tours
        self.robot_tours = {
            0: [0, 6, 7, 5, 9, 2, 10, 4, 3, 8, 0],
            1: [1, 16, 20, 14, 17, 13, 18, 19, 12, 15, 11, 1]
        }

        # Expected travel costs
        self.expected_costs = {
            0: 142.33,
            1: 133.34
        }

    def test_starts_and_ends_at_depot(self):
        for robot, tour in self.robot_tours.items():
            self.assertEqual(tour[0], tour[-1], f"Robot {robot} does not start and end at depot.")

    def test_visit_all_cities_once(self):
        all_visited_cities = sum(self.robot_tours.values(), [])
        unique_cities = set(all_visited_cities)
        expected_visited = set(range(21))
        self.assertEqual(unique_cities, expected_visited, "All cities are not visited exactly once or are visited more than once.")

    def test_minimize_total_travel_cost(self):
        for robot, tour in self.robot_tours.items():
            actual_cost = 0
            for i in range(len(tour) - 1):
                city1, city2 = tour[i], tour[i + 1]
                actual_cost += sqrt((self.cities[city1][0] - self.cities[city2][0])**2 + (self.cities[city1][1] - self.cities[city2][1])**2)
            self.assertAlmostEqual(actual_cost, self.expected_costs[robot], delta=1e-2, msg=f"Total travel cost for Robot {robot} is incorrect.")

    def test_overall_solution_correctness(self):
        self.test_starts_and_ends_at_depot()
        self.test_visit_all_cities_once()
        self.test_minimize_total_travel_cost()
        print("CORRECT")

    def runTest(self):
        self.test_overall_solution_correctness()

# Run the test
test = TestRobotTours()
test.runTest()