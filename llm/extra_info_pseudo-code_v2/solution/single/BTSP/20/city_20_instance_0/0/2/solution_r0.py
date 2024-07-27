import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

# City coordinates, indexed by city numbers
cities = [
    (8, 11),  # City 0 (Depot)
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

# Calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Total number of cities
n = len(cities)

# Create distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = calc_distance(i, j)
        else:
            distance_matrix[i][j] = float('inf')


# Function to find biconnected graph with minimal max edge
def bottleneck_biconnected_subgraph(n, distance_matrix):
    sorted_edges = [(distance_matrix[i][j], i, j) for i in range(n) for j in range(i + 1, n)]
    sorted_edges.sort()
    
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    E_BB = []
    for weight, u, v in sorted_elements:
        if find(u) != find(v):
            union(u, v)
            E_BB.append((u, v))
    return E_BB

# Convert edges list to adjacency list for further use
def edges_to_adj_list(edges, n):
    adj_list = {i: [] for i in range(n)}
    for u, v in edges:
        adj_unit.append(v)
        adj_list[v].append(u)
    return adj_list

# Depth-first search for finding Hamiltonian path
def dfs_hamiltonian_path(graph, start, path, visited):
    visited.add(start)
    path.append(start)
    if len(path) == len(graph):
        if path[0] in graph[path[-1]]:
            path.append(path[0])  # complete the cycle
            return path
        else:
            path.pop()
            visited.remove(start)
            return None
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs_hamiltonian_path(graph, neighbor, path, visited)
            if result is not None:
                return result
    path.pop()
    visited.remove(start)
    return None

# Main logic to find a tour
def find_tour():
    E_BB = bottleneck_biconnected_subgraph(n, distance_matrix)
    adj_list = edges_to_adj_list(E_BB, n)
    tour = dfs_hamiltonian_path(adj_list, 0, [], set())
    return tour

# Calculate tour statistics
def tour_stats(tour, distance_matrix):
    max_dist = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        dist = distance_matrix[tour[i]][tour[i+1]]
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    return total_cost, max_dist

# Execute the TSP solving
tour = find_tour()
if tour:
    total_cost, max_dist = tour_stats(tour, distance_matrix)
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
    print("No feasible tour found.")