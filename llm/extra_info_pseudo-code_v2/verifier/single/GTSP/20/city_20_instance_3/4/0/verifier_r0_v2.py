import math

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    """Verify if the given GTSP tour and cost satisfy the problem requirements."""
    
    # Requirement 1: Tour starts and ends at the depot city (city index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visits exactly one city from each of the 6 distinct groups
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:  # Exclude the depot city
        in_group = False
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # This group has already been visited
                visited_groups[i] = True
                in_group = True
                break
        if not in_group:
            return "FAIL"  # Visited city does not belong to any group
    
    if not all(visited_groups):
        return "FAIL"  # Not all groups are visited exactly once

    # Requirement 3: Travel cost calculated using Euclidean distance
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(total_cost, computed_cost, rel_tol=1e-5):
        return "FAIL"  # The total travel cost is not correct

    # Requirement 4 & 5 are ensured by the tour format and cost output
    return "CORRECT"

# Test data
city_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]
tour = [0, 11, 16, 15, 6, 13, 19, 0]
total_cost = 219.43829363969311

result = verify_solution(tour, total_cost, city_coordinates, city_groups)
print(result)