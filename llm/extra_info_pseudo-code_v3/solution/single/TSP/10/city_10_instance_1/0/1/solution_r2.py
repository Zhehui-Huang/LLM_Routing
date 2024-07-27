import math
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms import approximation as apxa

# Define cities and their positions
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Compute Euclidean distance matrix
positions = list(cities.values())
distance_matrix = squareform(pdist(positions, metric='euclidean'))

# Create a complete graph from the distance matrix
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = distance_matrix[i][j]

# Step 1: Compute a Minimum Spanning Tree (MST) of G
mst = apxa.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify vertices with odd degree in T
odd_degree_nodes = [n for n, deg in mst.degree() if deg % 2 == 1]

# Create subgraph induced by nodes with odd degree
odd_degree_subgraph = G.subgraph(odd_degree_nodes)

# Step 3: Find minimum-weight perfect matching (MWM)
mwm = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of MST and MWM to form a multigraph H
H = nx.MultiGraph(mst)
H.add_edges_from(mwm)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
seen = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in seen:
        seen.add(u)
        hamiltonian_circuit.append(u)
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the total travel cost
total_cost = round(sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:])))

# Output result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)