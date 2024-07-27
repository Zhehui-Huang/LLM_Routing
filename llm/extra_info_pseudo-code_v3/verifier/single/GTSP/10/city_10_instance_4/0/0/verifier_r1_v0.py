import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost):
    city_coordinates = [
        (79, 15),  # depot city index 0
        (79, 55),
        (4, 80),
        (65, 26),
        (92, 9),
        (83, 61),
        (22, 21),
        (97, 70),
        (20, 99),
        (66, 62)   # city 9
    ]
    
    groups = [
        [1, 4],  # Group 0
        [2, 6],  # Group 1
        [7],     # Group 2
        [5],     # Group 3
        [9],     # Group 4
        [8],     # Group 5
        [3]      # Group 6
    ]
    
    # Check if all cities including the depot city are included
    if len(city_coordinates) != 10:
        return "FAIL"
    
    # Check if depot city index is correct and tour starts/ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if one city from each group is visited
    visited_groups = set()
    for city in tour:
        for group_index, group in enumerate(groups):
            if city in group:
                visited_groups.add(group_index)
                
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Check if travel cost matches the sum of distances between successive cities in the provided tour
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Given solution verification
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
total_cost = 371.1934423276749

# Verify the solution
result = verify_solution(tour, total_cost)
print(result)