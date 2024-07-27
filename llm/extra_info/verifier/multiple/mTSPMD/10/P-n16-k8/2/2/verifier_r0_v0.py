import math

# Given robot tours
robot_tours = {
    0: [0, 10, 12, 15, 11, 8, 13, 9, 14, 0],
    1: [1, 1],
    2: [2, 2],
    3: [3, 3],
    4: [4, 4],
    5: [5, 5],
    6: [6, 6],
    7: [7, 7]
}

# Travel costs
robot_travel_costs = [142.5115861601223, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Overall total cost
overall_total_cost = 142.5115861601223

# Each robot's depot
depot = {i: i for i in range(8)}

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tours, travel_costs, overall_cost):
    # Requirement 1: Each robot starts and ends at its assigned depot.
    for r, tour in tours.items():
        if not (tour[0] == depot[r] and tour[-1] == depot[r]):
            return "FAIL"

    # Requirement 2: Each city must be visited exactly once across all robots' tours.
    visited = set()
    for tour in tours.values():
        visited.update(tour)
    if len(visited) != 16:  # Since there are 16 cities including depots.
        return "FAIL"

    # Requirement 3: Calculated costs are correct
    calculated_costs = []
    for robot_id, tour in tours.items():
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_costs.append(total_cost)
    
    if not all(math.isclose(calculated_costs[r], travel_costs[r], abs_tol=0.01) for r in range(8)):
        return "FAIL"
    
    if not math.isclose(sum(calculated_costs), overall_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Run and check the verification
result = verify_solution(robot_tours, robot_travel_costs, overall_total_cost)
print(result)