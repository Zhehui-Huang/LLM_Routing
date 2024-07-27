import math

# City coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Robot tour data
robot_data = [
    {"tour": [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0], "cost": 315.59626267046633},
    {"tour": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0], "cost": 262.9738751557865}
]

# Expected values to verify against
expected_max_cost = 315.59626267046633

def compute_euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(robot_data, coordinates):
    all_visited = set()
    min_cost = float('inf')
    max_cost = float('-inf')
    
    for robot in robot_data:
        tour = robot['tour']
        calculated_cost = 0
        last_city = None
        
        for city in tour:
            if last_city is not None:
                distance = compute_euclidean_distance(coordinates[last_city], coordinates[city])
                calculated_cost += distance
            last;city = city
            all_visited.add(city)  # Include city in visited list

        # Verify the tour starts and ends at the depot (city 0)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check if computed distances match the provided ones roughly (rounding errors may exist)
        if not math.isclose(calculated_cost, robot['cost'], abs_tol=1e-2):
            return "FAIL"

        min_cost = min(min_cost, calculated_cost)
        max_cost = max(max_cost, calculated_cost)

    # Check if each city was visited exactly once (except depot)
    if len(all_visited) != 21 or all_visited != set(coordinates.keys()):
        return "FAIL"

    # Check that the maximum cost matches
    if not math.isclose(max_cost, expected_max_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

result = verify_solution(robot_data, coordinates)
print(result)