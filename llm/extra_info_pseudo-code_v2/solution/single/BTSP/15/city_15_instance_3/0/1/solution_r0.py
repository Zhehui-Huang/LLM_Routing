import itertools
from math import sqrt
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
import numpy as np

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_biconnected(G, V):
    # Assume Edge list is given in non-decreasing order
    for n_edges in range(1, len(G) + 1):
        subset = G[:n_edges]  # First n_edges
        sparse_matrix = csr_matrix(
            ([1]*len(subset), ([e[0] for e in subset], [e[1] for e in subset])), shape=(V, V)
        )
        n_components, labels = connected_components(sparse_matrix, connection='strong')
        if n_components == 1:
            return subset
    return []

def construct_tour(E_BB, V):
    # This function constructs an approximate optimal tour. Simple nearest neighbor heuristic.
    unvisited = set(range(V))
    current = 0
    tour = [0]
    unvisited.remove(0)
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(0)  # Complete the cycle
    return tour

def calculate_tour_cost(tour, cities):
    total_cost = 0
    max_consecutive_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        max_consecutive_distance = max(max_consecutive_distance, dist)
    return total_cost, max_consecutive_distance

# Define the cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]

# Calculate all inter-city distances
N = len(cities)
edges = []
for i, j in itertools.combinations(range(N), 2):
    distance = euclidean_distance(cities[i], cities[j])
    edges.append((i, j, distance))
    edges.append((j, i, distance))

# Sort edges by weight
edges_sorted = sorted(edges, key=lambda x: x[2])

# Find the biconnected subgraph
E_BB = find_biconnected(edges_sorted, N)

# Construct the tour
tour = construct_tour(E_BB, N)

# Calculate the tour cost
total_cost, max_distance = calculate_tour_cost(tour, cities)

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)