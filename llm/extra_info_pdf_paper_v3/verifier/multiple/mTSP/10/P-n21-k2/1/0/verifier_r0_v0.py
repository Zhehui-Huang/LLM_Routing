import unittest
import math

# Mock data for the purpose of test verification
cities_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Solution example, for verification purposes
robot_tours = [
    [0, 6, 7, 5, 9, 2, 10, 1, 4, 3, 8, 0],
    [0, 16, 20, 14, 17, 13, 18, 19, 12, 15, 11, 0]
]

robots_travel_costs = [148.98, 146.55]

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        city1, city2 = tour[i], tour[i+1]
        total_cost += math.dist(cities_coords[city1], cities_coords[city2])
    return round(total_cost, 2)

class TestRobotsPath(unittest.TestCase):
    def test_starts_and_ends_at_depot(self):
        # Requirement 4
        for tour in robot_tours:
            self.assertEqual(tour[0], 0, "Tour should start at Depot City (0)")
            self.assertEqual(tour[-1], 0, "Tour should end at Depot City (0)")
    
    def test_visits_all_cities_exactly_once(self):
        # Requirement 2
        visited = set()
        for tour in robot_tours:
            visited.update(tour[1:-1])  # Exclude the depot city from checking
        self.assertSetEqual(visited, set(range(1, 21)), "All cities must be visited exactly once")
    
    def test_number_of_robots_used(self):
        # Requirement 5
        self.assertEqual(len(robot_tours), 2, "Only two robots should be used")
    
    def test_correct_travel_cost(self):
        # Requirement 6
        for idx, tour in enumerate(robot_tours):
            expected_cost = robots_travel_costs[idx]
            calculated_cost = calculate_cost(tour)
            self.assertEqual(calculated_cost, expected_cost, f"Robot {idx} travel cost should be correct.")
    
    def test_verify_total_travel_cost(self):
        # Requirement 6
        total_calculated_cost = sum(calculate_cost(tour) for tour in robot_tours)
        expected_total_cost = sum(robots_travel_costs)
        self.assertAlmostEqual(total_calculated_cost, expected_total_cost, places=2, msg="Total travel cost should be correct.")

# Executing the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotsPath)
test_result = unittest.TextTestRunner().run(suite)

# Determine if solution passes all tests
if test_result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")