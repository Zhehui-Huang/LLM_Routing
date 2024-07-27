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
        all_visited = set(self.robot0_tour[1:-1] + self.robot1_tour[1:-1])
        self.assertSetEqual(all_visited, set(range(1, 19)))  # Ensure all cities except the depot are visited

    def test_capacity_constraints(self):
        robot0_load = sum(self.demands[city] for city in self.robot0_tour[1:-1])
        robot1_load = sum(self.demands[city] for city in self.robot1_tour[1:-1])
        self.assertLessEqual(robot0_load, self.robot_capacities[0])
        self.assertLessEqual(robot1_load, self.robot_capacities[1])

    def test_total_travel_cost_calculation(self):
        def total_cost(tour):
            return sum(self.calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        expected_total_cost = 251.17
        calculated_cost = total_cost(self.robot0_tour) + total_cost(self.robot1_tour)
        
        self.assertAlmostEqual(calculated_cost, expected_total_cost, places=2)

if __name__ == '__main__':
    unittest.main()