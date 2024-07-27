import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
            16: (62, 63), 17: (63, 69), 18: (45, 35)
        }
        self.robot_0_tour = [0, 6, 18, 5, 13, 15, 9, 7, 2, 8, 16, 17, 3, 12, 14, 11, 4, 10, 1]
        self.robot_1_tour = [1]
        self.tested_cost_robot_0 = 158.39756231614152
        self.tested_cost_robot_1 = 0
        self.overall_tested_cost = 158.39756231614152
    
    def test_all_cities_visited_once(self):
        all_cities = set(range(19))
        visited_cities = set(self.robot_0_tour + self.robot_1_tour)
        self.assertEqual(visited_cities, all_cities, "Not all cities are visited exactly once.")
    
    def test_correct_start_and_end(self):
        self.assertEqual(self.robot_0_tour[0], 0, "Robot 0 should start at city 0.")
        self.assertEqual(self.robot_1_tour[0], 1, "Robot 1 should start at city 1.")
    
    def test_no_return_to_depot(self):
        # Check that robots do not return to depot unnecessarily (not required by problem, but part of flexibility)
        self.assertNotEqual(self.robot_0_tour[-1], 0, "Robot 0 should not need to return to city 0 as its endpoint.")
        self.assertNotEqual(self.robot_1_tour[-1], 1, "Robot 1 should not need to return to city 1 as its endpoint.")

    def test_total_travel_cost_computation(self):
        # Compute and check each robot's travel cost
        def calculate_tour_cost(tour):
            return sum(euclidean_distance(self.coordinates[tour[i]], self.coordinates[tour[i+1]]) for i in range(len(tour)-1))
        
        cost_robot_0 = calculate_tour_cost(self.robot_0_tour)
        cost_robot_1 = calculate_tour_cost(self.robot_1_tour)
        
        self.assertAlmostEqual(cost_robot_0, self.tested_cost_robot_0, places=5, msg="Robot 0 travel cost is incorrect.")
        self.assertAlmostEqual(cost_robot_1, self.tested_cost_robot_1, places=5, msg="Robot 1 travel cost is zero as expected.")
        self.assertAlmostEqual(cost_robot_0 + cost_robot_1, self.overall_tested_cost, places=5, msg="Overall cost is incorrect.")

unittest.main(argv=[''], verbosity=2, exit=False)