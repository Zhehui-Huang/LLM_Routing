import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# Coordinates of the cities including the depot city
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Step 1: Create the complete graph G with weights as Euclidean distances
def create_graph(coords):
    G = nx.complete_graph(len(coords))
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            G[i][j]['weight'] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    return G

# Step 2: Compute a minimum spanning tree (MST) of G
def get_mst(G):
    return nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Identify set O of vertices with odd degree in MST
def find_odd_degree_vertices(T):
    return [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 4: Find a minimum weight perfect matching M in the subgraph induced by O
def find_min_weight_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    matching = max_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return matching

# Step 5: Combine the edges of T and M to form a multigraph H
def create_multigraph(T, matching):
    H = nx.Graph()
    H.add_nodes_from(T.nodes(data=True))
    H.add_edges_from(T.edges(data=True))
    H.add_edges_from(matching, weight=[T[u][v]['weight'] for u, v in matching])
    return H

# Step 6: Find Eulerian circuit in H, skipping repeated vertices
def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def create_hamiltonian_circuit(circuit):
    path = []
    visited = set()
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # complete the circuit
    return path

# Step 7: Calculate travel cost
def calculate_cost(path, G):
    cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
    return cost

# Executing the Christofides algorithm
G = create_graph(coords)
T = get_mst(G)
odd_vertices = find_odd_degree_vertices(T)
matching = find_min_weight_matching(G, odd_vertices)
H = create_multigraph(T, matching)
circuit = find_eulerian_circuit(H)
path = create_hamilton Sagittarian_circuit(circuit)
total_cost = calculate_cost(path, G)

print("Tour:", path)
print("Total travel cost:", total_cost)