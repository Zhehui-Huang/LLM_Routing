import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # [Requirement 1] Start and end at the depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # [Requirement 2] Visit exactly one city from each of the four groups
    visited_groups = set()
    for city in tour:
        for group_index, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(group_index)
    if len(visited_groups) != 4:
        return "FAIL"
    
    # [Requirement 3] Minimize travel cost: calculate the cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates indexed by city number
city_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Groups of cities
city_groups = [
    [5, 6, 7, 11, 17],  # Group 0
    [1, 4, 8, 13, 16],  # Group 1
    [2, 10, 15, 18, 19],# Group 2
    [3, 9, 12, 14]      # Group 3
]

# Proposed solution details
tour = [0, 9, 13, 2, 6, 0]
total_travel_cost = 108.66296159815985

# Verify the provided solution
result = verify_solution(tour, total_travel_cost, city_coordinates, city_groups)
print(result)