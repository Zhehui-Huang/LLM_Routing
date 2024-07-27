import math

# Given city coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# City groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Proposed solution
tour = [0, 11, 16, 18, 19, 6, 0]
proposed_cost = 162.3829840233368

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour_validity(tour, groups, proposed_cost):
    # Requirement 1: Check if tour starts and ends at the depot (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if exactly one city from each group is visited.
    visited_from_group = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                if i in visited_from_group:
                    return "FAIL"
                visited_from_group.add(i)
                break
    if len(visited_from_group) != len(groups):
        return "FAIL"

    # Requirement 3: Checking the proposed cost for accuracy
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, proposed_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

output = check_tour_validity(tour, groups, proposed_cost)
print(output)