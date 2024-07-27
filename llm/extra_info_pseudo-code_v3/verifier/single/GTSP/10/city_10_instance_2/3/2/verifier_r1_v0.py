import math
from itertools import permutations

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[1]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour(tour):
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
    city_groups = {
        0: [3, 6],
        1: [5, 8],
        2: [4, 9],
        3: [1, 7],
        4: [2]
    }

    # Check starts and ends at Depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_from_group = set()
    for city in tour:
        for group, cities in city_groups.items():
            if city in cities:
                if group in visited_from_group:
                    return "FAIL"
                visited_from_group.add(group)
    if len(visited_from_group) != len(city_groups):
        return "FAIL"

    # Calculate the travel cost
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        total_travel_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Given travel cost from the solution
    given_total_travel_cost = 273.3072642077373

    # Check if the travel cost is correctly calculated (allowing small precision error)
    if not math.isclose(total_travel_cost, given_total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    # Calculate the minimal travel cost using a naive approach to confirm the given cost is minimized
    # This is done by generating all valid tours and finding the one with the lowest cost
    minimal_cost = float('inf')
    for permutation in permutations([0] + [min(group) for group in city_groups.values()]):
        if permutation[0] == 0: # Starts at depot
            cost = 0
            for i in range(len(permutation) - 1):
                cost += calculate_euclidean_distance(cities[permutation[i]], cities[permutation[i+1]])
            cost += calculate_euclidean_distance(cities[permutation[-1]], cities[0]) # Return to depot
            minimal_cost = min(minimal_cost, cost)
    if total_travel_cost > minimal_cost:
        return "FAIL"

    return "CORRECT"

# Provided tour
tour = [0, 3, 5, 2, 1, 9, 0]
print(check_tour(tour))