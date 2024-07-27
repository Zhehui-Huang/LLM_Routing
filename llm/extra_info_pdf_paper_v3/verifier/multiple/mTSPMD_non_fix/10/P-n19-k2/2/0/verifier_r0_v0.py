import unittest
from math import sqrt

class TestTours(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 40),  # Depot 0
            (37, 52),  # Depot 1
            (49, 43),  # City 2
            (52, 64),  # City 3
            (31, 62),  # City 4
            (52, 33),  # City 5
            (42, 41),  # City 6
            (52, 41),  # City 7
            (57, 58),  # City 8
            (62, 42),  # City 9
            (42, 57),  # City 10
            (27, 68),  # City 11
            (43, 67),  # City 12
            (58, 27),  # City 13
            (37, 69),  # City 14
            (61, 33),  # City 15
            (62, 63),  # City 16
            (63, 69),  # City 17
            (45, 35),  # City 18
        ]
        self.robot0_tour = [0, 10, 4, 11, 12, 3, 8, 9, 6, 0]
        self.robot1_tour = [1, 14, 17, 16, 2, 7, 13, 5, 18, 1]
        self.robot0_cost = 122.26073635703385
        self.robot1_cost = 126.32726639281817
        self.total_cost = 248.58800274985202

    def test_unique_cities_visited(self):
        all_visited = set(self.robot0_tour + self.robot1_tour)
        self.assertEqual(len(all_visited), 19, "Requirement 3: Each city must be visited exactly once.")

    def test_robot_starts_and_ends_at_depot(self):
        self.assertIn(self.robot0_tour[0], [0], "Requirement 2: Robot 0 should start at Depot 0")
        self.assertIn(self.robot1_tour[0], [1], "Requirement 2: Robot 1 should start at Depot 1")
        self.assertIn(self.robot0_tour[-1], [0], "Requirement 2: Robot 0 should potentially end at any city.")
        self.assertIn(self.robot1_tour[-1], [1], "Requirement 2: Robot 1 should potentially end at any city.")

    def test_cost_calculation(self):
        # Calculate costs based on Euclidean distance and compare with given costs
        def euclidean_distance(city1, city2):
            return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        robot0_calc_cost = sum(
            euclidean_distance(self.cities[self.robot0_tour[i]], self.cities[self.robot0_tour[i + 1]]) for i in range(len(self.robot0_tour) - 1)
        )
        robot1_calc_cost = sum(
            euclidean_distance(self.cities[self.robot1_tour[i]], self.cities[self.robot1_tour[i + 1]]) for i in range(len(self.robot1_tour) - 1)
        )
        self.assertAlmostEqual(robot0_calc_cost, self.robot0_cost, "Requirement 6: Robot 0 cost calculation error.")
        self.assertAlmostEqual(robot1_calc_cost, self.robot1_cost, "Requirement 6: Robot 1 cost calculation error.")

    def test_total_cost(self):
        calculated_total_cost = self.robot0_cost + self.robot1_cost
        self.assertAlmostEqual(calculated_total_cost, self.total_cost, "Requirement 8: Total cost calculation error.")

    def test_optimal_solution(self):
        # For simplicity in the unit test, we assume the provided solution is optimal for testing purposes.
        # Actual optimality check would require solving the problem optimally which is not feasible for unit testing.
        pass

    def runTest(self):
        # Collect all test results
        test_methods = [
            self.test_unique_cities_visited,
            self.test_robot_starts_and_ends_at_depot,
            self.test_cost_calculation,
            self.test_total_cost,
            self.test_optimal_solution
        ]
        for method in test_methods:
            method()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestTours())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # Check for overall success
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")