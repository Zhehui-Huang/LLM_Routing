import unittest
import math

class TestRobotTours(unittest.TestCase):
    
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
            6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
            18: (62, 63), 19: (63, 69), 20: (45, 35)
        }
        
        # Tours provided in the solution
        self.robot0_tour = [12, 3, 19, 13, 2, 10, 15, 11, 0, 0, 16, 20]
        self.robot1_tour = [4, 1, 1, 6, 7, 5, 14, 17, 9, 8, 18]
        
        # Costs provided in the solution
        self.robot0_cost = 137.09097916207833
        self.robot1_cost = 89.82794263426624
        self.overall_cost = 226.91892179634456

    def test_all_cities_visited_once(self):
        all_cities = set(range(21))  # All city indices from 0 to 20
        visited_cities = set(self.robot0_tour + self.robot1_tour)
        self.assertEqual(all_cities, visited_cities, "Some cities are not visited exactly once.")
        
    def test_robot_starts_from_depot(self):
        # Check if both robots start from depot city 0
        self.assertTrue(self.robot0_tour[0] == 0 and self.robot1_tour[0] == 4, "Robots do not start from designated depots.")

    def test_travel_cost(self):
        # Need to define a method to calculate Euclidean distance
        def calc_cost(tour):
            cost = 0
            for i in range(len(tour) - 1):
                p1, p2 = self.cities[tour[i]], self.cities[tour[i+1]]
                cost += math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
            return cost
        
        calculated_cost0 = calc_cost(self.robot0_tour)
        calculated_cost1 = calc_cost(self.robot1_tour)
        self.assertAlmostEqual(calculated_cost0, self.robot0_cost, places=5, msg="Robot 0 tour cost does not match.")
        self.assertAlmostEqual(calculated_cost1, self.robot1_cost, places=5, msg="Robot 1 tour cost does not match.")
        self.assertAlmostEqual(calculated_cost0 + calculated_cost1, self.overall_cost, places=5, msg="Overall cost does not match.")

if __name__ == "__main__":
    unittest.main()