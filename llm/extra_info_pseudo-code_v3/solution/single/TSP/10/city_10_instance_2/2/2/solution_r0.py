import numpy as np
import networkx as nx
from scipy.spatial import distance
from networkx.algorithms import minimum_spanning_tree, eulerian_circuit
from networkx.algorithms.matching import min_weight_matching

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Number of cities
n = len(cities)

# Calculate Euclidean distance between all pairs of cities
def euclidean_distance(c1, c2):
    return distance.euclidean(c1, c2)

# Create complete graph G with weights (distances)
G = nx.complete_graph(n)
for u in range(n):
    for v in range(u + 1, n):
        G.edges[u, v]['weight'] = euclidean _distance(cities[u], cities[v])

# Step 1: Compute a Minimum Spanning Tree (MST) T of G
T = minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in T to form set O
O = [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
M = min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in the multigraph H
circuit = list(eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit (skipping repeated vertices)
visited = set()
Hamiltonian_circuit = []
for u, v in circuit:
    if u not in visited:
        Hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        Hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure the tour starts and ends at the depot
if Hamiltonian_circuit[0] != 0:
    Hamiltonian_circuit.insert(0, 0)
if Hamiltonian_circuit[-1] != 0:
    Hamiltonian_circuit.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(G.edges[Hamiltonian_circuit[i], Hamiltonian_circuit[i + 1]]['weight'] for i in range(len(Hamiltonian_circuit) - 1))

# Output the results
print(f"Tour: {Hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")