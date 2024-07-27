import unittest
from math import sqrt

# Provided solution tours and costs
robot_0_tour = [0, 7, 5, 20, 16, 11, 4, 10, 15, 12]
robot_0_cost = 144
robot_1_tour = [1, 3, 19, 18, 8, 2, 6, 14, 17, 9, 13]
robot_1_cost = 133
overall_cost = 276

# City coordinates as provided
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

def calculate_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestRobotTourSolution(unittest.TestCase):
    def test_unique_cities(self):
        # Requirement 4: Each city must be visited exactly once by any of the robots
        all_cities_visited = set(robot_0_tour + robot_1_tour)
        self.assertEqual(len(all_cities_visited), 21)
    
    def test_tour_departure_from_depot(self):
        # Requirement 2 and 5: Robots should start at a specific depot
        self.assertEqual(robot_0_tour[0], 0)
        self.assertEqual(robot_1_tour[0], 1)

    def test_tour_coverage(self):
        # Requirement 3: Each robot covers all cities collectively
        all_cities = set(range(21))
        visited_cities = set(robot_0_tour + robot_1_tour)
        self.assertEqual(all_cities, visited_cities)

    def test_total_cost(self):
        # Requirement 6 and 7: Checking the total costs
        calc_robot_0_cost = calculate_tour_cost(robot_0_tour + [robot_0_tour[-1]])
        calc_robot_1_cost = calculate_tour_cost(robot_1_tour + [robot_1_tour[-1]])
        self.assertAlmostEqual(calc_robot_0_cost, robot_0_cost, places=1)
        self.assertAlmostEqual(calc_robot_1_cost, robot_1_cost, places=1)
        self.assertEqual(calc_robot_0_cost + calc_robot_1_cost, overall_cost)

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTourSolution)
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")