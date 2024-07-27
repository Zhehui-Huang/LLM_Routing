import math
from itertools import permutations

# Define the locations of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Compute Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Generate the distance matrix
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')

# A simple heuristic to find a tour that minimizes maximum distance between consecutive cities
def find_tour():
    all_tours = permutations(range(1, n))  # Generate all permutations of cities except the starting depot
    min_max_dist = float('inf')
    best_tour = None
    best_total_cost = 0

    for tour in all_tours:
        tour_with_depot = [0] + list(tour) + [0]  # Add depot to the start and end of the tour
        max_dist_in_tour = 0
        total_cost = 0
        for i in range(len(tour_with_depot) - 1):
            dist = distances[tour_with_depot[i]][tour_with_depot[i+1]]
            total_cost += dist
            if dist > max_dist_in_tour:
                max_dist_in_tour = dist
        if max_dist_in_tour < min_max_dist:
            min_max_dist = max_dist_in_tour
            best_tour = tour_with_depot
            best_total_cost = total_cost

    return best_tour, best_total_cost, min_max_dist

# Execute the tour finding function
tour, total_cost, max_distance = find_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")