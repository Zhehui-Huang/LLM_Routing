import unittest
from math import sqrt

# Provided solution data
robot_0_tour = [0, 1, 3, 4, 8, 10, 11, 12, 15, 18, 19, 0]
robot_0_cost = 212.21732723337922
robot_1_tour = [0, 2, 5, 6, 7, 9, 13, 14, 16, 17, 20, 0]
robot_1_cost = 184.31166515759514
overall_cost = 396.5289923909744

# Define all cities and their coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_cost(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += calculate_distance(tour[i], tour[i + 1])
    return total_dist

class TestRobotTourSolution(unittest.TestCase):
    def test_visitation(self):
        all_cities = set(city_coordinates.keys()) - {0}  # exclude depot
        visited_cities = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])
        self.assertEqual(all_cities, visited_cities, "Each city must be visited exactly once.")

    def test_trip_starts_ends_at_depot(self):
        self.assertTrue(all(tour[0] == 0 and tour[-1] == 0 for tour in [robot_0_tour, robot_1_tour]), "Each tour should start and end at the depot.")

    def test_total_costs(self):
        calculated_robot_0_cost = calculate_total_cost(robot_0_tour)
        calculated_robot_1_cost = calculate_total_cost(robot_1_tour)
        calculated_overall_cost = calculated_robot_0_cost + calculated_robot_1_cost
        self.assertAlmostEqual(calculated_robot_0_cost, robot_0_cost, delta=0.001, msg="Cost for robot 0 is incorrect.")
        self.assertAlmostEqual(calculated_robot_1_cost, robot_1_cost, delta=0.001, msg="Cost for robot 1 is incorrect.")
        self.assertAlmostEqual(overall_cost, calculated_overall_cost, delta=0.001, msg="Overall cost is incorrect.")

def run_tests():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(TestRobotTourSolution))
    result = unittest.TextTestRunner().run(test_suite)
    
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Calling the run_tests function to execute the unit tests and print the result.
print(run_tests())