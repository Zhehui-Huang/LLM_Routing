import math

def verify_solution(tour, computed_cost):
    # Define cities with their coordinates
    city_coordinates = [
        (8, 11),  # Depot 0
        (40, 6),  # City 1
        (95, 33), # City 2
        (80, 60), # City 3
        (25, 18), # City 4
        (67, 23), # City 5
        (97, 32), # City 6
        (25, 71), # City 7
        (61, 16), # City 8
        (27, 91), # City 9
        (91, 46), # City 10
        (40, 87), # City 11
        (20, 97), # City 12
        (61, 25), # City 13
        (5, 59),  # City 14
        (62, 88), # City 15
        (13, 43), # City 16
        (61, 28), # City 17
        (60, 63), # City 18
        (93, 15)  # City 19
    ]
    
    # Groups of cities
    city_groups = [
        [1, 3, 5, 11, 13, 14, 19],
        [2, 6, 7, 8, 12, 15],
        [4, 9, 10, 16, 17, 18]
    ]
    
    # Check solution starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check only one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot city
        found_group = False
        for idx, group in enumerate(city_groups):
            if city in group:
                if idx in visited_groups:
                    return "FAIL"
                visited_groups.add(idx)
                found_group = True
        if not found_group:
            return "FAIL"

    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Verify that cost is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i+1]]
        calculated_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    if abs(calculated_cost - computed_cost) > 0.5:  # acceptable floating point tolerance
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Provided solution variables corrected
tour_solution = [0, 1, 8, 4, 0]
total_cost_solution = 110.09
result = verify_solution(tour_solution, total_cost_solution)

print(result)