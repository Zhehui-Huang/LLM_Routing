import itertools
import math
from scipy.spatial.distance import euclidean

# Define the cities as (x, y) coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate distances between each pair of cities
def calculate_distance(city1, city2):
    return euclidean(city1, city2)

edges = []
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        distance = calculate_distance(cities[i], cities[j])
        edges.append((distance, i, j))

# Sort edges by distance
edges.sort()

# Function to find Hamiltonian path using DFS
def valid_tour(visited):
    return len(visited) == len(cities) and visited[-1] == 0

def dfs(current, visited, adj, max_distance):
    if valid_tour(visited):
        return visited, max_distance
    for neighbor in adj[current]:
        if neighbor not in visited or (neighbor == 0 and len(visited) == len(cities)):
            visited.append(neighbor)
            new_max_dist = max(max_distance, calculate_distance(cities[current], cities[neighbor]))
            result = dfs(neighbor, visited, adj, new_max_dist)
            if result:
                return result
            visited.pop()
    return None

# Attempt to construct a valid tour for each increasing distance threshold
for max_dist, _, _ in edges:
    adj = {i: [] for i in range(len(cities))}
    # Build the graph with the current max distance constraint
    for dist, u, v in edges:
        if dist <= max_dist:
            adj[u].append(v)
            adj[v].append(u)
        else:
            break
    
    # Use DFS to find a Hamiltonian path that starts and ends at the depot city (0)
    tour = dfs(0, [0], adj, 0)
    if tour:
        path, max_edge_distance = tour
        # Calculate total travel cost
        total_distance = sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_distance}")
        print(f"Maximum distance between consecutive cities: {max_edge_distance}")
        break