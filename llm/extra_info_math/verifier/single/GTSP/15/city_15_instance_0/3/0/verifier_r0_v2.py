import math

# Given cities and their coordinates
cities = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# City groups based on problem details
city_groups = [
    [2, 7, 10, 11, 14],  # Group 0
    [1, 3, 5, 8, 13],    # Group 1
    [4, 6, 9, 12]        # Group 2
]

# Provided tour sequence and total travel cost
provided_tour = [0, 8, 0, 8, 0]
provided_total_cost = 78.89

# Calculate Euclidean distance between two cities
def euclidean_distance(ci, cj):
    x1, y1 = cities[ci]
    x2, y2 = cities[cj]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verify the provided tour based on the requirements
def verify_solution(tour, total_cost):
    # Requirement 1: Must start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly one city from each group visited
    visited_from_groups = []
    for city in tour:
        for group_index, group in enumerate(city_groups):
            if city in group:
                visited_from_groups.append(group_index)
    if len(set(visited_from_groups)) != len(city_groups):
        return "FAIL"
    
    # Requirement 3: Verify the total tour cost
    calculated_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):  # Allowing a small tolerance
        return "FAIL"
    
    return "CORRECT"

# Execute the verification function
print(verify_solution(provided_tour, provided_total_cost))