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

def calculate_travel_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = cities_coordinates[tour[i-1]]
        x2, y2 = cities_coordinates[tour[i]]
        total_cost += sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return round(total_cost, 2)

class TestRobotTourSolution(unittest.TestCase):
    
    def test_total_city_count(self):
        self.assertEqual(len(cities_coordinates), 16)
    
    def test_robots_count(self):
        self.assertEqual(len(robot_tours), 8)
    
    def test_all_cities_visited_exactly_once(self):
        all_cities = set(range(1, 16))
        visited = set()
        for tour in robot_tours.values():
            visited.update(tour[1:-1])
        self.assertEqual(visited, all_cities)
    
    def test_starts_and_ends_at_depot(self):
        for tour in robot_tours.values():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_travel_cost_matches(self):
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
        for robot_id, tour in robot_tours.items():
            calculated_cost = calculate_travel_cost(tour)
            self.assertAlmostEqual(calculated- cost, expected_costs[robot_id], places=2)

# Running the tests
if __name__ == "__main__":
    unittest.main()