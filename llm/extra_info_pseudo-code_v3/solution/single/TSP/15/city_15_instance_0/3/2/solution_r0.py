import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# City coordinates
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

def calculate_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

G = calculate_distances(coordinates)

# Step 1: Compute MST of G
mst = minimum_spanning_tree(G)

# Create a graph
graph = nx.Graph(mst)

# Step 2: Find vertices with odd degrees
odds = [v for v, d in graph.degree() if d % 2 == 1]

# Create the subgraph using vertices with odd degrees
odd_graph = nx.subgraph(graph, odds)

# Step 3: Minimal weight perfect matching in the subgraph induced by odd-degree vertices
matching_graph = nx.complete_graph(odd_graph, nx.Graph())
for u, v, d in matching_graph.edges(data=True):
    d['weight'] = euclidean(coordinates[u], coordinates[v])

# Matching
matching = nx.algorithms.matching.min_weight_matching(matching_graph, maxcardinality=True, weight='weight')

# Add matching edges to the original graph
graph.add_edges_from(matching)

# Step 5: Find Eulerian circuit
eulerian_circuit = nx.eulerian_path(graph)  # Eulerian path/circuit

# Convert to Hamiltonian by skipping visited nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Make sure we start and end at the depot city 0
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)