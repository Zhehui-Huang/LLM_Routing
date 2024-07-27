import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial.distance import euclidean
from scipy.optimize import linear_sum_assignment

def euclidean_distance(points):
    n = len(points)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = euclidean(points[i], points[j])
    return dist_matrix

def minimum_spanning_tree(dist_matrix):
    G = nx.complete_graph(len(dist_matrix))
    for i in range(len(dist_matrix)):
        for j in range(len(dist_matrix)):
            G[i][j]['weight'] = dist_matrix[i][j]
    T = nx.minimum_spanning_tree(G)
    return T

def find_odd_degree_vertices(T):
    return [v for v in T.nodes if T.degree[v] % 2 != 0]

def min_weight_matching(subgraph, odd_vertices):
    complete_subgraph = subgraph.subgraph(odd_vertices).copy()
    min_weight_match = nx.Graph()
    for u, v, d in complete_subgraph.edges(data=True):
        if u != v:
            min_weight_match.add_edge(u, v, weight=-d['weight'])
    # Matching is computed on the negative weights graph
    match = nx.max_weight_matching(min_weight_match, maxcardinality=True)
    return match

def eulerian_circuit(H):
    circuit = list(nx.eulerian_circuit(H))
    return [u for u, v in circuit]

def hamiltonian_circuit(circuit, start_node):
    seen = set()
    path = []
    for node in circuit:
        if node not in seen:
            seen.add(node)
            path.append(node)
        if len(seen) == len(circuit):
            break
    path.append(start_node)  # return to start
    return path

# Coordinates of cities including the depot
coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Step 1: Create distance matrix
dist_matrix = euclidean_distance(coordinates)

# Step 2, 3 and 4: Compute MST and find odd vertices
T = minimum_spanning_tree(dist_matrix)
O = find_odd_degree_vertices(T)

# Step 5: Find minimum-weight perfect matching on odd-degree vertices
M = min_weight_matching(T, O)

# Step 6 and 7: Combine the edges of T and M to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 8: Find an Eulerian circuit in H
circuit = eulerian_circuit(H)

# Step 9: Create Hamiltonian circuit from Eulerian circuit
tour = hamiltonian_circuit(circuit, 0)

# Calculate the total travel cost
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")