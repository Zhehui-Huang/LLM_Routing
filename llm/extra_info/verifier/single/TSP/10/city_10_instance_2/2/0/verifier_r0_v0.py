import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(tour, cost, cities):
    # [Requirement 2] Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 1] Check if all cities are visited exactly once
    if sorted(tour) != sorted(set(tour)):
        return "FAIL"
    if set(range(len(cities))) != set(tour):
        return "FAIL"

    # [Requirement 3] Calculate and check travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [(90, 3),    # Depot city 0
          (11, 17),   # City 1
          (7, 27),    # City 2
          (95, 81),   # City 3
          (41, 54),   # City 4
          (31, 35),   # City 5
          (23, 95),   # City 6
          (20, 56),   # City 7
          (49, 29),   # City 8
          (13, 17)]   # City 9

# Given solution
tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
total_travel_cost = 354.91

# Verify the solution
print(verify_solution(tour, total_travel_cost, cities))