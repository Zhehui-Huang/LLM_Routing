import unittest
from math import sqrt

class TestCVRPCorrectness(unittest.TestCase):
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }

    demands = {
        1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28,
        9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12,
        17: 26, 18: 17, 19: 6, 20: 15, 21: 5, 22: 10
    }

    robot_tours = {
        0: [0, 22, 0], 1: [0, 3, 4, 0], 2: [0, 5, 6, 9, 0],
        3: [0, 7, 10, 11, 13, 0], 4: [0, 8, 15, 0], 5: [0, 12, 14, 19, 0],
        6: [0, 16, 17, 0], 7: [0, 18, 20, 21, 0]
    }
    
    robot_capacities = 8 * [40]  # 8 robots, each with a capacity of 40

    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def test_start_end_at_depot(self):
        for tour in self.robot_tours.values():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_full_demand_meeting(self):
        delivered = {city: 0 for city in self.demands}
        for tour in self.robot_tours.values():
            for city in tour:
                if city != 0:
                    delivered[city] += self.demands[city]
        self.assertDictEqual(delivered, self.demands)

    def test_capacity_constraints(self):
        for tour in self.robot_tours.values():
            load = 0
            for city in tour:
                if city != 0:
                    load += self.demands[city]
            self.assertLessEqual(load, 40)  # Each robot's capacity

    def test_total_cost_minimization(self):
        # Checking if the provided overall cost is consistent with the reported tour distance sums
        expected_cost = sum([
            52.3450093132096, 75.67537984747364, 87.98046471435967,
            125.50392609591222, 85.10825368055515, 158.91500409222184,
            68.20018679138722, 88.0023381850297
        ])
        actual_cost = sum([
            sum(self.calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            for tour in self.robot_tours.values()
        ])
        self.assertAlmostEqual(actual_cost, expected_cost, places=5)

    def test_correct_number_of_robots(self):
        self.assertEqual(len(self.robot_tours), 8)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCVRPCorrectness)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")