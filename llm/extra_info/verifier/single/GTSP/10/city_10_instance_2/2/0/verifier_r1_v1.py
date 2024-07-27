import math

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define group membership
groups = [
    [3, 6],  # Group 0
    [5, 8],  # Group 1
    [4, 9],  # Group 2
    [1, 7],  # Group 3
    [2]      # Group 4
]

# Provided solution
tour = [0, 3, 5, 9, 1, 2, 0]
reported_cost = 281.60273931778477

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour_requirements(tour, groups, cities, reported_cost):
    # Requirement 1: Starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: One city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot at start/end
        found = False
        for idx, group in enumerate(groups):
            if city in group:
                if idx in visited_groups:
                    return "FAIL"  # Duplicate group visit
                visited_groups.add(idx)
                found = True
                break
        if not found:
            return "FAIL"  # City not in any group
    if len(visited_groups) != len(groups):
        return "FAIL"

    # Requirement 3 & 4: Compute the total travel cost and compare with reported_cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += compute_euclidean�_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_tour_requirements(tour, groups, cities, reported_cost)
print(result)