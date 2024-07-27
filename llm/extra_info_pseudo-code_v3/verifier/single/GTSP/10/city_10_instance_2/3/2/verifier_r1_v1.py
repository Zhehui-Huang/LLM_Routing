import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour(tour, given_total_travel_cost):
    cities = [
        (90, 3),   # City 0 - Depot
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
        [3, 6],    # Group 0
        [5, 8],    # Group 1
        [4, 9],    # Group 2
        [1, 7],    # Group 3
        [2]        # Group 4
    ]

    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # skip the first and last entry as they are the depot
        for group_index, group in enumerate(city_groups):
            if city in group:
                if visited_groups[group_index] >= 1:
                    return "FAIL"
                visited_groups[group_index] += 1

    if any(v != 1 for v in visited_groups):
        return "FAIL"

    # Calculate the travel cost
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        total_travel_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Check if the total calculated distance matches the given total travel cost
    if not math.isclose(total_travel_dict, given_total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided tour and cost
tour = [0, 3, 5, 2, 1, 9, 0]
given_total_travel_cost = 273.3072642077373
result = check_tour(tour, given_total_travel_cost)
print(result)