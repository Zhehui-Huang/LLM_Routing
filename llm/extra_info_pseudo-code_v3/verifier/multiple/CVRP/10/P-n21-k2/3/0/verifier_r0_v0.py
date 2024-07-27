import unittest
import math

class TestCVRPSolution(unittest.TestCase):
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }

    demands = {
        0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28,
        9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26,
        18: 17, 19: 6, 20: 15
    }

    capacity = 160
    robot_tours = [
        [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 0],
        [0, 6, 20, 5, 7, 2, 9, 17, 14, 0]
    ]

    costs = [
        152.94843881430188, 103.97302235762616
    ]

    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def test_start_and_end_at_depot(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_all_cities_visited(self):
        visited_cities = set()
        for tour in self.robot_tours:
            visited_cities.update(tour)
        expected_cities = set(self.demands.keys())
        self.assertEqual(visited_cities, expected_cities)

    def test_demand_meeting(self):
        for tour in self.robot_tours:
            current_capacity = self.capacity
            for city in tour[1:-1]:  # Ignore depot in demand check
                demand = self.demands[city]
                self.assertLessEqual(demand, current_capacity)
                current_capacity -= demand

    def test_capacity_constraints(self):
        for tour in self.robot_tours:
            total_delivered = sum(self.demands[city] for city in tour[1:-1])
            self.assertLessEqual(total_delivered, self.capacity)

    def test_travel_costs(self):
        for tour, expected_cost in zip(self.robot_tours, self.costs):
            total_cost = sum(self.calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            self.assertAlmostEqual(total_cost, expected_cost, places=5)

    def test_total_cost(self):
        total_cost = sum(self.costs)
        self.assertAlmostEqual(total_cost, 256.92146117192806, places=5)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCVRPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")