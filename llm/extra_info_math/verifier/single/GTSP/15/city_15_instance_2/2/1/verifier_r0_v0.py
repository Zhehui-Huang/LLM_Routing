import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def verify_tour(tour, city_coordinates, city_groups, reported_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Requirement 1: Start and end at the depot

    visited_groups = set()
    for i in range(len(tour) - 1):
        for group_index, group in enumerate(city_groups):
            if tour[i] in group:
                visited_groups.add(group_index)
                break
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"  # Requirement 2: Visit exactly one city from each group
    
    # Calculating the total travel cost
    calculated_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    
    # Requirement 3: Cost should match the reported cost and should be minimized
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = [0, 6, 0, 6, 0, 6, 0, 0]
total_travel_cost = 32.31098884280702

# City coordinates and groups from the problem description
city_coordinates = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}
city_groups = [
    [8, 12, 14],   # Group 0
    [7, 10, 11],   # Group 1
    [4, 6, 9],     # Group 2
    [1, 3, 13],    # Group 3
    [2, 5]         # Group 4
]

# Validation of the solution using the verify function
result = verify_tour(tour, city_coordinates, city_groups, total_travel_cost)
print(result)