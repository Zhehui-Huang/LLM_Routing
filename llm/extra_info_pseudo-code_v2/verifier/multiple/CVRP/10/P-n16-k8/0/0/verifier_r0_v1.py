import unittest
import math

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
            (43, 67), (58, 48), (58, 27), (37, 69)
        ]
        self.demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
        self.robot_capacity = 35
        self.tours = [
            [0, 9, 13, 0], [0, 12, 15, 0], [0, 3, 12, 0], [0, 8, 13, 0], 
            [0, 11, 15, 0], [0, 8, 9, 0], [0, 9, 14, 0], [0, 3, 15, 0]
        ]
        self.travel_costs = [
            68.39398119181284, 66.12407122823275, 72.01112230024795, 71.62027665741887,
            68.04299908213093, 81.27545517717891, 78.45731186088909, 78.20189727339391
        ]

    def test_robot_tours_start_end_at_depot(self):
        for tour in self.tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_demand_fulfillment(self):
        delivered = [0] * 16
        for tour in self.tours:
            for city in tour:
                if city != 0:  # Ignore the depot city for delivery tally
                    delivered[city] += self.demands[city]
        # We check if the demand of each city exceeded the original demand
        demand_met = all(delivered[city] >= self.demands[city] for city in range(1, 16))
        self.assertTrue(demand_met)

    def test_capacity_constraints(self):
        for tour in self.tours:
            total_demand = sum(self.demands[city] for city in tour if city != 0)
            self.assertTrue(total_demand <= self.robot_capacity, 
                            msg=f"Total demand {total_demand} exceeds capacity {self.robot_capacity} in tour {tour}")

    def test_travel_cost_calculation(self):
        for idx, tour in enumerate(self.tours):
            total_cost = 0
            for i in range(len(tour) - 1):
                x1, y1 = self.coordinates[tour[i]]
                x2, y2 = self.coordinates[tour[i + 1]]
                total_cost += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            self.assertAlmostEqual(total_cost, self.travel_costs[idx], places=5)

    def test_robot_count(self):
        self.assertTrue(len(self.tours) <= 8, "Number of robots exceed available robots.")

if __name__ == '__main__':
    unittest.main()