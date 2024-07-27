import numpy as np
import networkx as nx
from itertools import combinations

# City coordinates
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

# Complete graph with weights
G = nx.Graph()
for u, v in combinations(cities.keys(), 2):
    dist = euclidean_distance(cities[u], cities[v])
    G.add_edge(u, v, weight=dist)

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify vertices with odd degree in the MST
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3 and 4: Find a minimum-weight perfect matching and combine with MST
odd_subgraph = G.subgraph(O)
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, True, weight='weight')
H = nx.Graph(T)
H.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in the multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
hamiltonian_circuit.append(0)  # returning to the depot

# Calculate the cost of the tour
total_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_cost += G[hamiltonian_circuit[i - 1]][hamiltonian_circuit[i]]['weight']

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel points:", total_cost)