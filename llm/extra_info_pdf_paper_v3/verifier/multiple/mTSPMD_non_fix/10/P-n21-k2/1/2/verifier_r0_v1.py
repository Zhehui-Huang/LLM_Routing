import math

# Data setup
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Provided solutions
solution_paths = {
    0: [0, 4, 11, 3, 19, 18, 8, 13, 7, 14, 17, 9, 2, 10, 12, 15, 1, 16, 6, 5, 20, 0],
    1: [1, 16, 0, 6, 2, 13, 18, 8, 19, 3, 12, 15, 11, 4, 10, 7, 9, 17, 14, 5, 20, 1]
}

# Calculate Euclidean distance
def calc_euclidean(x, y):
    return math.sqrt((cities[x][0] - cities[y][0])**2 + (cities[x][1] - cities[y][1])**2)

# Check Requirements
def validate_solution(paths, req_start):
    visited = set()
    total_cost = 0.0

    for robot_id, path in paths.items():
        # Check start and end at designated depot
        if path[0] != req_start[robot_id] or path[-1] != req_start[robot_id]:
            return False, 0.0

        # Compute cost and validate each step
        tour_cost = 0.0
        last_city = path[0]
        for city in path[1:]:
            tour_cost += calc_euclidean(last_city, city)
            visited.add(city)
            last_city = city

        if len(set(path)) != len(path):
            return False, 0.0
        
        total_cost += tour_cost

    # Check if all cities are visited exactly once
    if len(set(visited)) != 20:  # 21 cities, visited set should have 20 distinct non-depot cities
        return False, 0.0

    return True, total_cost

# Validate conditions
correct_start_loc = {0: 0, 1: 1}
valid, computed_cost = validate_solution(solution_paths, correct_start_loc)
if valid and abs(computed_cost - 456.6149263442546) < 1e-5:
    print("CORRECT")
else:
    print("FAIL")