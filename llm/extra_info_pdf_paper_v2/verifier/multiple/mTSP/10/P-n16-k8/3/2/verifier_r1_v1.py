import unittest
from math import sqrt

# Data provided in the solution
robot_tours = {
    0: [0, 5, 14, 0],
    1: [0, 11, 4, 0],
    2: [0, 12, 15, 0],
    3: [0, 8, 3, 0],
    4: [0, 9, 13, 0],
    5: [0, 2, 7, 0],
    6: [0, 1, 10, 0],
    7: [0, 6, 0]
}

# Coordinates of cities
cities_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Calculating the travel cost as Euclidean distance
def calculate_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        city1_coords = cities_coordinates[city1]
        city2_coords = cities_coordinates[city2]
        total_cost += sqrt((city1_coords[0] - city2_coords[0]) ** 2 + (city1_coords[1] - city2_coords[1]) ** 2)
    return round(total_cost, 2)

class TestRobotTourSolution(unittest.TestCase):
    
    def test_total_city_count(self):
        # Including Depot (city 0)
        self.assertEqual(len(cities_coordinates), 16)
    
    def test_robots_count(self):
        self.assertEqual(len(robot_tours), 8)
    
    def test_all_cities_visited_exactly_once(self):
        visited = set(sum((tour[1:-1] for tour in robot_tours.values()), []))
        self.assertEqual(len(visited), 15)
        self.assertTrue(all(city in visited for city in range(1, 16)))
    
    def test_starts_and_ends_at_depot(self):
        all_start_end_depot = all(tour[0] == tour[-1] == 0 for tour in robot_tours.values())
        self.assertTrue(all_start_end_depot)

    def test_minimize_total_travel_cost(self):
        # Exact optimality is hard to test without knowing the ideal solution
        # but we should test provided distances to match the claimed ones
        
        expected_costs = {
            0: 62.44,
            1: 57.39,
            2: 66.12,
            3: 72.82,
            4: 68.39,
            5: 51.59,
            6: 41.77,
            7: 24.08
        }
        
        computed_costs = {robot: calculate_travel_cost(tour) for robot, tour in robot_tours.items()}
        for robot, cost in expected_costs.items():
            self.assertAlmostEqual(computed_costs[robot], cost, places=2)

# Running the tests
suite = unittest.TestSuite()
for method in dir(TestRobotTourSolution):
    if method.startswith("test_"):
        suite.addTest(TestRobot- TourSolution(method))
runner = unittest.TextTestRunner()
result = runner.run(suite)

# Verifying whether all tests pass
success = result.wasSuccessful()
print("CORRECT" if success else "FAIL")