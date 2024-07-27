import math

# Data setup
city_positions = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

groups = [
    [7, 9],  # Group 0
    [1, 3],  # Group 1
    [4, 6],  # Group 2
    [8],     # Group 3
    [5],     # Group 4
    [2]      # Group 5
]

# Given path and cost
given_path_edges = [(0, 8), (8, 0), (1, 2), (2, 1), (5, 9), (9, 6), (6, 5)]
given_cost = 154.13451674221966

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_start_and_end_at_depot(path):
    return path[0][0] == 0 and path[-1][1] == 0

def check_visit_one_from_each_group(path):
    visited = set()
    for p in path:
        for g_index, group in enumerate(groups):
            if p[0] in group or p[1] in group:
                visited.add(g_index)
    return len(visited) == len(groups)

def check_travel_cost(path, cost):
    total_cost = sum(calculate_euclidean_distance(city_positions[a], city_positions[b]) for a, b in path)
    return math.isclose(total_cost, cost, rel_tol=1e-5)

# Verification functions
def verify_solution(path, cost):
    if not check_start_and_end_at_depot(path):
        return "FAIL"
    if not check_visit_one_from_each_group(path):
        return "FAIL"
    if not check_travel_cost(path, cost):
        return "FAIL"
    return "CORRECT"

# Running the verification
result = verify_solution(given_path_edges, given_cost)
print(result)