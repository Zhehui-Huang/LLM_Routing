import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def compute_mst(G):
    return nx.minimum_spanning_tree(G)

def odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

def min_weight_perfect_matching(G, O):
    subgraph = G.subgraph(O)
    cost_matrix = nx.to_numpy_array(subgraph)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    matching = [(O[row_ind[i]], O[col_ind[i]]) for i in range(len(row_ind)) if row_ind[i] != colind[i]]
    return matching

def combine_edges(T, M):
    H = T.copy()
    H.add_edges_from(M)
    return H

def find_hamiltonian_circuit(Eulerian_circuit):
    visited = set()
    circuit = []
    for node in Eulerian_circuit:
        if node not in visited or node == 0:
            visited.add(node)
            circuit.append(node)
        if node == 0 and len(visited) == len(Eulerian_circuit):
            break
    return circuit

# Setting up cities and depot
locations = np.array([
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
])

# Compute distances between each pair of points
dist = distance_matrix(locations, locations)

# Create the complete graph with weighted edges based on distances
G = nx.complete_graph(len(locations))
for i in range(len(locations)):
    for j in range(len(locations)):
        G[i][j]['weight'] = dist[i][j]

# Step 1: Compute a minimum spanning tree of G
T = compute_mst(G)
# Step 2: Identify vertices with odd degree in T
O = odd_degree_vertices(T)
# Step 3: Find a minimum-weight perfect matching in the subgraph induced by O
M = min_weight_perfect_matching(G, O)
# Step 4: Combine edges of T and M
H = combine_edges(T, M)
# Step 5: Find an Eulerian circuit in H
Eulerian_circuit = list(nx.eulerian_circuit(H, source=0))
# Step 6: Make it a Hamiltonian circuit
hamiltonian_circuit = find_hamiltonian_circuit(Eulerian_circuit)

# Compute the cost of the Hamiltonian circuit
total_cost = sum(dist[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)