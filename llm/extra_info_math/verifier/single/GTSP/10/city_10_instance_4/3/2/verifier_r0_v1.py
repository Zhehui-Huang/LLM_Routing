import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, travel_cost, cities, groups):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(groups)  # Tracker for each group
    for index in tour:
        for group_id, group_cities in enumerate(groups):
            if index in group_cities:
                visited_groups[group_id] += 1
    if any(count != 1 for count in visited_groups):  # Only one visit per group
        return "FAIL"

    # Compute the total travel cost from the tour and compare it to the given travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, travel_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given solution details
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

tour = [0, 1, 5, 7, 9, 8, 2, 3, 0]
travel_cost = 279.0156928434315

# Verify solution correctness
result = verify_solution(tour, travel_cost, cities, groups)
print(result)