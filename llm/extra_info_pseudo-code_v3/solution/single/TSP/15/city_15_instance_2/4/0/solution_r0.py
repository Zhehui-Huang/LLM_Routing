import math
import networkx as nx
from scipy.spatial import distance_matrix
import numpy as np
from itertools import combinations

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# List of city coordinates including the depot city
cities = [
    (54, 87), # Depot city 0
    (21, 84), # City 1
    (69, 84), # City 2
    (53, 40), # City 3
    (54, 42), # City 4
    (36, 30), # City 5
    (52, 82), # City 6
    (93, 44), # City 7
    (21, 78), # City 8
    (68, 14), # City 9
    (51, 28), # City 10
    (44, 79), # City 11
    (56, 58), # City 12
    (72, 43), # City 13
    (6, 99)  # City 14
]

# Create the complete graph with the cities
num_cities = len(cities)
G = nx.Graph()
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree in T
O = [v for v in T.nodes if T.degree(v) % 2 != 0]

# Step 3: Find minimum-weight perfect matching in the subgraph induced by O
subG = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subG, maxcardinality=True)

# Step 4: Combine T and M to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure the tour ends at the starting point
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate total travel cost
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the tour and total travel cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_cost:.2f}")