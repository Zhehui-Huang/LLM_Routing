import unittest
import math

# Coordinates for each city, indexed by city number
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Tours and costs from the solution provided
        robot_0_tour = [0, 16, 6, 20, 2, 10, 12, 4, 8, 18, 14, 0]
        robot_1_tour = [1, 15, 11, 3, 19, 13, 9, 17, 5, 7, 1]
        
        # Calculate the costs from tours
        robot_0_cost_calculated = calculate_total_travel_cost(robot_0_tour)
        robot_1_cost_calculated = calculate_total_travel_cost(robot_1_tour)
        total_cost_calculated = robot_0_cost_calculated + robot_1_cost_calculated
        
        # Provided costs
        robot_0_cost_provided = 171.820768703562
        robot_1_cost_provided = 137.90549546878637
        total_cost_provided = 309.72626417234835
        
        # Check Requirements
        # Req 1: Check if robots start and end at their depots
        self.assertEqual(robot_0_tour[0], 0)
        self.assertEqual(robot_0_tour[-1], 0)
        self.assertEqual(robot_1_tour[0], 1)
        self.assertEqual(robot_1_tour[-1], 1)
        
        # Req 2: Check if all cities are visited exactly once
        all_visited_cities = sorted(robot_0_tour[1:-1] + robot_1_tour[1:-1])
        self.assertEqual(all_visited_cities, list(range(2, 21)))
        
        # Req 3 & 5: Check if the cost calculations are correct
        self.assertAlmostEqual(robot_0_cost_calculated, robot_0_cost_provided, places=5)
        self.assertAlmostEqual(robot_1_cost_calculated, robot_1_cost_provided, places=5)
        self.assertAlmostEqual(total_cost_calculated, total_cost_provided, places=5)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_solution'))
    result = unittest.TextTestRunner().run(suite)
    
    # Output result according to the solution's correctness
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")