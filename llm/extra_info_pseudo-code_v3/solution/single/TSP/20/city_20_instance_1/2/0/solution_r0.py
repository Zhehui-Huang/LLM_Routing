import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# City coordinates
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
          (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
          (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Compute pairwise Euclidean distances
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.complete_graph(len(cities))
for i, j in combinations(range(len(cities)), 2):
    G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# 1. Compute a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# 2. Identify vertices with odd degree in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# 3. Find minimum weight perfect matching on the induced subgraph by the odd nodes
odd_graph = G.subgraph(odd_degree_match)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# 4. Combine the edges of T and M to form a multigraph H
multigraph = nx.MultiGraph(mst)
multigraph.add_edges_from(min_weight campaigning)

# 5. Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(multigraph))

# 6. Convert to Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0) # return to the depot

# Calculate the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")