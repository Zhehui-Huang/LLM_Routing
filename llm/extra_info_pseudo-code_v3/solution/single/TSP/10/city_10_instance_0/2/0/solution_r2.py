import math
import networkx as nx
from itertools import combinations

# Define the coordinates of the cities
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 
    4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
    8: (61, 90), 9: (42, 49)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating the complete graph G
G = nx.Graph()
for i, coord1 in cities.items():
    for j, coord2 in cities.items():
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(coord1, coord2))

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T
O = [node for node in T.nodes if T.degree(node) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
min_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Add the edges of M to T to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # to complete the tour by returning to the starting city

# Calculate the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the tour and the total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)