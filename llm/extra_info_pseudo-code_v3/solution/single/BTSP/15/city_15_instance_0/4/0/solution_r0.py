import math
from itertools import permutations

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Check if a graph has a Hamiltonian path using permutation (brute-force)
def has_hamiltonian_path(graph, n):
    for perm in permutations(range(1, n)):  # Exclude the depot which is 0 and is start and end point
        all_connected = True
        path = [0] + list(perm) + [0]
        for i in range(len(path) - 1):
            if path[i + 1] not in graph[path[i]]:
                all_connected = False
                break
        if all_connected:
            return True, path
    return False, []

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23),
          (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]
n = len(cities)

# Calculate distances between all cities
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Creating list of all edges with their distances
edges = [(i, j, distances[i][j]) for i in range(n) for j in range(i + 1, n)]

# Sort edges based on distance
edges.sort(key=lambda x: x[2])

# Attempt to find Hamiltonian path that minimizes the maximum edge weight
for threshold in edges:
    graph = {i: set() for i in range(n)}
    for i, j, dist in edges:
        if dist > threshold[2]:
            break
        graph[i].add(j)
        graph[j].add(i)
    
    exist, path = has_hamiltonian_path(graph, n)
    if exist:
        max_edge_length = 0
        total_travel_cost = 0
        for i in range(len(path) - 1):
            travel_cost = distances[path[i]][path[i + 1]]
            total_travel_cost += travel_cost
            if travel_cost > max_edge_length:
                max_edge_length = travel_cost
        
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_travel_cost}")
        print(f"Maximum distance between consecutive cities: {max_edge_length}")
        break