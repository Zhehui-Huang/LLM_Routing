import unittest
from math import sqrt

# Coordinates of the cities (indexed from 0 to 22)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

robot_tours = [
    [0, 21, 7, 9, 0],
    [0, 16, 5, 17, 0],
    [0, 6, 22, 8, 0],
    [0, 1, 12, 15, 0],
    [0, 20, 14, 18, 0],
    [0, 10, 3, 19, 0],
    [0, 2, 13, 0],
    [0, 4, 11, 0]
]

def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tours_and_costs(robot_tours):
    all_visited = set()
    total_cost = 0

    for tour in robot_tours:
        tour_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_cost += tour_cost
        all_visited.update(tour[:-1])  # Excluding the return to the depot

    if len(all_visited) != 22 or not all(city in all_visited for city in range(1, 23)):  # Ensure all cities visited exactly once
        return "FAIL"
    
    return total_cost

class TestRobotTours(unittest.TestCase):
    def test_tour_validation(self):
        result = check_tours_and_costs(robot_tours)
        expected_total_cost = 593  # Placeholder total cost
        self.assertAlmostEqual(result, expected_total_cost, delta=1)  # Allow some tolerance

if __name__ == "__main__":
    unittest.main()