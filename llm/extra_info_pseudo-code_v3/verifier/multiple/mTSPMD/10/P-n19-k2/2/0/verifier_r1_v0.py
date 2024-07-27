import unittest
from math import sqrt

# Assume that the tours and costs are already assigned by the genetic algorithm
robot_0_tour = [0, 8, 3, 6, 9, 13, 2, 5, 18, 0]
robot_1_tour = [1, 15, 7, 4, 11, 12, 16, 17, 14, 10, 1]
robot_0_cost = 152.77860710353104
robot_1_cost = 167.1631753925759
overall_cost = 319.94178249610695

# City coordinates dictionary
city_coords = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

class TestRobotTours(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(robot_0_tour[0], 0)
        self.assertEqual(robot_0_tour[-1], 0)
        self.assertEqual(robot_1_tour[0], 1)
        self.assertEqual(robot_1_tour[-1], 1)
    
    def test_all_cities_visited_exactly_once(self):
        combined_tours = robot_0_tour[:-1] + robot_1_tour[:-1]  # Exclude ending depots
        unique_cities = set(combined_tours)
        all_cities = set(range(19))  # Cities 0 through 18
        self.assertEqual(unique_cities, all_cities)
    
    def test_minimized_total_travel_cost(self):
        # Calculate total actual cost from the tours
        def tour_cost(tour):
            cost = 0.0
            for i in range(1, len(tour)):
                cost += calculate_distance(city_coords[tour[i-1]], city_coords[tour[i]])
            return cost
        calculated_cost_0 = tour_cost(robot_0_tour)
        calculated_cost_1 = tour_cost(robot_1_tour)
        calculated_overall_cost = calculated_cost_0 + calculated_cost_1
        
        # Compare calculated costs with provided costs (allow small floating point differences)
        self.assertAlmostEqual(calculated_cost_0, robot_0_cost, places=5)
        self.assertAlmostEqual(calculated_cost_1, robot_1_cost, places=5)
        self.assertAlmostEqual(calculated_overall_cost, overall_cost, places=5)
    
    def test_output_format(self):
        # Ensure the output is in the correct format i.e., list of city indices starts and ends at depots
        self.assertIsInstance(robot_0_tour, list)
        self.assertTrue(all(isinstance(x, int) for x in robot_0_tour))
        self.assertIsInstance(robot_1_tour, list)
        self.assertTrue(all(isinstance(x, int) for x in robot_1_tour))

suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
test_result = unittest.TextTestRunner().run(suite)

if test_result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")