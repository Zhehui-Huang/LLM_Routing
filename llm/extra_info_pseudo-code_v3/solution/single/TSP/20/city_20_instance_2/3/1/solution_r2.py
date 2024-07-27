import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Define the coordinates of the cities
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49),
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to compute distance matrix based on Euclidean distance
def compute_distances(cities):
    coords = np.array(list(cities.values()))
    return distance_matrix(coords, coords)

dist_matrix = compute_distances(cities)

# Creating a complete graph with distances as weights
G = nx.complete_graph(len(cities))
for i, j in combinations(cities, 2):
    G[i][j]['weight'] = dist_matrix[i, j]

# Minimum Spanning Tree (MST) of the graph
MST = nx.minimum_spanning_tree(G, weight='weight')

# Find all vertices in the MST with odd degree
odd_degree_vertices = [v for v in MST.nodes() if MST.degree(v) % 2 == 1]

# Induced subgraph on the odd degree vertices
odd_subgraph = G.subgraph(odd_degree_vertices)

# Minimum weight perfect matching on the subgraph of odd degree vertices
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Add the edges of the matching to the MST
multi_graph = nx.MultiGraph(MST)
multi_graph.add_edges_from(matching)

# Eulerian circuit in the constructed multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian circuit to Hamiltonian circuit (simple path, no repeated nodes)
visited = set()
hamiltonian_circuit = [0]
total_cost = 0
last_city = 0

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
        total_cost += dist_matrix[last_city][v]
        last_city = v

# Closing the tour by returning to the starting point
hamiltonian_circuit.append(0)
total_cost += dist_matrix[last_city][0]

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")