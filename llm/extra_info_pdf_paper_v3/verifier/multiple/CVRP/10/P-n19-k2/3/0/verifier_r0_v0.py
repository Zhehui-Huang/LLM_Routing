import unittest
import math

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of each city (including depot)
        self.coordinates = [
            (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
            (61, 33), (62, 63), (63, 69), (45, 35)
        ]
        
        # Demand of each city
        self.demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
        
        # Capacity of each robot
        self.robot_capacity = 160
        
        # Robots tours
        self.robot_tours = [
            [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
            [0, 6, 18, 5, 7, 2, 9, 15, 16, 0]
        ]
        
        # Total cost reported 
        self.robot_costs = [129.15403265466222, 129.15403265466222]
        self.total_cost_reported = 258.30806530932443
        
    def test_all_cities_delivered_excluding_depot(self):
        delivered_cities = set(city for tour in self.robot_tours for city in tour if city != 0)
        self.assertEqual(delivered_cities, set(range(1, 19)))
    
    def test_return_to_depot(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)
    
    def test_demand_fulfilled(self):
        city_delivery = [0] * 19
        for tour in self.robot_tours:
            for city in tour:
                city_delivery[city] += 1
        self.assertTrue(all(city_delivery[city] >= 1 for city in range(1, 19)))
    
    def test_capacity_not_exceeded(self):
        for tour in self.robot_tours:
            load = sum(self.demands[city] for city in tour)
            self.assertLessEqual(load, self.robot_capacity)
    
    def test_tour_costs(self):
        def calculate_cost(tour):
            cost = 0
            for i in range(len(tour) - 1):
                x1, y1 = self.coordinates[tour[i]]
                x2, y2 = self.coordinates[tour[i + 1]]
                cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            return cost
        
        for i, tour in enumerate(self.robot_tours):
            self.assertAlmostEqual(calculate_cost(tour), self.robot_costs[i], places=5)

    def test_reported_total_cost(self):
        total_cost = sum(self.robot_costs)
        self.assertAlmostEqual(self.total_cost_reported, total_cost, places=5)

    def test_solution(self):
        # This is a summary test running all tests above
        self.test_all_cities_delivered_excluding_depot()
        self.test_return_to_depot()
        self.test_demand_fulfilled()
        self.test_capacity_not_exceeded()
        self.test_tour_costs()
        self.test_reported_total_cost()

        # If all pass, it's correct, otherwise detects as fail
        return "CORRECT"

# Execute the tests
solution_status = TestVRPSolution().test_solution()
print(solution_status)