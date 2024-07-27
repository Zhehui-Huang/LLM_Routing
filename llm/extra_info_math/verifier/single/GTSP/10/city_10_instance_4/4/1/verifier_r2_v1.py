import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_solution(tour, city_locations, city_groups):
    # [Requirement 1] Starts and ends at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit exactly one city from each group.
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at beginning and end.
        found_group = False
        for group_index, group_cities in enumerate(city_groups):
            if city in group_cities:
                if group_index in visited_groups:
                    return "FAIL"  # City from the same group visited more than once.
                visited_groups.add(group_index)
                found_group = True
                break
        if not found_group:
            return "FAIL"  # No group found for the city.
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"  # Not all groups were visited.

    return "CORRECT"

# Test settings
city_locations = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 5: (83, 61),
    6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}
city_groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Solution provided
tour = [0, 3, 0]
actual_cost = calculate_distance(city_locations[tour[0]], city_locations[tour[1]]) + \
              calculate_distance(city_locations[tour[1]], city_locations[tour[2]])

expected_cost = 35.61  # Extracted from solver output

# Testing if calculated cost matches expected and if requirements are met
if abs(actual_cost - expected_cost) > 1e-5:
    print("FAIL due to cost mismatch")
else: 
    result = validate_solution(tour, city_locations, city_groups)
    print(result)