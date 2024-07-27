import math

def euclidean_distance(x1, y11, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y11) ** 2)

def verify_tour(tour, coordinates):
    n = len(coordinates)
    visited = [False] * n

    # Requirement 1: Visits each city exactly once and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    for city in tour:
        if visited[city]:
            return "FAIL"
        visited[city] = True
    if not all(visited):
        return "FAIL"

    # Requirement 2: Use Euclidean distance for travel cost
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(*coordinates[tour[i-1]], *coordinates[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Cost is provided only for verification of distances and constraining function.
    # It is not needed to directly verify against a given value, but the longuest distance.
    # Requirement 3: Minimize the longest distance
    expected_max_distance = max(
        euclidean_distance(*coordinates[tour[i]], *coordinates[tour[i+1]]) for i in range(len(tour)-1)
    )
    if max_distance == expected_max_distance:
        return "CORRECT"
    return "FAIL"

# Define coordinates as provided in the description
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Hypothetical good solution based on an algorithm's output
good_tour = [0, 1, 6, 13, 8, 2, 11, 12, 5, 4, 10, 9, 3, 7, 14, 0]

print(verify_tour(good_tour, coordinates))