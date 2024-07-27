import math

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, city_coordinates, groups):
    # [Requirement 1] Starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visits exactly one city from each city group
    visited_cities = set(tour[1:-1])  # Except the depot
    found_groups = set()
    for city in visited_cities:
        for group_idx, group in enumerate(groups):
            if city in group:
                found_groups.add(group_idx)
                break
    if len(found_groups) != 3:
        return "FAIL"
    
    # [Requirement 3] Check for the shortest tour by validating the cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates including the depot
city_coordinates = [
    (50, 42),  # Depot
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Group divisions
groups = [
    [1, 2, 6],  # Group 0
    [3, 7, 8],  # Group 1
    [4, 5, 9]   # Group 2
]

# Solution given from the solver
tour = [0, 5, 0]
total_travel_cost = 8.48528137423857

# Execute the verification test
result = verify_solution(tour, total_travel_cost, city_coordinates, groups)
print(result)