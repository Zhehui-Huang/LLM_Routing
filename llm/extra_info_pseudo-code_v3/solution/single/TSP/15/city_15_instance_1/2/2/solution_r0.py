import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx import Graph, eulerian_circuit
import networkx.algorithms.matching as nxm

# Define the city coordinates
cities = np.array([
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
])

# Compute Euclidean distances
distance_matrix = squareform(pdist(cities))

# Construct MST
mst_matrix = minimum_spanning_tree(distance_matrix).toarray()

# Convert MST to a graph
G = Graph()
num_cities = len(cities)
for i in range(num_cities):
    for j in range(num_cities):
        if mst_matrix[i, j] > 0:
            G.add_edge(i, j, weight=mst_matrix[i, j])

# Find vertices with odd degree
odd_degree_nodes = [v for v in G.nodes if G.degree(v) % 2 == 1]

# Find minimum weight perfect matching on subgraph induced by odd_degree_nodes
subgraph = G.subgraph(odd_count_nodes)
matching = nxm.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matching edges to graph
G.add_edges_from(matching)

# Find an Eulerian circuit
e_circuit = list(eulerian_circuit(G, source=0))

# Convert Eulerian to Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = []
for u, _ in e_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
hamiltonian_circuit.append(0)  # End at the starting node

# Calculate total cost of the tour
total_cost = sum(
    distance_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1)
)

# Output result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)