import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_solution(tour, expected_cost, city_coordinates, city_groups):
    # Check: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check: Visit exactly one city from each group
    visited_groups = set()
    for city_index in tour[1:-1]:  # Exclude depot city at start and end
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                if group_index in visited_group:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups.add(group_index)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check: Travel costs and shortest tour
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Tolerance for floating point comparison
    if not math.isclose(total_calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
city_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]

# City groups
city_groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Proposed tour and cost
proposed_tour = [0, 14, 5, 10, 11, 8, 9, 0]
proposed_cost = 166.75801920718544

# Testing
result = test_tour_solution(proposed_tour, proposed_cost, city_coordinates, city_groups)
print(result)