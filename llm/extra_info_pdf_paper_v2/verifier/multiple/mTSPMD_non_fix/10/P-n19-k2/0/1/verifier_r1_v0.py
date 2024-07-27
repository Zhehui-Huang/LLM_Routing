import unittest
from math import sqrt

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
            16: (62, 63), 17: (63, 69), 18: (45, 35)
        }
        
        self.robot_0_tour = [0, 10, 4, 11, 14, 12, 3, 2, 7, 18, 5, 13, 15, 9, 16, 17, 8, 6, 0]
        self.robot_1_tour = [1, 10, 12, 3, 17, 16, 8, 7, 2, 6, 18, 5, 13, 15, 9, 14, 11, 4, 1]
        self.robot_0_cost = 205.86
        self.robot_1_cost = 184.41

    def test_unique_visits(self):
        visited = set(self.robot_0_tour + self.robot_1_tour)
        self.assertEqual(len(visited), 19, "Fail: Not all cities are visited exactly once")

    def test_start_end_depot(self):
        self.assertEqual(self.robot_0_tour[0], 0, "Robot 0 did not start at depot 0")
        self.assertEqual(self.robot_0_tour[-1], 0, "Robot 0 did not end at depot 0")
        self.assertEqual(self.robot_1_tour[0], 1, "Robot 1 did not start at depot 1")
        self.assertEqual(self.robot_1_tour[-1], 1, "Robot 1 did not end at depot 1")

    def test_total_cost_calculation(self):
        def compute_cost(tour):
            total_cost = 0
            for i in range(len(tour)-1):
                total_cost += euclidean_distance(self.cities[tour[i]], self.cities[tour[i+1]])
            return round(total_cost, 2)

        calc_robot_0_cost = compute_cost(self.robot_0_tour)
        calc_robot_1_cost = compute_down(self.robot_1_tour)
        self.assertEqual(calc_robot_0_cost, self.robot_0_cost, "Incorrect cost calculation for Robot 0")
        self.assertEqual(calc_robot_1_cost, self.robot_1_cost, "Incorrect cost calculation for Robot 1")
        
        total_calc_cost = calc_robot_0_cost + calc_robot_1_cost
        reported_total_cost = 390.26
        self.assertAlmostEqual(total_calc_cost, reported_total_cost, places=2, msg="Total travel cost is incorrect")

# Run the test
if __Name__ == "__main__":
    unittest.main()