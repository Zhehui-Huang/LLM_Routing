import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, expected_groups, total_cost, coordinates):
    # Check start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check visit one city from each group
    visited_groups = [0]  # Group 0 already visited (depot)
    for city in tour[1:-1]:  # ignoring first and last element as those are depots
        for group_idx, group in enumerate(expected_groups):
            if city in group and group_idx not in visited_groups:
                visited_groups.append(group_idx)
                break
    if sorted(visited_groups) != list(range(len(expected_groups))):
        return "FAIL"
    
    # Check total travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    if abs(calculated_cost - total_cost) > 1e-6:  # Allowing a very small error margin for floating point arithmetic
        return "FAIL"
    
    return "CORRECT"

# Provided outputs
tour = [0, 7, 1, 4, 8, 5, 2, 0]
total_travel_cost = 324.1817486177585

# Define city coordinates and groups
city_coordinates = [
    (84, 67),  # City 0 (depot)
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Groups
city_groups = [
    [0],
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Validation
print(validate_solution(tour, city_groups[1:], total_travel_data, city_coordinates))