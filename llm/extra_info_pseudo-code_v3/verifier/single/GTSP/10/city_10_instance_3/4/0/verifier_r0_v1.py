import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, expected_groups, total_cost, coordinates):
    # Check start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check visit one city from each group
    visited_groups = set()
    for city in tour:
        for group_idx, group in enumerate(expected_groups):
            if city in group:
                visited_groups.add(group_idx)
    if sorted(visited_groups) != list(range(len(expected_span_groups))):
        return "FAIL"
    
    # Check total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Allow a small margin due to floating point arithmetic imprecisions
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Data
tour = [0, 7, 1, 4, 8, 5, 2, 0]
total_travel_cost = 324.1817486177585
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
city_groups = [
    [7, 9],  # Group 0
    [1, 3],  # Group 1
    [4, 6],  # Group 2
    [8],     # Group 3
    [5],     # Group 4
    [2]      # Group 5
]

# Execute the verification
result = validate_solution(tour, city_groups, total_travel_cost, city_coordinates)
print(result)