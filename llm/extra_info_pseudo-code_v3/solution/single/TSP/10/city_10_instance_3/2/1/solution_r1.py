import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform

def euclidean_distance(points):
    return squareform(pdist(points, metric='euclidean'))

def minimum_spanning_tree(dist_matrix):
    G = nx.Graph()
    num_nodes = len(dist_matrix)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    T = nx.minimum_spanning_tree(G)
    return T

def find_odd_degree_vertices(T):
    return [v for v in T.nodes() if T.degree(v) % 2 != 0]

def min_weight_matching(T, odd_vertices):
    subgraph = T.subgraph(odd_vertices)
    min_weight_match = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    return min_weight_match

def make_multigraph_eulerian(T, matching):
    H = nx.MultiGraph(T)
    H.add_edges_from(matching)
    return H

def eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def hamiltonian_path(eulerian_path):
    path = []
    visited = set()
    for u, v in eulerian_path:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # return to the start point
    return path

# Coordinates of cities including the depot
coordinates = np.array([(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)])

# Step 1: Create distance matrix
dist_matrix = euclidean_distance(coordinates)

# Steps 2 & 3: Compute MST
T = minimum_spanning_tree(dist_matrix)

# Step 4: Identify odd degree vertices
odd_vertices = find_odd_degree_vertices(T)

# Step 5: Minimum weight perfect matching
matching = min_weight_matching(T, odd_vertices)

# Step 6: Combine the edges of T and M to form multigraph H
H = make_multigraph_eulerian(T, matching)

# Step 7: Find an Eulerian circuit in H
eulerian_path = eulerian_circuit(H)

# Step 8: Convert it to Hamiltonian circuit
tour = hamiltonian_path(eulerian_path)

# Calculate the total travel cost
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")