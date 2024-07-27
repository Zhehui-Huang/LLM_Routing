import numpy as np
import networkx as nx
from scipy.spatial import distance
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms import eulerian_circuit

# Define the city coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Construct a complete graph
def euclidean_distance(p1, p2):
    return distance.euclidean(p1, p2)

G = nx.complete_graph(len(cities))
for i in G.nodes:
    G.nodes[i]['pos'] = cities[i]

for u, v in G.edges:
    G.edges[u, v]['weight'] = euclidean_distance(cities[u], cities[v])

# Step 1: Compute a Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in the MST
odd_degree_nodes = [v for v in T.nodes if T.degree(v) % 2 == 1]

# Step 3: Find minimum weight perfect matching in the subgraph induced by odd vertices
odd_subgraph = nx.subgraph(G, odd_degree_nodes)
matching = max_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Add matching edges to the MST
T.add_edges_from(matching)

# Step 5: Find an Eulerian circuit
eulerian_path = list(eulerian_circuit(T, source=0))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit by skipping repeated vertices
hamiltonian_path = [0]
visited = set()
visited.add(0)

for u, v in eulerian_path:
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)
hamiltonian_path.append(0)  # return to the start

# Step 7: Calculate total travel cost
total_cost = sum(G.edges[hamiltonian_path[i], hamiltonian_path[i + 1]]['weight'] for i in range(len(hamiltonian_path) - 1))

# Output
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)