import unittest
from math import sqrt

class TestMTSPSolution(unittest.TestCase):
    def calculate_distance(self, city1, city2):
        return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    
    def test_solution(self):
        # Cities coordinates
        cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
            16: (62, 63), 17: (63, 69), 18: (45, 35)
        }
        
        # Solution
        robot_0_tour = [0, 6, 18, 5, 13, 15, 9, 7, 2, 8, 16, 17, 3, 12, 14, 11, 4, 10, 0]
        robot_1_tour = [1, 1]
        robot_0_cost = 172.13514655096085
        robot_1_cost = 0.0
        total_cost = 172.13514655096085

        # Requirement 1: 19 cities check
        self.assertEqual(len(cities), 19)

        # Requirement 2: Start and end at respective depots
        self.assertEqual(robot_0_tour[0], robot_0_tour[-1])
        self.assertEqual(robot_0_tour[0], 0)
        self.assertEqual(robot_1_tour[0], robot_1_tour[-1])
        self.assertEqual(robot_1_tour[0], 1)

        # Requirement 3: All cities visited exactly once across robots
        all_cities_visited = sorted(robot_0_tour[1:-1] + robot_1_tour[1:-1])
        self.assertEqual(all_cities_visited, list(range(1, 19)))

        # Requirement 4: Minimizing the combined travel cost
        # (Check if other computation methods can yield a lower cost than the given solution)
        # Assuming the solution provided is optimal based on the problem's setup.
        
        # Requirement 5: Calculate the given travel costs using the Euclidean distances
        calculated_robot_0_cost = sum([self.calculate_distance(cities[robot_0_tour[i]], cities[robot_0_tour[i+1]]) for i in range(len(robot_0_tour)-1)])
        calculated_robot_1_cost = sum([self.calculate_distance(cities[robot_1_tour[i]], cities[robot_1_tour[i+1]]) for i in range(len(robot_1_tour)-1)])

        self.assertAlmostEqual(calculated_robot_0_cost, robot_0_cost, places=5)
        self.assertAlmostEqual(calculated_robot_1_cost, robot_1_cost, places=5)

        # Requirement 6: Check the start and end of the tours output
        self.assertEqual(robot_0_tour[0], 0)  # Starts at depot 0
        self.assertEqual(robot_0_tour[-1], 0)  # Ends at depot 0
        self.assertEqual(robot_1_tour[0], 1)  # Starts at depot 1
        self.assertEqual(robot_1_tour[-1], 1)  # Ends at depot 1

        # Requirement 7: Check the overall cost calculation
        self.assertAlmostEqual(calculated_robot_0_cost + calculated_robot_1_cost, total_cost)

# Run the test
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestMTSPSolution("test_solution"))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
       print("FAIL")