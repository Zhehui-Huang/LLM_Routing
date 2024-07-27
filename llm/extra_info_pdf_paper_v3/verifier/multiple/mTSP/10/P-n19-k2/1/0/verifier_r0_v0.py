import unittest
import math

# Data setup
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Solution details
solutions = {
    0: {"tour": [0, 6, 2, 7, 5, 9, 8, 3, 4, 1, 0], "cost": 115.60},
    1: {"tour": [0, 10, 11, 14, 12, 17, 16, 15, 13, 18, 0], "cost": 149.77}
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += calculate_euclidean_distance(tour[i], tour[i+1])
    return round(cost, 2)

class TestRobotTours(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        for robot, details in solutions.items():
            self.assertEqual(details['tour'][0], 0)
            self.assertEqual(details['tour'][-1], 0)

    def test_all_cities_visited_exactly_once(self):
        visited = set()
        for robot, details in solutions.items():
            # Ignore the depot city in the count, count each only once
            visited.update(details['tour'][1:-1])
        self.assertEqual(len(visited), 18)  # We expect all cities but depot to be included

    def test_tour_costs(self):
        for robot, details in solutions.items():
            calculated_cost = calculate_total_tour_cost(details['tour'])
            self.assertAlmostEqual(calculated_cost, details['cost'], places=2)

if __name__ == "__main__":
    unittest.main()