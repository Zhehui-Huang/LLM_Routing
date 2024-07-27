import unittest
import math

# Helper function to calculate Euclidean distance between two cities by coordinates
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }
        # Tours provided in the solution
        self.robot_0_tour = [0, 20, 4, 8, 19, 18, 15, 3, 17, 14, 0]
        self.robot_1_tour = [1, 10, 11, 12, 9, 13, 16, 2, 6, 5, 7, 1]
        self.robot_0_cost = 202.52
        self.robot_1_cost = 161.85
        self.total_cost = 364.37

    def test_robot_tours_start_end_depot(self):
        # Test if each tour starts and ends at a depot
        self.assertTrue(self.robot_0_tour[0] == 0 and self.robot_0_tour[-1] == 0)
        self.assertTrue(self.robot_1_tour[0] == 1 and self.robot_1_tour[-1] == 1)
    
    def test_all_cities_visited_once(self):
        # Test if all cities except depots are visited exactly once across both robots
        all_visited_cities = sorted(self.robot_0_tour + self.robot_1_tour)
        expected_cities = sorted(list(self.cities.keys()) * 2)  # Each city should appear twice as they are start and end points
        self.assertEqual(all_visited_cities, expected_cities)

    def test_travel_costs(self):
        # Test the accuracy of travel costs calculations
        def calculate_tour_cost(tour):
            cost = 0
            for i in range(len(tour) - 1):
                cost += euclidean_distance(self.cities[tour[i]], self.cities[tour[i + 1]])
            return cost
        
        calc_robot_0_cost = calculate_tour_cost(self.robot_0_tour)
        calc_robot_1_cost = calculate_tour_cost(self.robot_1_tour)
        calc_total_cost = round(calc_robot_0_cost + calc_robot_1_cost, 2)

        self.assertAlmostEqual(calc_robot_0_cost, self.robot_0_cost, places=2)
        self.assertAlmostEqual(calc_robot_1_cost, self.robot_1_cost, places=2)
        self.assertAlmostEqual(calc_total_cost, self.total_cost, places=2)

    def test_solution(self):
        self.test_robot_tours_start_end_depot()
        self.test_all_cities_visited_once()
        self.test_travel_costs()
        print("CORRECT")

# Run the tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)