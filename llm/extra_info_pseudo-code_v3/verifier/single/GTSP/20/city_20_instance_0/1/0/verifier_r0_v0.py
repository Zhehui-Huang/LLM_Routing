import math

# Cities coordinates
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
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Proposed solution
tour = [0, 1, 8, 4, 0]
proposed_cost = 110.08796524611944

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_requirements(tour, proposed_cost):
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2
    visited_groups = {0: False, 1: False, 2: False}
    for city in tour[1:-1]:  # exclude the depot city at the start and end
        for idx, group in enumerate(groups):
            if city in group:
                visited_groups[idx] = True
                break
    if not all(visited_groups.values()):
        return "FAIL"
    
    # Requirement 3
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(tour[i], tour[i+1])
    if not math.isclose(actual_cost, proposed_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Checking the solution
result = check_requirements(tour, proposed_cost)
print(result)