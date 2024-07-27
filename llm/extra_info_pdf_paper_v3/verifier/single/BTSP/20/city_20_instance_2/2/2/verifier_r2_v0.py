import math

# Data for the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # Requirement 1 & 4: Check if all cities are visited exactly once and start/end at depot
    if sorted(tour) != sorted(list(range(20)) + [0]) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total travel cost and max distance
    calculated_cost = 0
    calculated_max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_dist:
            calculated_max_dist = dist

    # Requirement 5: Check total travel cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 6: Check maximum distance
    if not math.isclose(calculated_max_dist, max_distance, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Test the provided solution
solution_tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
solution_total_cost = 478.4306776278287
solution_max_distance = 80.61017305526642

# Resulting output
result = verify_solution(solution_t Oops…ry_solution_tour, solution_total_cost, solution_max_distance)
print(result)