import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(tour, total_cost, cities, groups):
    # Verify that tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify that exactly one city from each group is visited
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Exclude the first and last city as they are the depot
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True

    if not all(visited_groups):
        return "FAIL"

    # Verify the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # If all checks passed
    return "CORRECT"

# City coordinates
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

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],  # Group 0
    [2, 6, 7, 8, 12, 15],       # Group 1
    [4, 9, 10, 16, 17, 18]      # Group 2
]

# Tour provided in the solution
given_tour = [0, 1, 8, 4, 0]
given_total_cost = 110.08796524611944

# Checking the solution
result = verify_solution(given_tour, given_total_cost, cities, groups)
print(result)  # Output should be "CORRECT" if all conditions are satisfied