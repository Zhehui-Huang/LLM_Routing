import unittest
import math

# Define the cities coordinates, including two depots
cities = [
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
    (45, 35)   # City 18
]

# Define the robots tour data as provided
robot_0_tour = [0, 15, 7, 8, 16, 18, 10, 11, 9, 0]
robot_0_cost = 162.221787093763

robot_1_tour = [1, 6, 13, 14, 5, 4, 12, 1]
robot_1_cost = 124.22269399010564

overall_cost = 286.44448108386865

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_tour_cost(tour, cities):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
    return total_cost

class TestRobotRouteSolution(unittest.TestCase):
    def test_tour_completeness(self):
        all_cities = set(range(19))  # total 19 cities, including depots
        visited_cities = set(robot_0_tour + robot_1_tour)
        self.assertEqual(all_cities, visited_cities, "Not all cities were visited exactly once")

    def test_start_at_depot(self):
        self.assertEqual(robot_0_tour[0], 0, "Robot 0 should start at depot city 0")
        self.assertEqual(robot_1_tour[0], 1, "Robot 1 should start at depot city 1")

    def test_optimized_travel_cost(self):
        calculated_cost_0 = calculate_total_tour_cost(robot_0_tour, cities)
        calculated_cost_1 = calculate_total_tour_cost(robot_1_tour, cities)
        self.assertAlmostEqual(calculated_cost_0, robot_0_cost, delta=0.001, msg="Robot 0 cost not as expected")
        self.assertAlmostEqual(calculated_cost_1, robot_1_cost, delta=0.001, msg="Robot 1 cost not as expected")
        self.assertAlmostEqual(calculated_cost_0 + calculated_cost_1, overall_cost, delta=0.001, msg="Overall travel cost not as expected")

# Running the tests
if __name__ == '__main__':
    unittest.main()