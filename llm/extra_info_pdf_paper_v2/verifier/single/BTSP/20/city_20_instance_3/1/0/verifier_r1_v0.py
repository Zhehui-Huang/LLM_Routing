import math

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour(cities_coordinates, tour, expected_max_dist):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities_coordinates) or len(tour) != len(cities_coordinates) + 1:
        return "FAIL"

    # Requirement 3: Calculate the actual max distance and compare with provided max distance
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = compute_euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        if dist > max_dist:
            max_dist = dist

    if max_dist > expected_max_dist:
        return "FAIL"

    return "CORRECT"

# City coordinates
cities_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Given solution
tour_solution = [0, 1, 4, 7, 14, 8, 18, 12, 10, 11, 3, 15, 5, 17, 16, 9, 19, 6, 13, 2, 0]
expected_max_dist = 72.44

# Check the given solution
result = check_tour(cities_coordinates, tour_solution, expected_max_dist)
print(result)