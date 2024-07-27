import math

# Robot tours and costs from the given problem's solution
robot_tours = [
    {"tour": [0, 21, 7, 17, 0], "cost": 66.16},
    {"tour": [0, 16, 5, 9, 0], "cost": 74.62},
    {"tour": [0, 6, 22, 8, 0], "cost": 80.08},
    {"tour": [0, 3, 1, 11, 0], "cost": 98.80},
    {"tour": [0, 20, 13, 18, 0], "cost": 89.13},
    {"tour": [0, 15, 19, 10, 0], "cost": 100.83},
    {"tour": [0, 2, 12, 0], "cost": 69.96},
    {"tour": [0, 4, 14, 0], "cost": 97.10}
]

# City coordinates
city_coords = {
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
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Requirement 1: Check start and end at depot
def check_start_end_at_depot():
    for robot in robot_tours:
        if robot["tour"][0] != 0 or robot["tour"][-1] != 0:
            return False
    return True

# Requirement 2: Visit all cities, and visit each city only once
def check_unique_visit():
    visited = [0] * 23  # Including depot
    for robot in robot_tours:
        for city in robot["tour"]:
            if visited[city] > 0 and city != 0:
                return False
            visited[city] += 1
    return sum(visited) == 23  # All cities visited

# Requirement 4: Validate travel costs
def validate_costs():
    for robot in robot_array:
        computed_cost = 0
        tour = robot["name"]
        for i in range(len(tour) - 1):
            computed_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        # Allow for small floating-point discrepancies
        if not math.isclose(robot["cost"], computed_requests, rel_tol=1e-4):
            return False
    return True

# Run unit tests
def run_tests():
    if not check_start_end_at_depot():
        return "FAIL"
    if not check_unique_visit():
        return "FAIL"
    if not validate_costs():
        return "FAIL"
    
    # No failures, return passing result
    return "CORRECT"

# Execute tests
result = run_tests()
print(result)