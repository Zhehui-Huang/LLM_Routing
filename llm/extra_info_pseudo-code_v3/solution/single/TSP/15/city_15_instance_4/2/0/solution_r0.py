import networkx as nx
import numpy as np
from itertools import combinations

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46),
    6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47),
    11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Creating the graph with weighted edges between each pair of nodes
G = nx.complete_graph(len(cities))
for u, v in combinations(cities, 2):
    G[u][v]['weight'] = distance(u, v)
    G[v][u]['weight'] = distance(u, v)  # Undirected graph, mirror edge

# Step 1: Compute a minimum spanning tree
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in the MST
odd_vertices = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find a minimum weight perfect matching
O = G.subgraph(odd_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(O, True)

# Step 4: Add edges of the minimum matching to the tree
T.add_edges_from(mina_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(T))

# Step 6: Convert it into a Hamiltonian path (avoid repetitions)
# skipping visited nodes - making a path unique
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # Complete the tour by returning to the depot

# Calculate the total distance
total_distance = sum(distance(hamiltonian_circuit[i], hamiltonian_circuit[i+1]) for i in range(len(hamiltonian_circuit)-1))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_distance, 2))