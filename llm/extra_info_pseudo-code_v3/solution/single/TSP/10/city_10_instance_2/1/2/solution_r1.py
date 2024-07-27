import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Define coordinates of the cities
coords = np.array([
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
])

# Compute the full distance matrix
dist_matrix = squareform(pdist(coords))

# Compute the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix))
mst = csr_matrix(mst)
mst = mst.toarray()

# Create graph from MST
G = nx.from_numpy_matrix(mst)

# Find vertices with odd degree in the MST
odd_degree_nodes = [v for v, d in G.degree() if d % 2 == 1]

# Create a subgraph with these odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching in the induced subgraph on odd-degree vertices
for zero_fill in np.arange(0.1, 10, 0.1):
    try:
        perfect_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
        break
    except:
        subgraph = nx.from_numpy_matrix(dist_matrix + np.eye(len(odd_degree_nodes)) * zero_fill)

# Adding the edges from the perfect matching to the graph
G.add_edges_from(perfect_match)

# Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(G, source=0))

# Convert Eulerian circuit to Hamiltonian path (avoid visited twice)
visited = set()
hamiltonian_path = []
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_path.append(v)

# Make sure the tour starts and ends at the depot city
if hamiltonian_path[0] != 0:
    idx = hamiltonian_path.index(0)
    hamiltonian_path = hamiltonian_path[idx:] + hamiltonian_path[:idx]
if hamiltonian_path[-1] != 0:
    hamiltonian_path.append(0)

# Calculate the total travel cost using the Hamiltonian path
total_cost = sum(dist_matrix[hamiltonian_path[i], hamiltonian_path[i+1]] for i in range(len(hamiltonian_path)-1))

# Print the outputs as specified
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)