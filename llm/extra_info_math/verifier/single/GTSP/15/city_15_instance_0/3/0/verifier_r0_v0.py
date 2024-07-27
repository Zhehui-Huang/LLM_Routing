import math

# Given cities information
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

# Given city groups
city_groups = [
    [2, 7, 10, 11, 14], 
    [1, 3, 5, 8, 13], 
    [4, 6, 9, 12]
]

# Provided tour and calculated total cost
provided_tour = [0, 8, 0, 8, 0]
provided_total_cost = 78.89

# Function to calculate Euclidean distance
def euclidean_distance(ci, cj):
    return math.sqrt((cities[ci][0] - cities[cj][0]) ** 2 + (cities[ci][1] - cities[cj][1]) ** 2)

# Test the requirements
def verify_solution(tour, total_cost):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group of cities
    visited_from_groups = []
    for i in range(1, len(tour) - 1):  # Exclude the depot city from check
        for group_index, group in enumerate(city_groups):
            if tour[i] in group:
                if group_index in visited_from_groups:
                    return "FAIL"
                visited_from_groups.append(group_index)
    if len(visited_from_groups) != len(city_groups):
        return "FAIL"
    
    # Requirement 3: Calculate the total travel cost
    calculated_cost = 0
    for idx in range(len(tour) - 1):
        calculated_cost += euclidean_distance(tour[idx], tour[idx + 1])
    if abs(calculated_cost - total_cost) > 1e-2:  # Allowing a small numerical error margin
        return "FAIL"
    
    return "CORRECT"

# Run the unit test
print(verify_solution(provided_tour, provided_total_path))