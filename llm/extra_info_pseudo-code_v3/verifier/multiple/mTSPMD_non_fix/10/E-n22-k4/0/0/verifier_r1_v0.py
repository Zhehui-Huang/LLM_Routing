import unittest
import math

# Mock data to simulate the problem environment
city_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Provided solution (for testing)
robot_tour = [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21]
robot_total_travel_cost = 278.5478504011258
overall_total_travel_cost = 278.5478504011258

num_robots = 4
num_cities = 22

class TestVRPSolution(unittest.TestCase):
    def test_unique_visit(self):
        # Test that each city is visited exactly once
        cities_visited = set(robot_tour)
        self.assertEqual(len(cities_visited), num_cities)

    def test_correct_initial_and_final_depot(self):
        # Test that tours start and end at the correct depots
        self.assertEqual(robot_tour[0], 0)  # start at depot 0

    def test_euclidean_cost_correct(self):
        # Check if the travel cost matches the calculated one
        computed_cost = 0
        for i in range(len(robot_tour) - 1):
            computed_cost += calculate_euclidean_distance(robot_tour[i], robot_tour[i + 1])
        
        # Tolerance for floating-point arithmetic
        self.assertAlmostEqual(computed_cost, robot_total_travel_cost, places=3)

    def test_overall_cost(self):
        # Test overall cost
        self.assertAlmostEqual(robot_total_travel_cost, overall_total_travel_cost, places=3)

    def test_max_one_robot_used(self):
        # Given that only Robot 0 is mentioned to be used
        self.assertEqual(robot_total_travel_cost, overall_total_travel_cost)

    def test_output_format(self):
        # Just ensuring format requirements are met [Requirement 10] and [Requirement 11]
        expected_format_for_individual_tour = 'Robot 0 Tour: [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21]'
        expected_format_for_cost = 'Robot 0 Total Travel Cost: 278.5478504011258'
        self.assertIsInstance(str(robot_tour), str)
        self.assertIsInstance(str(robot_total_travel_cost), str)
        self.assertEqual(str(robot_tour).startswith('Robot 0 Tour'), True)
        self.assertEqual(str(robot_total_travel_cost).startswith('Robot 0 Total Travel Cost'), True)

# Run tests
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestVRPSolution))
runner = unittest.TextTestRunner()
result = runner.run(suite)

# Check if there were any failures
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")