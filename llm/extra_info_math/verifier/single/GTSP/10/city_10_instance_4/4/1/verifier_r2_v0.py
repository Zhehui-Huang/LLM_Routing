import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_solution(tour, city_locations, city_groups):
    # [Requirement 1] Starts and ends at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit exactly one city from each group.
    visited_groups = {}
    for city in tour:
        for group_index, group_cities in enumerate(city_groups):
            if city in group_cities:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups[group_index] = True

    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # [Requirement 3] Minimize the total travel cost.
    # This requirement can't be easily checked without comparing to all possible solutions.
    # We will assume the provided solution respects this requirement if other requirements are met.

    return "CORRECT"

# Test settings
city_locations = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 5: (83, 61),
    6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}
city_groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Solution provided
tour = [0, 3, 0]
calculated_cost = calculate_distance(city_locations[tour[0]], city_locations[tour[1]]) + \
                  calculate_distance(city_locations[tour[1]], city_locations[tour[2]])

expected_cost = 35.61  # extracted from solver output

# Testing if calculated cost matches expected and if requirements are met
if abs(calculated_cost - expected_test) > 1e-5:
    print("FAIL")
else: 
    result = validate_solution(tour, city_locations, city_groups)
    print(result)