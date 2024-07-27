import math

# Given problem data
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Calculated tour and cost from solver output
tour = [0, 3, 0]
reported_cost = 14.142135623730951

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour_and_cost(tour, reported_cost):
    # Check if tour starts and ends at the depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check if all cities are visited exactly once excluding the depot
    visited = set(tour) - {0}
    if visited != set(range(1, 20)):
        return "FAIL"

    # Calculate the total travel cost and compare with reported cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Running test
test_result = validate_tour_and_cost(tour, reported_cost)
print(test_result)