import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)

def test_solution(tour, total_travel_cost):
    city_coords = [
        (9, 93),   # 0 - Depot
        (8, 51),   # 1
        (74, 99),  # 2
        (78, 50),  # 3
        (21, 23),  # 4
        (88, 59),  # 5
        (79, 77),  # 6
        (63, 23),  # 7
        (19, 76),  # 8
        (21, 38),  # 9
        (19, 65),  # 10
        (11, 40),  # 11
        (3, 21),   # 12
        (60, 55),  # 13
        (4, 39)    # 14
    ]
    
    groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]
    
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot (start and end)
        found_group = False
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in visited_group:
                    return "FAIL"
                visited_groups.add(group_index)
                found_group = True
                break
        if not found_group:
            return "FAIL"
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate and validate the total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    
    # Comparing costs (allowing slight floating point differences)
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Given tour and cost
tour = [0, 8, 10, 9, 0]
total_travel_cost = 114.09

# Output test result
result = test_solution(tour, total_travel_cost)
print(result)