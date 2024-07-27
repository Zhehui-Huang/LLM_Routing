import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour(tour, given_total_travel_cost):
    cities = [
        (90, 3),   # Depot city 0
        (11, 17),  # City 1
        (7, 27),   # City 2
        (95, 81),  # City 3
        (41, 54),  # City 4
        (31, 35),  # City 5
        (23, 95),  # City 6
        (20, 56),  # City 7
        (49, 29),  # City 8
        (13, 17)   # City 9
    ]
    city_groups = [
        [3, 6],  # Group 0
        [5, 8],  # Group 1
        [4, 9],  # Group 2
        [1, 7],  # Group 3
        [2]      # Group 4
    ]

    # Check to ensure the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check for exactly one city visited from each group
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # Exclude the first and last city (depot)
        found_group = False
        for group_index, group in enumerate(city_groups):
            if city in group:
                if visited_groups[group_index] >= 1:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups[group_index] += 1
                found_group = True
        if not found_group:
            return "FAIL"  # City not found in any group

    if any(v != 1 for v in visited_groups):
        return "FAIL"  # Not all groups visited

    # Calculate total travel distance
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        total_travel_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check if the travel cost matches the given one
    if not math.isclose(total_travel_cost, given_total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided tour and expected cost (corrected typo here as well)
tour = [0, 3, 5, 5, 4, 1, 9, 0]  # Correct the tour if necessary this is only for example
given_total_travel_cost = 273.3072642077373
result = check_tour(tour, given_total_travel_cost)
print(result)