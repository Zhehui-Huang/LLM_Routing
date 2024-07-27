import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_requirements(tour, total_travel_cost, cities_coordinates, city_groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # The tour must start and end at the depot city 0.

    # Extract actual visited cities excluding the depot city (start and end).
    visited_cities = tour[1:-1]

    # Check if exactly one city from each group is visited.
    visited_from_each_group = {}
    for index, group in enumerate(city_groups):
        visited_from_each_group[index] = any(city in visited_cities for city in group)
    if not all(visited_from_each_group.values()):
        return "FAIL"  # Not all groups are properly visited.

    # Check if total travel cost is correctly calculated.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"  # Mismatch in the reported and calculated travel costs.
    
    return "CORRECT"

# Data
cities_coordinates = [
    (35, 40),  # Depot city 0
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

city_groups = [
    [3, 8],   # Group 0
    [4, 13],  # Group 1
    [1, 2],   # Group 2
    [6, 14],  # Group 3
    [5, 9],   # Group 4
    [7, 12],  # Group 5
    [10, 11]  # Group 6
]

tour = [0, 1, 5, 12, 11, 8, 14, 13, 0]
total_travel_cost = 156.55750207016007

# Test the solution
result = verify_requirements(tour, total_travel_cost, cities_coordinates, city_groups)
print(result)