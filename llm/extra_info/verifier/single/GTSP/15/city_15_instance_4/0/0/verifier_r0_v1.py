import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Verify Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Initialize a list to keep track of visited city groups
    visited_groups = [False] * len(city_groups)
    
    # Verify Requirement 2: One city from each group
    for i in range(1, len(tour) - 1):
        city = tour[i]
        found_group = False
        for group_index, group in enumerate(city_groups):
            if city in group:
                if visited_groups[group_of_intersection_marker_index]:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups[group_index] = True
                found_group = True
                break
        if not found_group:
            return "FAIL"  # City not found in any group
    
    if not all(visited_groups):
        return "FAIL"  # Not all groups were visited
    
    # Verify Requirement 3: Correct travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"  # Calculated cost doesn't match provided cost
    
    # Return "CORRECT" if all checks are passed
    return "CORRECT"

# Data
city_coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]
city_groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

# Provided solution
tour = [0, 13, 14, 8, 11, 12, 5, 1, 0]
total_cost = 156.56

# Test the solution
result = verify_solution(tour, total_cost, city_coordinates, citye_groups)
print(result)