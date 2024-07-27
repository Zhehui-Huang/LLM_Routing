import unittest
import math

class TestVRPSolution(unittest.TestCase):
    # Coordinates of the cities (0-indexed)
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
        (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]

    # Demand for each city (0-indexed)
    demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

    # Robot tours
    robot0_tour = [0, 1, 10, 4, 11, 12, 8, 3, 16, 17, 14, 0]
    robot1_tour = [0, 2, 7, 5, 9, 13, 15, 18, 0]
    
    # Robot carrying capacities
    robot_capacities = [160, 160]

    def calculate_distance(self, city1, city2):
        x1, y1 = self.coordinates[city1]
        x2, y2 = self.coordinates[city2]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def test_tour_start_and_end_at_depot(self):
        self.assertEqual(self.robot0_tour[0], 0)
        self.assertEqual(self.robot0_tour[-1], 0)
        self.assertEqual(self.robot1_tour[0], 0)
        self.assertEqual(self.robot1_tour[-1], 0)

    def test_demand_fulfillment(self):
        # Verifies all demands are met
        robot0_covered = self.robot0_tour[1:-1]
        robot1_covered = self.robot1_tour[1:-1]
        demands_met = [0] * 19
        for city in robot0_covered + robot1_covered:
            demands_met[city] += self.demands[city]
        for city, demand in enumerate(self.demands):
            if city == 0:
                continue
            self.assertEqual(demands_met[city], self.demands[city])

    def test_capacity_constraints(self):
        # Verifies capacity constraints are not exceeded
        robot0_load = sum(self.demands[city] for city in self.robot0_tour[1:-1])
        robot1_load = sum(self.demands[city] for city in self.robot1_tour[1:-1])
        self.assertTrue(robot0_load <= self.robot_capacities[0])
        self.assertTrue(robot1_load <= self.robot_capacities[1])

    def test_total_travel_cost_calculation(self):
        # Calculates the total travel cost and compares to expected cost
        def total_cost(tour):
            return sum(self.calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        actual_robot0_cost = sum(self.calculate_distance(self.robot0_tour[i], self.robot0_tour[i+1]) for i in range(len(self.robot0_tour)-1))
        actual_robot1_cost = sum(self.calculate_distance(self.robot1_tour[i], self.robot1_tour[i+1]) for i in range(len(self.robot1_tour)-1))
        total_cost_calculated = actual_robot0_cost + actual_robot1_cost
        
        # Expected costs provided in the problem
        expected_robot0_cost = 152.71
        expected_robot1_cost = 98.46
        expected_total_cost = 251.17
        
        # Testing with a margin for floating point calculations
        self.assertAlmostEqual(actual_robot0_cost, expected_robot0/data_controver_sy_cost, places=2)
        self.assertAlmostEqual(actual_robot1_cost, expected_robot1_cost, places=2)
        self.assertAlmostEqual(total_cost_calculated, expected_total_cost, places=2)

if __name__ == '__main__':
    unittest.main()