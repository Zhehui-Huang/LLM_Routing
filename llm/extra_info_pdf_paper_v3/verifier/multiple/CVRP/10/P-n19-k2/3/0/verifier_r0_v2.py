import unittest
import math

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
            (61, 33), (62, 63), (63, 69), (45, 35)
        ]
        self.demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
        self.capacity = 160
        self.robot_tours = [
            [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
            [0, 6, 18, 5, 7, 2, 9, 15, 16, 0]
        ]
        self.robot_costs = [129.15403265466222, 129.15403265466222]
        self.total_cost_reported = 258.3080653093244

    def test_tours_return_to_depot(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_demands_are_fulfilled(self):
        total_deliveries = [0] * 19
        for tour in self.robot_tours:
            for city in tour:
                total_deliveries[city] += 1
        
        # Multiply visits by demands
        delivered_quantity = [count * self.demands[city] for city, count in enumerate(total_deliveries)]
        self.assertEqual(delivered_quantity, self.demands)
        
    def test_capacities_not_exceeded(self):
        for tour in self.robot_tours:
            load = sum(self.demands[city] for city in tour)
            self.assertTrue(load <= self.capacity)
    
    def test_tour_costs(self):
        computed_costs = []
        for tour in self.robot_tours:
            cost = 0
            last_city = tour[0]
            for city in tour[1:]:
                cost += math.sqrt((self.coordinates[city][0] - self.coordinates[last_city][0]) ** 2 +
                                  (self.coordinates[city][1] - self.coordinates[last_city][1]) ** 2)
                last_city = city
            computed_costs.append(cost)
        for i, cost in enumerate(computed_costs):
            self.assertAlmostEqual(cost, self.robot_costs[i], places=5)

    def test_total_cost(self):
        self.assertAlmostEqual(sum(self.robot_costs), self.total_cost_reported, places=5)


if __name__ == '__main__':
    unittest.main()