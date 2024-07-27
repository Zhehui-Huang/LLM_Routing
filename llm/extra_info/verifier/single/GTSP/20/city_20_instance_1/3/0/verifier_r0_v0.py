import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_cost_calculated, city_coordinates, city_groups):
    # Requirement 1: Starts and ends at City 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly one city from each group
    groups_visited = set()
    for city_index in tour[1:-1]:  # skip the depot in the start and end
        for i, group in enumerate(city_groups):
            if city_index in group:
                groups_visited.add(i)
    if len(groups_visited) != len(city_groups):
        return "FAIL"
    
    # Requirement 3: Travel cost using the Euclidean distance
    total_cost_computed = 0
    for i in range(len(tour) - 1):
        city1 = city_coordinates[tour[i]]
        city2 = city_coordinates[tour[i+1]]
        total_cost_computed += calculate_distance(city1, city2)
    
    # Compare computed cost with given cost (allowing a small margin for floating-point arithmetic handling)
    if not math.isclose(total_cost_computed, total_cost_calculated, rel_tol=1e-5):
        return "FAIL"
    
    # If all requirements are satisfied
    return "CORRECT"

# Cities with coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],  # Group 0
    [1, 4, 8, 13, 16],  # Group 1
    [2, 10, 15, 18, 19],  # Group 2
    [3, 9, 12, 14]  # Group 3
]

# Provided tour and cost
provided_tour = [0, 6, 13, 2, 14, 0]  # corrected tour with city from Group 3 pending verification
provided_total_cost = 114.66

# Verify the solution
result = verify_solution(provided_tour, provided_total_cost, [cities[i] for i in range(20)], groups)
print(result)