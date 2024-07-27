import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_distances(cities):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = distances[j][i] = dist
    return distances

def find_minimum_bottleneck_tour(cities):
    n = len(cities)
    dist = calculate_distances(cities)

    # A brute-force approach
    # Compatibly small for up to about 10 cities
    best_max_edge = float('inf')
    best_tour = None
    
    for perm in permutations(range(1, n)):
        # Form the tour with the starting and ending at the depot (0)
        tour = [0] + list(perm) + [0]
        max_edge = max(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        if max_edge < best_max_edge:
            best_max_edge = max_edge
            best_tour = tour
    
    total_cost = sum(dist[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))

    return best_tour, total_cost, best_max_edge

# Coordinates of the cities
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
          (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Execute the function to obtain the tour, cost, and the max distance
tour, total_cost, max_distance = find_minimum_bottleneck_tour(cities)

# Print the results
output = f"Tour: {tour}\nTotal travel cost: {total_cost:.2f}\nMaximum distance between consecutive cities: {max_distance:.2f}"
print(output)