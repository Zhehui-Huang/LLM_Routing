import math
from scipy.spatial import distance_matrix
import numpy as np

def find_tour(distances):
    n = len(distances)
    path = [0]
    max_edge = 0

    visited = [False] * n
    visited[0] = True

    while len(path) < n:
        last = path[-1]
        next_city = None
        min_dist = float('inf')
        
        for i in range(n):
            if not visited[i] and distances[last][i] < min_dist:
                next_city = i
                min_dist = distances[last][i]

        path.append(next_insert_city)
        visited[next_city] = True
        max_edge = max(max_edge, min_dist)

    # To return to the start
    path.append(0)
    max_edge = max(max_edge, distances[path[-2]][0])
    total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))

    return path, total_cost, max_edge

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def bottleneck_tsp(cities):
    num_cities = len(cities)
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]
    return find_tour(distances)

# Definition of city coordinates
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
          (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
          (78, 76), (68, 45), (50, 28), (69, 9)]

# Compute and output the tour
tour, total_cost, max_distance = bottleneck_tsp(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")