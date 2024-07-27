import math

# Position data for each city including the depot
positions = {
    0: (14, 77),  # Depot
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# City groups
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Provided test tour and its cost
test_tour = [0, 6, 13, 2, 9, 0]
test_cost = 114.66

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def assess_solution(tour, expected_cost):
    # Check the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Compile the indices of cities actually visited
    visited_cities = tour[1:-1]

    # Check that one city from each group is visited
    group_checks = all(any(city in group for city in visited_cities) for group in city_groups)
    if not group_checks:
        return "FAIL"

    # Check if all visited cities are from different groups
    seen_groups = []
    for city in visited_cities:
        for group_idx, group in enumerate(city_groups):
            if city in group:
                if group_idx in seen_groups:
                    return "FAIL"
                seen_groups.append(group_idx)

    # Calculate the tour cost
    actual_cost = sum(calculate_euclidean_distance(positions[tour[i]], positions[tour[i + 1]]) 
                      for i in range(len(tour) - 1))

    # Compare calculated cost with expected cost
    if not math.isclose(actual_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Validate the test solution
result = assess_solution(test_tour, test_cost)
print(result)