import numpy as np
import networkx as nx
from itertools import combinations

# Define city coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph with weighted edges based on Euclidean distances
G = nx.Graph()
for u, v in combinations(cities.keys(), 2):
    dist = euclidean_distance(cities[u], cities[v])
    G.add_edge(u, v, weight=dist)

# Step 1: Compute a minimum spanning tree (MST) of the graph
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in the MST
odd_degree_vertices = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Minimum-weight perfect matching for odd-degree vertices
subgraph = G.subgraph(odd_degree_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Union of MST and the matching to get the multigraph
H = nx.Graph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Create an Eulerian circuit from the multigraph
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
hamiltonian_circuit.append(0)  # return to the starting node

# Calculate the total travel cost of the tour
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)