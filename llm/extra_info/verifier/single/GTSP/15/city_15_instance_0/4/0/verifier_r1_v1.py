import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Starts or ends at the wrong city
    
    visited_groups = set()
    calculated_cost = 0
    
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        calculated_cost += euclidean_distance(*city_coordinates[city_a], *city_coordinates[city_b])
        
        # Check if city belongs to one of the groups and record the group
        for idx, group in enumerate(city_groups):
            if city_a in group:
                visited_groups.add(idx)
                break

    # Check if each group was visited once
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check if the calculated cost matches the provided cost within a tolerance
    if not math.isclose(calculated_cost, total_costs, rel_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Given cities coordinates
city_coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Given groups 
city_groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]

# Tour and cost provided in the output
tour = [0, 10, 1, 9, 0]
total_costs = 122.21527940040238

# Perform verification
result = verify_solution(tour, total_costs, city_coordinates, city_groups)
print(result)