import networkx as nx
import numpy as from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46),
    6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47),
    11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Creating the graph with weighted edges between each pair of cities
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            dist = round(euclidean(cities[i], cities[j]), 2)
            G.add_edge(i, j, weight=dist)

# Step 1: Compute a minimum spanning tree (MST) from the graph
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find nodes with an odd number of edges in MST
odds = [node for node, degree in T.degree if degree % 2 == 1]

# Step 3: We need to use the subgraph induced by odd degree vertices, and find a minimum weight perfect matching
subgraph = G.subgraph(odds)
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Add the matching to the minimum spanning tree to make it Eulerian
T.add_edges_from(matching)

# Step 5: Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Transform Eulerian circuit into a Hamiltonian circuit (skip repeated vertices)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Returning to the starting point, depot city

# Calculate the total distance of the circuit
total_distance = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print('Tour:', hamiltonian_circuit)
print('Total travel cost:', total_distance)