import math

def calculate_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return cost

def verify_solution(robot_0_tour, robot_0_cost, robot_1_tour, robot_1_cost, overall_cost, coordinates):
    cities = set(range(19))  # Total cities including depots
    robot_0_visited = set(robot_0_tour)
    robot_1_visited = set(robot_1_tour)

    # [Requirement 2]
    if not (robot_0_tour[0] == robot_0_tour[-1] == 0 and robot_1_tour[0] == robot_1_tour[-1] == 1):
        return "FAIL"

    # [Requirement 1]
    if not (cities == robot_0_visited.union(robot_1_visited) and len(robot_0_visited) + len(robot_1_visited) == 39):
        return "FAIL"

    # Calculate actual costs
    calc_robot_0_cost = calculate_cost(robot_0_tour, coordinates)
    calc_robot_1_cost = calculate_cost(robot_1_tour, coordinates)
    calc_overall_cost = calc_robot_0_cost + calc_robot_1_cost

    # [Requirement 6]
    # Check costs within a small margin due to floating point computations
    if not (abs(robot_0_cost - calc_robot_0_cost) < 1e-1 and abs(robot_1_cost - calc_robot_1_cost) < 1e-1):
        return "FAIL"

    # [Requirement 3]
    if abs(overall_cost - calc_overall_cost) > 1e-1:
        return "FAIL"

    return "CORRECT"

# City coordinates (index corresponds to city number)
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
               (61, 33), (62, 63), (63, 69), (45, 35)]

# Provided test from the solution
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 16, 17, 3, 12, 14, 4, 11, 10, 0]
robot_0_cost = 194.34221730486408
robot_1_tour = [1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 9, 15, 13, 5, 18, 6, 2, 7, 1]
robot_1_cost = 180.90063642330932
overall_cost = 375.2428537281734

result = verify_solution(robot_0_tour, robot_0_cost, robot_1_tour, robot_1_cost, overall_cost, coordinates)
print(result)