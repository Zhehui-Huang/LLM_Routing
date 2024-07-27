import unittest
import math

# City coordinates as given in the problem
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Proposed solution for robot tours
robot_0_tour = [0, 6, 2, 7, 5, 9, 8, 3, 4, 0]
robot_1_tour = [1, 10, 12, 14, 11, 16, 17, 15, 13, 18, 1]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate total travel cost of a tour
def calculate_total_travel_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestRobotTours(unittest.TestCase):
    def test_start_and_end_depot(self):
        self.assertEqual(robot_0_tour[0], 0)
        self.assertEqual(robot_0_tour[-1], 0)
        self.assertEqual(robot_1_tour[0], 1)
        self.assertEqual(robot_1_tour[-1], 1)

    def test_unique_visit(self):
        all_cities = set(range(19))
        visited_cities = set(robot_0_tour + robot_1_tour)
        visited_cities.discard(0)
        visited_cities.discard(1)
        self.assertEqual(all_cities, visited_cities)

    def test_minimize_total_combined_travel_cost(self):
        robot_0_cost = calculate_total_travel_cost(robot_0_tour)
        robot_1_cost = calculate_total_travel_cost(robot_1_tour)
        expected_total_cost = robot_0_cost + robot_1_cost
        self.assertAlmostEqual(expected_total_cost, 263.82, places=2)

    def test_tour_representation_and_travel_cost_output(self):
        robot_0_cost = calculate_total_travel_cost(robot_0_tour)
        self.assertAlmostEqual(robot_0_cost, 112.07, places=2)
        robot_1_cost = calculate_total_travel_cost(robot_1_tour)
        self.assertAlmostEqual(robot_1_cost, 151.75, places=2)

# Run the tests
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestRobotTours))
runner = unittest.TextTestRunner()
result = runner.run(suite)

if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")