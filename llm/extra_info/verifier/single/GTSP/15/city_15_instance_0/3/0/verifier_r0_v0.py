import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour_and_cost(tour, cost, cities, groups):
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visits exactly one city from each city group
    visited_groups = [0 for _ in groups]
    for city in tour[1:-1]:  # Exclude the depot city at the start and end
        found_group = False
        for idx, group in enumerate(groups):
            if city in group:
                visited_groups[idx] += 1
                found_group = True
                break
        if not found_group or any(v > 1 for v in visited_groups):
            return "FAIL"
    if any(v != 1 for v in visited_groups):
        return "FAIL"
    
    # Requirement 3: Travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Allow small margin for floating point comparison
    if not math.isclose(calculated_cost, cost, abs_tol=0.1):
        return "FAIL"

    # Requirement 4 and 5: Correct format is assumed handled externally or by interface
    return "CORRECT"

# Data setup
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}
groups = [
    [2, 7, 10, 11, 14],  # Group 0
    [1, 3, 5, 8, 13],    # Group 1
    [4, 6, 9, 12]        # Group 2
]

# Solution provided
solution_tour = [0, 10, 1, 9, 0]
solution_cost = 122.22

# Validate solution
result = validate_tour_and_cost(solution_tour, solution_cost, cities, groups)
print(result)