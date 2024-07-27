import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_tour(tour, total_cost, cities, groups):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if one city from each group is visited
    unique_cities = set(tour[1:-1])  # Exclude the depot city at start and end
    if len(unique_cities) != 7:
        return "FAIL"

    group_membership = {city: idx for idx, group in enumerate(groups) for city in group}
    visited_groups = set(group_membership[city] for city in unique_cities)
    if len(visited_groups) != 7:
        return "FAIL"

    # Check if the travel cost is correctly calculated
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Define cities with their coordinates
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

# Define groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Solution provided
tour = [0, 3, 6, 8, 9, 5, 7, 4, 0]
total_cost = 307.35

# Validate the solution
result = verify_tour(tour, total_cost, cities, groups)
print(result)