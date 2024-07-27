import math

# City coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
               (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robots info
robots = {0: [0, 16, 0, 8, 0, 3, 0, 17, 0, 13, 0, 9, 0, 12, 0, 14, 0, 11, 0, 5, 0, 7, 0], 
          1: [0, 3, 0, 8, 0, 12, 0, 9, 0, 16, 0, 17, 0, 14, 0, 13, 0, 5, 0, 4, 0]}
robot_capacity = 160

# Calculate the Euclidean distance between two points
def distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Validate the solution
def validate_solution(robots, demands, robot_capacity):
    # Check demand fulfillment
    city_demand_satisfied = [0] * len(demands)
    for robot, tour in robots.items():
        capacity_used = 0
        for i in range(len(tour) - 1):
            if tour[i] != 0:
                city_demand_satisfied[tour[i]] += demands[tour[i]]
            if i > 0 and tour[i] != 0 and tour[i-1] != 0:
                capacity_used += demands[tour[i]]
        if capacity_used > robot_capacity:
            return "FAIL: Capacity exceeded for robot " + str(robot)

    if not all(c == 0 or c >= demands[i] for i, c in enumerate(city[group])):
        return "FAIL: Not all city demands are met"

    # Check start and end at the depot
    for robot, tour in robots.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at the depot"

    # Calculate travel cost and verify it
    expected_costs = [688.6998119895741, 632.3793006282593]
    for robot, tour in robots.items():
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += distance(tour[i], tour[i+1])
        if not math.isclose(tour_cost, expected_costs[robot], rel_tol=1e-9):
            return f"FAIL: Incorrect travel cost calculation for robot {robot}"

    # All checks passed
    return "CORRECT"

# Run validation
result = validate_solution(robots, demands, robot_capacity)
print(result)