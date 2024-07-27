import unittest
import math

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40, 0),
            1: (37, 52, 7),
            2: (49, 49, 30),
            3: (52, 64, 16),
            4: (31, 62, 23),
            5: (52, 33, 11),
            6: (42, 41, 19),
            7: (52, 41, 15),
            8: (57, 58, 28),
            9: (62, 42, 8),
            10: (42, 57, 8),
            11: (27, 68, 7),
            12: (43, 67, 14),
            13: (58, 48, 6),
            14: (58, 27, 19),
            15: (37, 69, 11),
            16: (38, 46, 12),
            17: (61, 33, 26),
            18: (62, 63, 17),
            19: (63, 69, 6),
            20: (45, 35, 15)
        }

        self.robot_tours = [
            [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 0],
            [0, 6, 20, 5, 7, 2, 9, 17, 14, 0]
        ]

        self.robot_costs_computed = [152.94843881430188, 103.97302235762616]
        self.total_cost_computed = sum(self.robot_costs_computed)

    def test_city_demand_coverage(self):
        demand_met = [0] * 21  
        for tour in self.robot_tours:
            for city in tour:
                if city != 0:  
                    demand_met[city] += self.cities[city][2]
        
        for city in range(1, 21):  
            self.assertEqual(demand_met[city], self.cities[city][2])

    def test_return_to_depot(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_robot_capacity(self):
        robot_capacity = 160
        for tour in self.robot_tours:
            total_demand = sum(self.cities[city][2] for city in tour if city !=0)
            self.assertLessEqual(total_demand, robot_capacity)

    def test_travel_cost_calculation(self):
        def calc_distance(city1, city2):
            x1, y1, _ = self.cities[city1]
            x2, y2, _ = self.cities[city2]
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        for idx, tour in enumerate(self.robot_tours):
            cost = 0
            for i in range(len(tour) - 1):
                cost += calc_distance(tour[i], tour[i + 1])
            self.assertAlmostEqual(cost, self.robot_costs_computed[idx], delta=1e-4)

    def test_total_cost(self):
        self.assertAlmostEqual(self.total_cost_computed, 256.92146117192806, delta=1e-4)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVRPSolution))
    result = unittest.TextTestRunner().run(suite)
    return result

if __name__ == "__main__":
    test_results = run_tests()
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")