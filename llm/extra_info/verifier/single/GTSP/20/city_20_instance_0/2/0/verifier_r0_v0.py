import math

# Provided data
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_travel_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def verify_solution(tour, expected_cost):
    # Check tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check exactly one city from each group
    seen_groups = {}
    for city in tour[1:-1]:  # Ignore depot start and end in tour
        for group_id, group_cities in groups.items():
            if city in group_cities:
                if group_id in seen_groups:
                    return "FAIL"
                seen_groups[group_id] = True
    if len(seen_groups) != 3:
        return "FAIL"

    # Calculate total cost and compare with the expected cost
    calculated_cost = total_travel_cost(tour, cities)
    if not math.isclose(calculated_cost, expected_cost, abs_tol=1e-2):
        return f"FAIL: Expected cost {expected_cost}, got {calculated_cost}"

    return "CORRECT"

# Provided tour and cost
tour_solution = [0, 1, 8, 4, 0]
expected_cost_solution = 110.09

# Verify the given solution
print(verify_solution(tour_solution, expected_cost_solution))