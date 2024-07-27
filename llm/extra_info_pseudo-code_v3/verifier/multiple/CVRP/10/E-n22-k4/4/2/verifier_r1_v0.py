import math
import unittest

class TestCVRPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of each city including depot (index 0)
        self.coordinates = [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
            (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
            (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
            (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
            (155, 185), (139, 182)
        ]
        
        # Demand of each city excluding depot
        self.demand = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
                       600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
                       1800, 700]
        
        # Tours of each robot
        self.robots_tours = [
            [0, 14, 16, 17, 20, 21, 8, 0],
            [0, 12, 15, 18, 19, 6, 0],
            [0, 13, 11, 10, 9, 7, 2, 3, 0],
            [0, 5, 1, 4, 0]
        ]
        
        # Travel costs reported for each robot's tour
        self.reported_costs = [135.6322487935778, 163.9469786443022, 165.65732610535312, 124.18456123320681]
        self.robot_capacity = 6000
        self.total_reported_cost = 589.4211147764399

    def test_tour_validity(self):
        # Check all tours start and end at the depot and that all cities are visited exactly once.
        all_visited = set()
        for tour in self.robots_tours:
            # Check starting and ending at the depot
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)
            all_visited.update(tour[1:-1])
        
        self.assertEqual(all_visited, set(range(1, 22)))  # Cities 1 to 21 should be visited exactly once

    def test_demand_fulfillment(self):
        # Check that demands are met exactly
        city_demands = [0] * 22  # Initialize all city demands to zero
        for tour in self.robots_tours:
            for city in tour[1:-1]:  # Exclude depot
                city_demands[city] += self.demand[city]
        
        self.assertEqual(city_demands, self.demand)
    
    def test_capacity_constraints(self):
        # Check that no tour exceeds robot capacity
        for tour in self.robots_tours:
            total_demand = sum(self.demand[city] for city in tour[1:-1])
            self.assertLessEqual(total_demand, self.robot_capacity)
    
    def test_travel_cost(self):
        # Verify the total travel cost calculation
        total_cost = 0
        for tour, reported_cost in zip(self.robots_tours, self.reported_costs):
            cost = 0
            for i in range(len(tour) - 1):
                start = tour[i]
                end = tour[i+1]
                dist = math.sqrt((self.coordinates[start][0] - self.coordinates[end][0]) ** 2 + (self.coordinates[start][1] - self.coordinates[end][1]) ** 2)
                cost += dist
            total_cost += cost
            self.assertAlmostEqual(cost, reported_cost, places=5)  # Testing approx equal with small rounding allowance
            
        self.assertAlmostEqual(total_cost, self.total_reported_cost, places=5)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCVRPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")