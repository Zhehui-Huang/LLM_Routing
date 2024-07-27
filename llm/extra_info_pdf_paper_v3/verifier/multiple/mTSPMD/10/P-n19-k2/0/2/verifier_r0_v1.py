import unittest
from math import sqrt

# Definition of cities with their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def calc_euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def tour_cost(tour):
    return sum(calc_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

class TestRobotTours(unittest.TestCase):
    def test_robot_tours(self):
        # Given solution
        robot0_tour = [0, 14, 3, 17, 16, 8, 12, 6, 18, 0]
        robot1_tour = [1, 4, 11, 10, 5, 9, 7, 2, 15, 13, 1]

        # Requirement 1: Check if each robot starts and ends at its assigned depot
        self.assertEqual(robot0_tour[0], 0)  # start depot
        self.assertEqual(robot0_tour[-1], 0)  # end depot
        self.assertEqual(robot1_tour[0], 1)  # start depot
        self.assertEqual(robot1_tour[-1], 1)  # end depot

        # Requirement 2: Check if all cities are visited exactly once collectively by the robots
        all_cities_visited = set(robot0_tour + robot1_tour)
        expected_cities = set(range(len(cities)))  # Depots included
        self.assertEqual(all_cities_visited, expected_cities)

        # Calculating travel costs
        calculated_robot0_cost = tour_cost(robot0_tour)
        calculated_robot1_cost = tour_cost(robot1_tour)

        # Provided costs for comparison (to ensure calculations are consistent with the given solution)
        given_cost_robot0 = 136.06326526990262
        given_cost_robot1 = 145.56149124095717

        # Requirement 3: Comparing calculated costs with given costs using a small tolerance
        self.assertAlmostEqual(calculated_robot0_cost, given_cost_robot0, places=5)
        self.assertAlmostEqual(calculated_robot1_cost, given_cost_robot1, places=5)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)