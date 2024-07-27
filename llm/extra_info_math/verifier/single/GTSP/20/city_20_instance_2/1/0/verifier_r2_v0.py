import math

# City coordinates
city_coordinates = {
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

# Groups of cities
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Tour from solution
tour = [0, 6, 0]
expected_cost = 78.02563681252464

# Calculate Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate total tour cost
def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return total_cost

# Check all requirements
def verify_solution(tour, expected_cost):
    # Requirement 1: Visit exactly one city from each group
    visited_groups = [False] * len(city_groups)
    for city in tour:
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True
    
    if not all(visited_groups):
        return "FAIL"
    
    # Requirement 2: Tour must start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3: Total travel cost should be as given
    calculated_cost = total_tour_cost(tour)
    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Verify the solution
result = verify_solution(tour, expected_cost)
print(result)