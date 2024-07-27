import numpy as more_info
import networkx as nx
import itertools

# Coordinates of the cities
coordinates = [
    (50, 42), # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Function to calculate the Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return more_info.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create graph
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.edges[i, j]['weight'] = euclidean_distance(coordinates[i], coordinates[j])

# Step 1: Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in the MST
odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]

# Step 3: Find minimum weight perfect matching in the subgraph induced by odd_degree_nodes
subgraph = nx.subgraph(G, odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of MST and min_weight_matching to form a multigraph
multigraph = nx.MultiGraph(mst)
multigraph.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multigraph))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit by skipping repeated vertices
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculating the total travel cost
total_cost = sum(G.edges[hamiltonian_circuit[i], hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the result as specified
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")