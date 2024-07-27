import unittest
from math import sqrt

# Coordinates for cities
coordinates = [
    (30, 40),  # 0
    (37, 52),  # 1
    (49, 49),  # 2
    (52, 64),  # 3
    (31, 62),  # 4
    (52, 33),  # 5
    (42, 41),  # 6
    (52, 41),  # 7
    (57, 58),  # 8
    (62, 42),  # 9
    (42, 57),  # 10
    (27, 68),  # 11
    (43, 67),  # 12
    (58, 48),  # 13
    (58, 27),  # 14
    (37, 69),  # 15
    (38, 46),  # 16
    (61, 33),  # 17
    (62, 63),  # 18
    (63, 69),  # 19
    (45, 35)   # 20
]


def calculate_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)


def validate_paths(paths, total_costs):
    unique_cities_visited = set()
    total_calculated_cost = 0

    for path, reported_cost in zip(paths, total_costs):
        total_dist = 0
        last_city = path[0]
        unique_cities_visited.update(path)

        for city in path[1:]:
            dist = calculate_distance(last_city, city)
            total_dist += dist
            last_city = city

        # Consider error margin in floating point comparison
        if not (abs(total_dist - reported_cost) < 1e-5):
            return False

        total_calculated_cost += total_dist

    # Verify all cities are visited exactly once collectively
    if len(unique_cities_visited) != 21 or unique_cities_visited != set(range(21)):
        return False

    # Check the reported total cost with calculated cost
    if not (abs(total_calculated_cost - sum(total_costs)) < 1e-5):
        return False

    return True


class TestRobotTour(unittest.TestCase):
    def test_solution(self):
        # Robots tours and their corresponding costs
        robot_0_tour = [0, 6, 5, 14, 20, 0]
        robot_0_cost = 64.4088502512122
        robot_1_tour = [1, 15, 11, 4, 12, 19, 18, 9, 17, 13, 3, 8, 2, 7, 16, 10, 1]
        robot_1_cost = 197.92162758405976
        total_cost = 262.33047783527195

        result = validate_paths([robot_0_tour, robot_1_tour], [robot_0_cost, robot_1_cost])
        
        overall_cost_correct = abs((robot_0_cost + robot_1_cost) - total_cost) < 1e-5

        self.assertTrue(result and overall_cost_correct)


if __name__ == '__main__':
    unittest.main()