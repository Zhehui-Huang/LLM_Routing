import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
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

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)

# Step 1: Compute a Minimum Spanning Tree T of G
T = minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes if T.degree[v] % 2 != 0]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
G_sub = G.subgraph(O)
M = min_weight_matching(G_sub, maxcardinality=True, weight="weight")

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
euler_path = list(eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit by skipping repeated vertices
hamiltonian_path = []
visited = set()
for u, v in euler_path:
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)
if hamiltonian_path[0] != 0:
    hamiltonian_path.insert(0, 0)
if hamiltonian_path[-1] != 0:
    hamiltonian_path.append(0)

# Calculate the tour cost
tour_cost = sum(G[u][v]["weight"] for u, v in zip(hamiltonian_path[:-1], hamiltonian_path[1:]))

# Output the results
print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {tour_cost}")