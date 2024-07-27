import numpy as np
import networkx as nx

# Coordinates of the cities including the depot
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Creating the complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in MST
odd_degree_vertices = [v for v in mst.nodes if mst.degree(v) % 2 != 0]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O.
odd_graph = G.subgraph(odd_degree_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add the edges from the perfect matching to the MST.
mst.add_edges_from(min_weight_matching)

# Create an eulerian circuit from the graph with added edges
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Make a list of unvisited cities for Hamiltonian Circuit
visited = set()
hamiltonian_circuit = []

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # add the depot city at the end to complete the circuit

# Calculate the tour cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)