import math
import sys

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

def nearest_neighbor_tour(cities, start=0):
    n = len(cities)
    visited = set([start])
    tour = [start]
    current = start

    while len(tour) < n:
        next_city = min((i for i in range(n) if i not in visited), key=lambda i: cities[current][i])
        tour.append(next_city)
        visited.add(next_city)
        current = next_city

    tour.append(start)  # Returning to the start city (depot)
    return tour

def calculate_tour_cost(dist_matrix, tour):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def maximize_min_distance(dist_matrix, tour):
    max_dist = 0
    for i in range(len(tour)-1):
        max_dist = max(max_dist, dist_matrix[tour[i]][tour[i+1]])
    return max_dist

# Define cities' coordinates
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
          (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Calculate distance matrix
dist_matrix = create_distance_matrix(cities)

# Generate an initial tour using the nearest neighbor heuristic
nn_tour = nearest_neighbor_tour(dist_matrix)
nn_total_cost = calculate_tour_cost(dist_matrix, nn_tour)
max_distance = maximize_min_distance(dist_matrix, nn_tour)

print(f"Tour: {nn_tour}")
print(f"Total travel cost: {nn_total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")