import math

# Declaration of cities and their coordinates
cities = {
    0: (8, 11),  # Depot
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

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Proposed solution
tour = [0, 1, 8, 4, 0]
reported_cost = 110.08796524611944

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, groups):
    # Check the tour starts and ends at the depot (Requirement 1 & 5)
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot."
    
    # Check that exactly one city from each group is visited (Requirement 2)
    visited_groups = [0] * len(groups)
    for city in tour:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
                # Ensure only one city per group is chosen
                if visited_groups[i] > 1:
                    return False, f"More than one city from group {i} is visited."
    
    if any(v != 1 for v in visited_groups):
        return False, "Not exactly one city from each group is visited."
    
    # Calculate total travel distance and compare with reported (Requirements 4 & 6)
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if abs(calculated_cost - reported_cost) > 1e-5:
        return False, f"Reported cost ({reported_cost}) does not match calculated cost ({calculated_cost})."
    
    return True, "Test passed."

correct, message = verify_tour(tour, groups)
print("CORRECT" if correct else f"FAIL: {message}")