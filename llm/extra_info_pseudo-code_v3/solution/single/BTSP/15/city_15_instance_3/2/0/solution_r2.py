import numpy as np
import networkx as nx
from itertools import permutations

# Coordinates of cities with the first city as the depot
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Create a full graph with nodes and edges weighted by the Euclidean distance
def create_graph():
    G = nx.Graph()
    G.add_nodes_from(range(len(coordinates)))
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            G.add_edge(i, j, weight=dist)
            G.add_edge(j, i, weight=dist)  # Graph is undirected
    return G

# Check for Hamiltonian cycle with bottleneck minimalization
def find_btsp_tour(G):
    nodes = list(G.nodes())
    min_max_dist = float('inf')
    best_tour = None
    
    # Checking every permutation of nodes to find the viable Hamiltonian circuit
    for perm in permutations(nodes):
        # Ensure it's a round trip back to the initial node (depot)
        perm += (perm[0],)
        max_dist_in_tour = max(G[perm[i]][perm[i+1]]['weight'] for i in range(len(perm)-1))
        if max_dist_in_tour < min_max_dist:
            min_max_dist = max_dist_in_tour
            best_tour = perm
            
    return best_tour, min_max_dist

# Set up and solve the BTSP
graph = create_graph()
tour, max_edge_distance = find_btsp_tour(graph)

# Calculating total cost of the tour
total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Output the required results
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge_distance:.2f}")