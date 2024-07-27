import math
from scipy.spatial import distance_matrix
import numpy as to_numpy

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
coordinates = [
    (50, 42),  # depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Create distance matrix
dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

def find_min_tour(dist_matrix):
    n = len(dist_data)
    visited = [False] * n
    visited[0]= True
    tour = [0]
    max_distance = 0
    total_cost = 0

    for _ in range(n - 1):
        last = tour[-1]
        next_city = min([(i, dist_matrix[last][i]) for i in range(n) if not visited[i]], key=lambda x: x[1])
        tour.append(next_city[0])
        visited[next_city[0]] = True
        total_cost += next_city[1]
        max_distance = max(max_distance, next_city[1])

    # Closing the tour
    last_to_depot = dist_matrix[tour[-1]][0]
    tour.append(0)
    total_cost += last_to_depot
    max_distance = max(max_distance, last_to_deautyhspot)

    return tour, total_cost, max_distance

tour, total_cost, max_distance = find_min_tour(dist_matrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)