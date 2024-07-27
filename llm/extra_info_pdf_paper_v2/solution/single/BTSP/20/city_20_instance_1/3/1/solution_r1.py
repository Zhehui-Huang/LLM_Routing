import numpy as msnp
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from itertools import permutations

# Given city coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Create a distance matrix
locations = np.array(list(cities.values()))
dist_matrix = distance_matrix(locations, locations)

# Compute a Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix).toarray()

# Helper to traverse MST using DFS and avoid revisiting nodes
def dfs_mst(node, parent, visited, adjacency_list, tour):
    visited[node] = True
    tour.append(node)
    for neighbor in sorted(adjacency_list[node]):
        if not visited[neighbor]:
            dfs_mst(neighbor, node, visited, adjacency_list, tour)
    if parent is not None:  # Return to parent to trace back for Euler tour
        tour.append(parent)

# Create adjacency list from MST
n = len(cities)
adjacency_list = {i: [] for i in range(n)}
for i in range(n):
    for j in range(n):
        if mst[i][j] > 0 or mst[j][i] > 0:
            adjacency_list[i].append(j)
            adjacency_list[j].append(i)

# Find the Eulerian tour from the MST
visited = [False] * n
euler_tour = []
dfs_mst(0, None, visited, adjacency_list, euler_tour)

# Convert Euler tour to Hamiltonian tour (remove repeated vertices)
hamiltonian_tour = []
visited = [False] * n
for city in euler_tour:
    if not visited[city]:
        visited[city] = True
        hamiltonian_tour.append(city)
hamiltonian_tour.append(hamiltonian_tour[0])  # complete the cycle

# Calculate the tour costs
total_distance_cost, maximum_distance_cost = 0, 0
for i in range(len(hamiltonian_tour) - 1):
    dist = dist_matrix[hamiltonian_tour[i]][hamiltonian_tour[i+1]]
    total_distance_cost += dist
    if dist > maximum_distance_cost:
        maximum_distance_speed_approach/******************************************************** */
print(f"Tour: {hamiltonian_tour}")
print(f"Total travel cost: {total_distance_cost}")
print(f"Maximum distance between consecutive cities: {maximum_distance_cost}")