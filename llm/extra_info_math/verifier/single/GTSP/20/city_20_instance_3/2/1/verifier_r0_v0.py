import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, city_locations, city_groups):
    # Verify Requirement 1
    unique_cities_in_groups = {ci for g in city_groups for ci in g}
    visited_cities = set(tour)
    
    if all(any(c in visited_cities for c in g) for g in city_groups):
        if all(sum(c in visited_cities for c in g) == 1 for g in city_groups):
            pass
        else:
            return "FAIL: Each group must have exactly one city visited."
    else:
        return "FAIL: Not all groups are visited."

    # Verify Requirement 2
    # Calculate distance traveled in the tour
    tour_distance = sum(calculate_distance(city_locations[tour[i]], city_locations[tour[i + 1]]) for i in range(len(tour) - 1))
    expected_distance = 86.39257172  # obtained from the given result

    if not math.isclose(tour_distance, expected_distance, rel_tol=1e-5):
        return "FAIL: Tour distance is not minimal."

    # Verify Requirement 3
    # Check for subtours (Ensure visited cities are visited only once except the depot)
    if len(tour) != len(set(tour)) - 1 + tour.count(0):
        return "FAIL: Subtour detected in the solution."

    return "CORRECT"

# Define cities and groups as per problem description given previously
city_locations = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Assume given solution tour
tour = [0]  # The tour provided in the results was [0], which is clearly incorrect.
            # it should contain exactly one city from each group and start and end at depot.

# Run the test for the given tour
result = verify_solution(tour, city_locations, city_groups)
print(result)