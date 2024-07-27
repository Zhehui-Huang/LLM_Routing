import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
            16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }
        self.demands = {
            1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15,
            8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19,
            15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15
        }
        self.robot0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0]
        self.robot1_tour = [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
        self.robot_capacity = 160
        
    def euclidean_distance(self, a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def total_cost(self, tour):
        cost = 0
        for i in range(len(tour) - 1):
            cost += self.euclidean_distance(self.cities[tour[i]], self.cities[tour[i+1]])
        return cost

    def test_start_end_depot(self):
        self.assertEqual(self.robot0_tour[0], self.robot0_tour[-1])
        self.assertEqual(self.robot1_tour[0], self.robot1_tour[-1])

    def test_demand_fulfilled(self):
        all_cities = set(self.robot0_tour[1:-1] + self.robot1_tour[1:-1])
        self.assertSetEqual(all_cities, set(self.demands.keys()))

    def test_capacity_not_exceeded(self):
        robot0_load = sum(self.demands[city] for city in self.robot0_tour if city in self.demands)
        robot1_load = sum(self.demands[city] for city in self.robot1_tour if city in self.demands)
        self.assertLessEqual(robot0_load, self.robot_capacity)
        self.assertLessEqual(robot1_load, self.robot_capacity)

    def test_total_travel_cost(self):
        expected_total_cost = 296.40
        actual_total_cost = self.total_cost(self.robot0_tour) + self.total_cost(self.robot1_tour)
        self.assertAlmostEqual(expected_total_cost, actual_total_cost, places=2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    results = unittest.TextTestRunner().run(suite)
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")