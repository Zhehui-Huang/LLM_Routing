import math
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms.matching import min_weight_matching
from networkx.algorithms.euler import eulerian_circuit
import numpy as np

# Define the coordinates of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Create a function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create a fully connected graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Step 1: Compute a minimum spanning tree of the graph G
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices of odd degree in the MST
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find minimum weight perfect matching on the subgraph induced by odd-degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)
min_matching = min_weight_matching(odd_subgraph, True)

# Step 4: Add the matching edges to T
T.add_edges_from(min_matching)

# Step 5: Find an Eulerian circuit in the augmented graph
circuit = list(eulerian_circuit(T, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian path (shortcutting)
visited = set()
hamiltonian_circuit = [0]

for u, v in circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Ensure the tour returns to the start
hamiltonian_circuit.append(0)

# Calculate tour cost
tour_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {tour_cost}")