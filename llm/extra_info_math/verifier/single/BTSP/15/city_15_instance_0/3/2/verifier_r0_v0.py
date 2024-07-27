def verify_tour(tour, distances, max_leg_cost):
    # Verify the tour starts and ends at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify each city is visited exactly once
    visited = set(tour)
    if len(visited) != len(distances):
        return "FAIL"

    # Verify the objective is minimized (max distance between consecutive cities)
    max_distance = 0
    for i in range(len(tour) - 1):
        max_distance = max(max_distance, distances[tour[i]][tour[i+1]])
    if max_distance != max_leg_cost:
        return "FAIL"

    return "CORRECT"

# Sample data
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

from math import sqrt

# Calculate euclidean distances
def calculate_distances(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            distances[i][j] = distances[j][i] = sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return distances

distances = calculate_distances(cities)

# The output from CBC
tour = [0, 1, 9, 14, 11, 12, 4, 7, 3, 5, 13, 6, 2, 8, 10, 0]  # Sample example
max_leg_cost = 30.88689042  # From CBC results

# Call verification function
verification_result = verify_tour(tour, distances, max_leg_cost)
print(verification_result)