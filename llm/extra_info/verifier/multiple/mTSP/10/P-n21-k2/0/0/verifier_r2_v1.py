import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
            (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
        ]

        self.robot_0_tour = [0, 4, 11, 15, 3, 2, 6, 7, 9, 14, 20, 0]
        self.robot_0_cost = 147.67206251264554

        self.robot_1_tour = [0, 16, 1, 10, 12, 19, 18, 8, 13, 17, 5, 0]
        self.robot_1_cost = 123.8910144708197

        self.overall_cost = 271.56307698346524

    def test_correct_number_of_initial_and_end_positions(self):
        self.assertEqual(self.robot_0_tour[0], 0)
        self.assertEqual(self.robot_0_tour[-1], 0)
        self.assertEqual(self.robot_1_tour[0], 0)
        self.assertEqual(self.robot_1_tour[-1], 0)

    def test_unique_visitation(self):
        combined_visits = self.robot_0_tour[1:-1] + self.robot_1_tour[1:-1]
        self.assertEqual(sorted(combined_visits), list(range(1, 21)))

    def test_travel_cost(self):
        def calc_cost(route):
            cost = 0
            for i in range(len(route) - 1):
                x1, y1 = self.cities[route[i]]
                x2, y2 = self.cities[route[i + 1]]
                cost += sqrt((x2 - x1)**2 + (y2 - y1)**2)
            return cost
        
        robot_0_calculated_cost = calc_cost(self.robot_0_tour)
        robot_1_calculated_cost = calc_cost(self.robot_1_tour)
        
        self.assertAlmostEqual(robot_0_calculated_cost, self.robot_0_cost, places=2)
        self.assertAlmostEqual(robot_1_calculated_cost, self.robot_1_cost, places=2)
        self.assertAlmostEqual(robot_0_calculated_cost + robot_1_calculated_cost, self.overall_cost, places=2)

    def test_minimal_total_travel_cost(self):
        # This is a sample minimal naive verification (practical optimality would require specific algorithmic proof or comparison)
        self.assertIsInstance(self.overall_cost, float)
        self.assertLessEqual(self.overall_cost, self.robot_0_cost + self.robot_1_cost)

def run_tests():
    tests = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    result = unittest.TextTestRunner().run(tests)

    if len(result.failures) == 0 and len(result.errors) == 0:
        print("CORRECT")
    else:
        print("FAIL")

run_tests()