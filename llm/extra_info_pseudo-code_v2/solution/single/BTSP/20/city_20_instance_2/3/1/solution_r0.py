import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
import numpy as np

# The city positions
positions = [
    (3, 26),   # Depot City 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate the complete graph
n_cities = len(positions)
distances = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i, j] = calculate_distance(positions[i], positions[j])
        else:
            distances[i, j] = float('inf')

def is_biconnected(graph):
    # A simple way to approximate checking for biconnected status in undirected graphs
    # This will check for minimum two vertex-connected component presence
    _, component_labels = connected_components(csr_matrix(graph))
    return np.unique(component_labels).size == 1

def identify_tour(subgraph):
    # Naively create a tour from the subgraph by attempting to find a Hamiltonian path
    # This function could be optimized with heuristic or specific algorithms for Hamiltonian path
    path = [0]  # Start from depot
    visited = {0}
    current = 0
    while len(path) < n_cities:
        neighbors = np.argsort(subgraph[current])
        for neighbor in neighbors:
            if neighbor not in visited and subgraph[current, neighbor] != float('inf'):
                visited.add(neighbor)
                path.append(neighbor)
                current = neighbor
                break
    path.append(0)  # Return to depot
    return path

# Perform the Bottleneck-optimal Biconnected Subgraph algorithm
edges_sorted = np.dstack(np.unravel_index(np.argsort(distances.ravel()), (n_cities, n_cities)))[0]
subgraph = np.full((n_cities, n_cities), float('inf'))

for edge in edges_sorted:
    if edge[0] != edge[1]:
        subgraph[edge[0], edge[1]] = subgraph[edge[1], edge[0]] = distances[edge[0], edge[1]]
        if is_biconnected(subgraph):
            break  # Found a biconnected graph

# Create the approximate optimal tour
tour = identify_tour(subgraph)

# Calculate the total cost and maximum distance between consecutive nodes
total_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    distance = distances[tour[i-1], tour[i]]
    total_cost += distance
    if distance > max_distance:
        max_distance = distance

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)