import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def check_tour_requirements(tour, city_locations, city_groups):
    # Requirement 1: Start and end at depot (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly one city from each city group
    visited_groups = [False] * len(city_groups)
    unique_cities = set(tour)
    for city_index in tour:
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                if visited_groups[group_index]:
                    return "FAIL"
                visited_groups[group_index] = True
    if not all(visited_groups):
        return "FAIL"

    # Requirement 3: Travel between any two cities to calculate Euclidean distance
    total_distance_computed = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_distance_computed += calculate_distance(city_locations[city1], city_locations[city2])

    # Requirements 4: Using the same computation for total travel cost check
    provided_total_distance = 273.0065204434128
    if not math.isclose(total_distance_computed, provided_total_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Test input from the task description
city_locations = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15],
    [1, 3, 19], [8, 11, 18]
]

tour = [0, 17, 6, 12, 2, 19, 18, 0]

# Checking if the solution is correct
result = check_tour_requirements(tour, city_locations, city_groups)
print(result)