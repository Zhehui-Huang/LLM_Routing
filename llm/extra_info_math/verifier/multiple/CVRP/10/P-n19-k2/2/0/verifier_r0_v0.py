import unittest
import math

class TestCVRPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates for each city index
        self.coordinates = [
            (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
            (61, 33), (62, 63), (63, 69), (45, 35)
        ]
        # Demand for each city
        self.demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
        # Capacity of each robot
        self.capacity = 160
        # Robot tours
        self.robot_tours = [
            [0, 0],
            [0, 0]
        ]
        # Robot capacities
        self.robot_capacities = [160, 160]
        # Test provided solution
        self.solution_travel_costs = [0.0, 0.0]
    
    def test_route_starts_and_ends_at_depot(self):
        # Check if each robot's route starts and ends at the depot
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)
    
    def test_each_city_visited_exactly_once(self):
        # Combine all tours and count each city's visits
        all_cities_visited = sum(self.robot_tours, [])
        city_visit_count = {city: all_cities_visited.count(city) for city in range(1, len(self.coordinates))}
        # Check if each city is visited exactly once (exclude the depot city 0)
        for city in range(1, len(self.coordinates)):
            self.assertEqual(city_visit_count.get(city, 0), 1)

    def test_total_demand_does_not_exceed_capacity(self):
        # Check if demand on each route does not exceed the robot's capacity
        for tour, capacity in zip(self.robot_tours, self.robot_capacities):
            route_demand = sum(self.demands[city] for city in tour if city != 0)  # Exclude depot from demand calculation
            self.assertLessEqual(route_demand, capacity)

    def test_minimize_total_travel_cost(self):
        # Calculate the true minimal cost if given
        expected_minimal_cost = sum(self.solution_travel_costs)
        # Total travel cost considering Euclidean distance
        actual_cost = 0
        for tour in self.robot_tours:
            for i in range(1, len(tour)):
                prev_city = tour[i - 1]
                curr_city = tour[i]
                prev_coord = self.coordinates[prev_city]
                curr_coord = self.coordinates[curr_city]
                distance = math.sqrt((curr_coord[0] - prev_coord[0])**2 + (curr_coord[1] - prev_coord[1])**2)
                actual_cost += distance
        # Comparing actual cost from calculations and minimal cost considered by solution, should be the same
        self.assertAlmostEqual(actual_cost, expected_minimal_cost)

    def run_all_tests(self):
        # Running all tests
        self.test_route_starts_and_ends_at_depot()
        self.test_each_city_visited_exactly_once()
        self.test_total_demand_does_not_exceed_capacity()
        self.test_minimize_total_travel_cost()
        
        # If all tests pass:
        print("CORRECT")
        # If any test fails:
        # print("FAIL")

# Create test suite and runner
suite = unittest.TestSuite()
suite.addTest(TestCVRPSolution('run_all_tests'))
runner = unittest.TextTestRunner()
runner.run(suite)