import math

# Cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 28),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Given solution
robot_tours = {
    0: [0, 2, 7, 15, 9, 14, 12, 3, 8],
    1: [0, 18, 13, 5, 6, 4, 11, 10, 17, 16]
}
robot_cost_given = {
    0: 104.36,
    1: 132.16
}
overall_cost_given = 236.51

# Verification process
def verify_solution():
    all_cities = set(range(19))

    # Check if each robot starts at the designated depot
    if robot_tours[0][0] != 0 or robot_tours[1][0] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once
    visited = set()
    for tour in robot_tours.values():
        visited.update(tour)
    
    if visited != all_cities:
        return "FAIL"

    # Check total travel cost calculations
    total_cost_calculated = 0
    for robot_id, tour in robot_tours.items():
        tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        # Adding direct start cost to shutdown at last visited city, as no return to depot is required
        if abs(tour_cost - robot_cost_given[robot_id]) > 1e-2:
            return "FAIL"
        total_cost_calculated += tour_cost

    if abs(total_cost_calculated - overall_cost_given) > 1e-2:
        return "FAIL"

    return "CORRECT"

# Running the verification
result = verify_solution()
print(result)