import numpy as np

# Coordinates of each city
coordinates = {
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
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def calculate_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def verify_solution(robot_tours, expected_costs):
    # Check if all cities are visited
    all_visited = set()
    for tour in robot_tours:
        all_visited.update(tour[:-1])
    if len(all_visited) != 21:
        return "FAIL"

    # Check start and end points of the tours
    if not (robot_tours[0][0] == robot_tours[0][-1] == 0 and robot_tours[1][0] == robot_tours[1][-1] == 1):
        return "FAIL"

    # Check if calculated distances match expected costs
    calculated_costs = []
    for tour in robot_tours:
        tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        calculated_costs.append(round(tour_provider_cost, 2))

    if any(np.abs(calculated_costs[i] - expected_costs[i]) > 0.01 for i in range(2)):
        return "FAIL"

    # Check the total cost
    total_cost = sum(calculated_costs)
    if np.abs(total_cost - sum(expected_costs)) > 0.01:
        return "FAIL"

    return "CORRECT"

# Solution provided
robot_tours = [
    [0] + [int(city) for city in [6, 20, 5, 14, 17, 9, 13, 7, 2, 8, 18, 19, 3, 12, 15, 11, 4, 10, 1, 16]] + [0],
    [1] + [int(city) for city in [16, 0, 6, 20, 5, 14, 17, 9, 13, 7, 2, 8, 18, 19, 3, 12, 15, 11, 4, 10]] + [1]
]
expected_costs = [180.84, 180.84]

# Check if the given solution meets the requirements and validation tests
result = verify_solution(robot_tours, expected_costs)
print(result)