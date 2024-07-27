import unittest
from math import sqrt

# Coordinates of the cities (indexed from 0 to 22)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 35), (56, 37)
]

# Robot tours provided in the solution
robot_tours = [
    [0, 21, 7, 9, 0],   [0, 16, 5, 17, 0],   [0, 6, 22, 8, 0],
    [0, 1, 12, 15, 0],  [0, 20, 14, 18, 0],  [0, 10, 3, 19, 0],
    [0, 2, 13, 0],      [0, 4, 11, 0]
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Checking travel costs and tour validity
def check_tours_and_costs(robot_tours):
    expected_costs = [64.45, 69.89, 80.08, 66.21, 106.71, 89.03, 59.20, 57.39]
    total_travel_cost = 0
    cities_visited = set()
    
    for index, tour in enumerate(robot_tours):
        cost = 0
        for j in range(len(tour) - 1):
            city1, city2 = tour[j], tour[j + 1]
            cost += calculate_distance(city1, city2)
            cities_visited.add(city1)
        # Adding the last city
        cities_visited.add(tour[-1])
        total_travel_cost += cost
        
        # Check if individual cost calculation is almost equal to the reported cost
        if not (abs(cost - expected_costs[index]) < 0.1):
            return "FAIL"

    # Check if all cities are visited exactly once
    if len(cities_visited) == 23:
        return "CORRECT"
    else:
        return "FAIL"

class TestRobotTours(unittest.TestCase):
    def test_solution_correctness(self):
        self.assertEqual(check_tours_and_costs(robot_tours), "CORRECT")

if __name__ == "__main__":
    unittest.main()