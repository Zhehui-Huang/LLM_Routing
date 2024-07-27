import math

# Cities' locations
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
    18: (45, 35)
}

# Demands of each city
demands = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14, 10: 8,
    11: 7, 12: 14, 13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15
}

# Robot tours
robot_tours = {
    0: [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    1: [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
}

# Capacities of the robots
robot_capacities = {
    0: 160,
    1: 160
}

# Travel costs by robot
robot_costs = {
    0: 129.15403265466222,
    1: 172.59405136136587
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution():
    visited_cities = set()

    actual_robot_costs = {}
    for robot in robot_tours:
        tour = robot_tours[robot]
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Not starting or ending at depot

        # Calculate total distances and demands
        total_distance = 0
        total_demand = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i + 1]
            visited_cities.add(city1)
            if city1 != 0:  # Do not count demand of depot
                total_demand += demands[city1]
            total_distance += euclidean_distance(cities[city1], cities[city2])

        actual_robot_costs[robot] = total_distance
        if total_demand > robot_capacities[robot]:
            return "FAIL"  # Exceeding capacity

    # Check if all cities except the depot are visited exactly once
    if len(visited_cities - {0}) != len(cities) - 1:
        return "FAIL"

    # Calculate total costs and compare with provided
    total_cost = sum(actual_robot_costs.values())
    estimated_total_cost = sum(robot_costs.values())
    if not math.isclose(total_cost, estimated_total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Run the unit test
print(verify_solution())