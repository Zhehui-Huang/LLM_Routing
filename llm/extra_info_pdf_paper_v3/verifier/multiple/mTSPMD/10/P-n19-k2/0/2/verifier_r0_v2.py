import unittest
from math import sqrt

# Dictionary holding city indices and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def calc_euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def tour_cost(tour):
    return sum(calc_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Initialize test results
        self.test_results = True

    def test_robot_tours(self):
        # Given solution
        robot0_tour = [0, 14, 3, 17, 16, 8, 12, 6, 18, 0]
        robot1_tour = [1, 4, 11, 10, 5, 9, 7, 2, 15, 13, 1]

        # Requirement 1 & 2
        self.assertEqual(robot0_tour[0], 0)  # start depot
        self.assertEqual(robot0_tour[-1], 0)  # end depot
        self.assertEqual(robot1_tour[0], 1)  # start depot
        self.assertEqual(robot1_tour[-1], 1)  # end depot

        # Requirement 2: All cities visited exactly once
        all_cities_visited = set(robot0_tour + robot1_tour)
        expected_cities = set(range(len(cities)))  # Depots included
        self.assertEqual(all_cities_visited, expected_cities)

        # Requirement 3: Travel cost comparisons (checking if the calculations are consistent with the given costs)
        given_cost_robot0 = 136.06326526990262
        given_cost_robot1 = 145.56149124095717
        calculated_robot0_cost = tour_cost(robot0_tour)
        calculated_robot1_cost = tour_cost(robot1_tour)

        self.assertAlmostEqual(calculated_robot0_cost, given_cost_robot0, places=5)
        self.assertAlmostEqual(calculated_robot1_cost, given_cost_robot1, places=5)

    def tearDown(self):
        if not self._outcome.success:
            self.test_results = False

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTours))
    runner = unittest.TextTestRunner()

    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")