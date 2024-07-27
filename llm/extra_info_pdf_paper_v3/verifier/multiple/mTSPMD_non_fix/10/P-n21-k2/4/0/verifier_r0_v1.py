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

def is_solution_correct(robot_paths, robot_costs, total_cost):
    visited = set(sum(robot_paths, []))
    if len(visited) != 21 or set(visited) != set(range(21)):
        return False

    computed_total_cost = 0
    for path, cost in zip(robot_paths, robot_costs):
        path_cost = sum(calculate_distance(path[i], path[i+1]) for i in range(len(path) - 1))
        if not abs(path_cost - cost) < 1e-4:  # accounting for floating point precision
            return False
        computed_total_cost += cost

    return abs(computed_total_cost - total_cost) < 1e-4

class TestRobotTours(unittest.TestCase):
    def test_robot_tours(self):
        # Paths and costs from the solution
        robot_0_path = [0, 6, 5, 14, 20, 0]
        robot_0_cost = 64.4088502512122
        robot_1_path = [1, 15, 11, 4, 12, 19, 18, 9, 17, 13, 3, 8, 2, 7, 16, 10, 1]
        robot_1_cost = 197.92162758405976
        total_cost = 262.33047783527195

        # Check the solution
        correct = is_solution_correct([robot_0_path, robot_1_path], [robot_0_cost, robot_1_cost], total_cost)
        if correct:
            print("CORRECT")
        else:
            print("FAIL")
        self.assertTrue(correct)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)