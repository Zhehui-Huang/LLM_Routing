import numpy as np
import networkx as nx
from scipy.spatial import distance
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

# Calculate the Euclidean distance between each pair of cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph G
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree (MST) T of G
mst = nx.minimum_spanning_tree(G.copy())

# Step 2: Identify the set O of vertices with odd degree in T
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
O_subgraph = nx.Graph()
O_subgraph.add_nodes_from(odd_degree_nodes)
for u, v in combinations(odd_degree_nodes, 2):
    O_subgraph.add_edge(u, v, weight=euclidean_distance(cities[u], cities[v]))

matching = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True)

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(mst)
H.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure the tour starts and ends at the depot city
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)