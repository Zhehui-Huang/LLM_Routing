import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def calculate_euclidean_distance(coords1, coords2):
    return np.linalg.norm(np.array(coords1) - np.array(coords2))

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Create a complete graph
G = nx.complete_graph(len(cities))

# Add distances to the graph edges
for u, v in G.edges():
    G[u][v]['weight'] = calculate_euclidean_distance(cities[u], cities[v])

# Find Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Determine vertices with odd degree in MST
odd_vertices = [v for v, degree in dict(mst.degree()).items() if degree % 2 == 1]

# Create the induced subgraph on odd degree vertices
odd_subgraph = mst.subgraph(odd_vertices)
complete_odd_graph = nx.complete_graph(odd_vertices)

# Add weights to the complete graph of odd vertices
for u, v in complete_odd_graph.edges():
    complete_odd_graph[u][v]['weight'] = G[u][v]['weight']

# Find Minimum-Cost Perfect Matching
mate = nx.algorithms.matching.min_weight_matching(complete_odd_graph, maxcardinality=True, weight='weight')

# Add matching edges to the MST
mst.add_edges_from(mate)

# Create an Eulerian circuit from the MST with added edges
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Remove repeated nodes to get a Hamiltonian circuit (approximate solution)
visited = set()
tour = []
for node, _ in eulerian_circuit:
    if node not in visited:
        visited.add(node)
        tour.append(node)
tour.append(0)  # return to depot

# Calculate the total travel cost
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)