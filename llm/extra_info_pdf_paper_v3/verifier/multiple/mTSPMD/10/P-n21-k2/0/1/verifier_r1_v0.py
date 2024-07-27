from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def tour_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        city1 = tour[i - 1]
        city2 = tour[i]
        cost += euclidean_distance(coordinates[city1][0], coordinates[city1][1], coordinates[city2][0], coordinates[city2][1])
    return round(cost, 2)

def validate_solution():
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }

    robot_0_tour = [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
    robot_1_tour = [1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]

    # Check Requirement 1
    if robot_0_tour[0] != robot_0_tour[-1] or robot_0_tour[0] != 0:
        return "FAIL"
    if robot_1_tour[0] != robot_1_tour[-1] or robot_1_tour[0] != 1:
        return "FAIL"

    # Check Requirement 2
    all_cities = set(range(21))
    visited_cities = set(robot_0_tour + robot_1_tour)
    if visited_cities != all_cities:
        return "FAIL"

    # Check Requirement 3
    estimated_total_cost = 55.76
    calculated_cost_robot_0 = tour_cost(robot_0_tour, coordinates)
    calculated_cost_robot_1 = tour_cost(robot_1_tour, coordinates)
    total_cost = calculated_cost_robot_0 + calculated_cost_robot_1
    if abs(total_cost - estimated_total_cost) > 0.1:
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Run validation
result = validate_solution()
print(result)